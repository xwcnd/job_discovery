#!/usr/bin/env python3
"""Check a generic Job Discovery release without reading candidate private data.

File/content checks work on the ZIP distribution. Git commit author/committer
privacy checks require a full local Git clone. This is not a guarantee of full
anonymity or of live ChatGPT/Gmail/Sheets/scheduled-task behavior.
"""

import argparse
import csv
import pathlib
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED_HEADER = [
    "Date found", "Company", "Position", "Job URL", "Company job URL",
    "Employer website", "Fit %", "Strongest matching experience", "Gaps", "Eligibility concerns",
]
REQUIRED_FILES = [
    "README.md", "START_HERE.md", "INSTALLATION_MANUAL.md",
    "PROJECT_INSTRUCTIONS.md", "PROJECT_INSTRUCTIONS_COMPACT.md",
    "PUBLISHING.md", "SECURITY.md", ".gitignore",
    "docs/QUICK_SETUP_CHECKLIST.md", "docs/11-RELEASE-PRIVACY.md",
    "algorithm/SCREENING.md", "algorithm/DECISIONS-AND-RECONCILIATION.md",
    "algorithm/FAILURE-PATTERNS.md", "prompts/DAILY_MONITOR.md",
    "prompts/STARTER_PROMPT.md", "prompts/EVIDENCE_ENRICHMENT.md",
    "prompts/TARGETED_SEARCH.md", "docs/09-EVIDENCE-ENRICHMENT.md",
    "docs/10-TARGETED-RESEARCH.md", "templates/USER_CONFIGURATION.example.yaml",
    "templates/Job_Matches.csv", "templates/Manual_Review_Backlog.csv",
    "tests/ACCEPTANCE_TESTS.md", "tests/test_privacy_validator.py",
]
PRIVATE_PATTERNS = {
    "Google private document/folder URL": re.compile(
        r"https?://(?:docs|drive)\.google\.com/[^\s)\]`\"<>]{20,}", re.I
    ),
    "GitHub-style token": re.compile(r"(?:ghp_|github_pat_|gho_|ghu_|ghs_)[A-Za-z0-9_]{15,}"),
    "literal private credential assignment": re.compile(
        r"(?im)^\s*(?:password|access_token|api_key|secret_key)\s*[:=]\s*[A-Za-z0-9_-]{12,}\s*$"
    ),
}
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
TEXT_EXTENSIONS = {".md", ".csv", ".yaml", ".yml", ".json", ".txt", ".py", ".sh"}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SAFE_SAMPLE_EMAIL_DOMAINS = {"example.com", "example.org", "example.net"}
SAFE_OPERATIONAL_EMAILS = {
    "jobalerts-noreply@linkedin.com", "messages-noreply@linkedin.com",
    "noreply@github.com",
}
NOREPLY_PATTERN = re.compile(r"^[A-Za-z0-9.+_-]+@users\.noreply\.github\.com$", re.I)


def safe_email(email):
    email = email.strip().lower()
    if email in SAFE_OPERATIONAL_EMAILS or NOREPLY_PATTERN.fullmatch(email):
        return True
    return email.rsplit("@", 1)[-1] in SAFE_SAMPLE_EMAIL_DOMAINS


def check_git_history(errors, require_history=False):
    """Check reachable refs in local checkout, not remote caches or external forks."""
    if not (ROOT / ".git").exists():
        if require_history:
            errors.append("A full Git clone is required to inspect commit metadata; ZIP/static files are insufficient")
        else:
            print("NOT CHECKED: Git commit metadata (no .git directory; run in a full clone before sharing)")
        return
    try:
        # Separators avoid ambiguous splitting of names; do not echo sensitive emails.
        cmd = ["git", "log", "--all", "--format=%H%x1f%aE%x1f%cE%x1e"]
        proc = subprocess.run(cmd, cwd=ROOT, text=True, encoding="utf-8",
                              capture_output=True, check=True, timeout=20)
    except (OSError, subprocess.SubprocessError) as exc:
        errors.append(f"Git history could not be inspected: {type(exc).__name__}")
        return
    commits = [c.strip() for c in proc.stdout.split("\x1e") if c.strip()]
    if not commits:
        errors.append("Git repository contains no reachable commits to inspect")
        return
    violations = set()
    for commit in commits:
        parts = commit.strip().split("\x1f")
        if len(parts) != 3:
            errors.append("Unable to parse a Git commit's author/committer metadata")
            continue
        sha, author_email, committer_email = parts
        for role, address in (("author", author_email), ("committer", committer_email)):
            if not safe_email(address):
                violations.add((sha[:12], role))
    for sha, role in sorted(violations):
        errors.append(f"Commit {sha}: {role} address is not GitHub noreply (email redacted)")
    print(f"GIT HISTORY CHECKED: {len(commits)} reachable commit(s); "
          f"{len(violations)} author/committer privacy issue(s).")
    print("LIMIT: Git hosting caches, other refs, forked clones, issues and pull requests are not proven clean.")


