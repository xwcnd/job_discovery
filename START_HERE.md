# START HERE — Assistant bootstrapping and user onboarding

## If you are ChatGPT reading this from a repository link

Your task is to **help this individual establish their own private Job Discovery workflow**. This repository is generic methodology, **not** a candidate profile or evidence of a particular person's skills. Never infer personal facts from an example or from the original author's identity. Do not store personal data in this repository.

**First, verify access:** Read this file, [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md), [algorithm/SCREENING.md](algorithm/SCREENING.md), [algorithm/DECISIONS-AND-RECONCILIATION.md](algorithm/DECISIONS-AND-RECONCILIATION.md), and the relevant setup documents. If repo retrieval fails, ask the user to attach the downloadable ZIP or paste the documents; do not pretend you read inaccessible pages.

**Check what is already done**, then guide the user through the missing steps using the [one-page setup checklist](docs/QUICK_SETUP_CHECKLIST.md) as the progress tracker. Do not re-create a Project or tracker that already exists. Ask for missing information only when the current chat, Project sources, and accessible connected documents do not answer it. Never ask the user to paste confidential documents into a *public* GitHub issue or repository.

## Sequence to follow

1. **Explain the workflow in two sentences.** Verified eligible jobs can be written to a private tracking sheet; unresolved jobs appear in chat without a passing score.
2. **Check their starting point:** Do they already have a ChatGPT Project and a complete factual CV? If not, show the Project setup below. Ask one direct question at a time when only one fact is needed, or use a compact grouped checklist if several independent essentials are missing.
3. **Establish a private Project:** In ChatGPT, select New project, choose a name such as `My Job Discovery`, and insert [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) under Project settings (use [PROJECT_INSTRUCTIONS_COMPACT.md](PROJECT_INSTRUCTIONS_COMPACT.md) if the full text exceeds the available instruction field). Suggest keeping it private; optionally select project-only memory when available. **Also add the complete [SCREENING.md](algorithm/SCREENING.md), [DECISIONS-AND-RECONCILIATION.md](algorithm/DECISIONS-AND-RECONCILIATION.md), and [FAILURE-PATTERNS.md](algorithm/FAILURE-PATTERNS.md) as Project source files, or an equivalent reliably available source.** Verify the full documents can be retrieved in a later new chat; a URL pasted in an earlier chat is not enough proof.
4. **Collect evidence:** Ask for a full chronological/base CV (not only the 1–2-page tailored resume); detailed projects/roles and validated achievements; education/certifications; other primary supporting records. For each factual gap, use `UNKNOWN` and ask targeted follow-up. Respect confidentiality and employment restrictions. See [docs/02-CAREER-EVIDENCE.md](docs/02-CAREER-EVIDENCE.md).
5. **Collect preferences and eligibility:** Target roles/industries; locations/remote/relocation; work authorization per country; languages; travel; salary baseline and currency; exclusions; preferred reporting frequency/time zone. Distinguish personal preferences from employer requirements. Do not require a biography or sensitive identity fields to begin.
6. **Prepare the candidate's private system of record:** Establish versioned source links or uploaded files and a private tracker using [templates/Job_Matches.csv](templates/Job_Matches.csv). Verify authorized connector access and columns/formatting. No filled candidate configuration should be committed here.
7. **Configure alerts:** Guide through LinkedIn search/filter/job-alert email settings and Gmail checks using [docs/03-LINKEDIN-GMAIL.md](docs/03-LINKEDIN-GMAIL.md). Adapt sender addresses only after observing the user's actual alerts.
8. **Dry-run 2–3 exact jobs:** Retrieve complete current job descriptions, map evidence, apply **both** mandatory and functional applicability gates, then score only roles that pass. Demonstrate one qualified match and one manual/rejected scenario if available; do not fabricate live opportunities to satisfy a demo.
9. **Set up recurring monitoring, if requested and supported:** First test whether a scheduled task can independently read its *private* candidate sources, Gmail and Sheet. Scheduled tasks may not access Project-uploaded files. Use a separately connected private Drive source or another verified permitted mechanism. No source access means no unattended scoring. Create at most one monitoring task, inspect actual schedule and enabled state, and test an initial run.
10. **Finish with a verification report:** What works, what remains manual, what was connected, which private document is authoritative, whether daily monitoring actually exists and is enabled, and how to update it.

## Immediate user-facing starter message

> I can help you install the Job Discovery workflow in your own private ChatGPT Project. It will verify actual job requirements against your evidence and keep confirmed matches separate from unresolved opportunities. First, do you already have a private ChatGPT Project with your **complete base CV**, or should we create one?

If the user already provided the documents or answered the question, **skip it**. Never ask for passwords, access tokens, passport/immigration IDs, employer confidential files, or third-party private data.

## Additional optional branches

If the user's full CV lacks project-level detail, offer the [interactive evidence-enrichment workflow](docs/09-EVIDENCE-ENRICHMENT.md), rather than inventing missing skills. If they want more than LinkedIn digest matches, use [targeted employer/market research](docs/10-TARGETED-RESEARCH.md). Existing manual-review jobs may be kept in a separate **private** backlog, not the verified-match Sheet.

## Optional next stage: vacancy-specific application

When the user selects a job to pursue, **open a separate private Project chat for that one vacancy**. Use the [vacancy application prompt](prompts/VACANCY_APPLICATION_WORKFLOW.md) with the [Stage-2 human/assistant guide](docs/12-VACANCY-APPLICATIONS.md). The user supplies the complete JD in that chat; ChatGPT must not import the repository author's identity, and must ask approval separately before CV creation and before the cover-letter stage. This does not trigger automatic applications or change the discovery task.

## Safe completion criteria

A valid setup is not just a pasted prompt. It includes: the Project instructions, actual primary-source candidate records, established preferences, a verified-access private tracker, demonstrably functioning job assessments, tested email ingestion, and — only if enabled — a scheduled task with an independent source-access check. If any step cannot be completed, report **PARTIAL SETUP** and the exact blocker; do not claim automation is active.
