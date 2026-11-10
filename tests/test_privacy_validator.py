"""Synthetic offline tests for scripts/validate_package.py. No private data needed."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]


class ReleaseValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory(prefix="job_discovery_test_")
        self.addCleanup(self.tempdir.cleanup)
        self.repo = Path(self.tempdir.name) / "job_discovery"
        shutil.copytree(SOURCE, self.repo,
                        ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))

    def command(self, *argv, env=None):
        return subprocess.run(list(argv), cwd=self.repo, capture_output=True,
                              text=True, encoding="utf-8", env=env, check=False)

    def validator(self, *options):
        return self.command(sys.executable, "scripts/validate_package.py", *options)

    def setup_git(self):
        for argv in (("git", "init", "-q"),
                     ("git", "config", "user.name", "Project Maintainer"),
                     ("git", "config", "user.email", "123+maintainer@users.noreply.github.com"),
                     ("git", "add", "-A"),
                     ("git", "commit", "-qm", "Synthetic safe commit")):
            result = self.command(*argv)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_zip_style_content_scan_discloses_history_limit(self):
        result = self.validator()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("NOT CHECKED: Git commit metadata", result.stdout)
        required = self.validator("--require-git-history")
        self.assertNotEqual(required.returncode, 0)
        self.assertIn("full Git clone", required.stdout)

    def test_noreply_git_history_passes(self):
        self.setup_git()
        result = self.validator("--require-git-history")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("0 author/committer privacy issue(s)", result.stdout)

    def test_sensitive_commit_emails_are_flagged_but_not_echoed(self):
        self.setup_git()
        sensitive = "person" + "@" + "private.invalid"
        env = os.environ.copy()
        env.update({"GIT_AUTHOR_NAME": "Synthetic Person",
                    "GIT_AUTHOR_EMAIL": sensitive,
                    "GIT_COMMITTER_NAME": "Synthetic Person",
                    "GIT_COMMITTER_EMAIL": sensitive})
        added = self.command("git", "commit", "--allow-empty", "-qm",
                             "Synthetic unsafe commit", env=env)
        self.assertEqual(added.returncode, 0, added.stderr)
        result = self.validator("--require-git-history")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("email redacted", result.stdout)
        self.assertNotIn(sensitive, result.stdout)

    def test_public_release_requires_explicit_license(self):
        self.setup_git()
        result = self.validator("--public-release")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("LICENSE file", result.stdout)


if __name__ == "__main__":
    unittest.main()