def check(require_git_history=False, public_release=False):
    errors = []
    for relative in REQUIRED_FILES:
        p = ROOT / relative
        if not p.is_file() or p.stat().st_size == 0:
            errors.append(f"Required file missing or empty: {relative}")
    if errors:
        print("FAIL:\n" + "\n".join("- " + e for e in errors))
        return 1

    with (ROOT / "templates" / "Job_Matches.csv").open(newline="", encoding="utf-8") as stream:
        rows = list(csv.reader(stream))
        if not rows or rows[0] != EXPECTED_HEADER or len(rows) != 1:
            errors.append("Job_Matches.csv must contain exactly 10 required headers, no sample people/jobs")

    docs = sorted(ROOT.rglob("*.md"))
    scans = 0
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix not in TEXT_EXTENSIONS:
            continue
        if any(part in {".git", "__pycache__", ".venv"} for part in p.relative_to(ROOT).parts):
            continue
        scans += 1
        content = p.read_text(encoding="utf-8")
        for label, pattern in PRIVATE_PATTERNS.items():
            for _ in pattern.finditer(content):
                errors.append(f"{p.relative_to(ROOT)}: possible {label} (matched value redacted)")
        for match in EMAIL_PATTERN.finditer(content):
            if not safe_email(match.group(0)):
                errors.append(f"{p.relative_to(ROOT)}: possible personal/non-placeholder email (redacted)")
        if p.suffix == ".md":
            for match in LINK_PATTERN.finditer(content):
                link = match.group(1).split(' "', 1)[0].strip()
                raw = link.split("#", 1)[0].split("?", 1)[0]
                if not raw or raw.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                if not (p.parent / unquote(raw)).exists():
                    errors.append(f"{p.relative_to(ROOT)}: broken relative link {link!r}")

    config_path = ROOT / "templates" / "USER_CONFIGURATION.example.yaml"
    try:
        import yaml  # pip install pyyaml, if needed
        config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
        weights = config["screening"]["role_weights"]
        coefficients = config["screening"]["evidence_factors"]
        threshold = config["screening"]["verified_match_threshold"]
        if len(weights) != 5 or sum(weights.values()) != 100:
            errors.append("Scoring weights must contain five categories totaling 100")
        if coefficients != {"direct": 1.0, "substantiated_equivalent": 0.85,
                            "transferable": 0.5, "weak": 0.2, "none": 0.0}:
            errors.append("Evidence coefficients differ from the canonical algorithm")
        if not (0 < threshold < 1):
            errors.append("Default threshold must be a fraction in (0,1)")
        if config["candidate"]["current_factual_cv"] is not None:
            errors.append("Public configuration example has a filled candidate CV source")
        if config["sources"]["private_google_sheet_url"] is not None:
            errors.append("Public configuration example has a filled private tracker URL")
        if config["monitoring"]["optional_historical_rechecks_per_run"] not in {0, 2, 3, 4}:
            errors.append("Historical recheck sample count must be 0 (off) or 2-4")
    except ImportError:
        print("NOT CHECKED: deep YAML parsing (install PyYAML)")
    except Exception as exc:
        errors.append("YAML configuration invalid: " + str(exc))

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for target in ["START_HERE.md", "PROJECT_INSTRUCTIONS.md", "algorithm/SCREENING.md",
                   "docs/09-EVIDENCE-ENRICHMENT.md", "docs/10-TARGETED-RESEARCH.md",
                   "PROJECT_INSTRUCTIONS_COMPACT.md", "docs/QUICK_SETUP_CHECKLIST.md",
                   "docs/11-RELEASE-PRIVACY.md"]:
        if target not in readme:
            errors.append("README.md does not reference " + target)
    if len((ROOT / "PROJECT_INSTRUCTIONS_COMPACT.md").read_text(encoding="utf-8")) > 5000:
        errors.append("Compact Project instructions exceed 5,000 characters")

    check_git_history(errors, require_history=require_git_history or public_release)
    if public_release and not any((ROOT / name).is_file() for name in ("LICENSE", "LICENSE.md", "LICENSE.txt")):
        errors.append("No LICENSE file: repository owner must decide license before public redistribution")

    if errors:
        print("FAIL: " + str(len(errors)) + " issues:\n" + "\n".join("- " + e for e in errors))
        return 1
    print(f"PASS: {len(docs)} Markdown files, {scans} text files, links/schema/sample config checked.")
    if not require_git_history and not public_release:
        print("LIMIT: PASS is a local file check; it is NOT a public-release or full-privacy approval.")
    print("LIMIT: static checks cannot verify live account permissions, job postings, or recurring task execution.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-git-history", action="store_true",
                        help="fail if no .git checkout; check author/committer email privacy")
    parser.add_argument("--public-release", action="store_true",
                        help="require clean accessible Git history and an explicit LICENSE file")
    options = parser.parse_args()
    sys.exit(check(require_git_history=options.require_git_history,
                   public_release=options.public_release))
