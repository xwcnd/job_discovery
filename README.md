# Job Discovery for ChatGPT

A reusable, human-supervised workflow for **finding, verifying, ranking, and tracking job opportunities against your actual career evidence**. Designed for ChatGPT Projects, LinkedIn job-alert emails, Gmail, Google Sheets, and optional ChatGPT Scheduled tasks. No proprietary source code or hosted service is required.

> **New user?** Start with the [one-page setup checklist](docs/QUICK_SETUP_CHECKLIST.md) and then [START_HERE.md](START_HERE.md). **ChatGPT assistant?** If someone shared this repository URL and asked you to set up Job Discovery, open [START_HERE.md](START_HERE.md) first, then follow its onboarding protocol. Do not ask the user to publish their CV on GitHub.

## What the system does

`Job alerts / employer research -> extract individual vacancies -> verify exact live job descriptions -> check employer, team and actual job function -> map each requirement to candidate facts -> check mandatory gates -> score genuinely eligible jobs -> write verified matches to a private Google Sheet -> report unresolved opportunities in chat -> incorporate corrections and re-verify.`

The methodology makes two distinctions that matter:

- **Candidate-position fit is not document quality.** A well-written resume cannot create experience a candidate does not have.
- **Potentially relevant is not verified eligible.** A numerical score is never allowed to bypass an unsupported mandatory qualification or missing domain depth.

## Stage 2 — one vacancy per application chat

After identifying an opportunity, start a **new private ChatGPT Project chat** for that specific job. Use the [separate vacancy-application prompt](prompts/VACANCY_APPLICATION_WORKFLOW.md) and follow the [step-by-step application guide](docs/12-VACANCY-APPLICATIONS.md). It covers exact-JD analysis, source-supported tailored CV, separate cover-letter approval, contact research, outreach drafts, and ATS/forms. Keep real candidate contact details in private sources and never send/apply without explicit authorization.

## Quick start for a person

1. Review the [one-page setup checklist](docs/QUICK_SETUP_CHECKLIST.md), then open ChatGPT and paste the repository URL alongside the text in [prompts/STARTER_PROMPT.md](prompts/STARTER_PROMPT.md). If ChatGPT cannot access the repository, attach the release ZIP instead.
2. In ChatGPT, create a **private Project** for your job search. Add the text of [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) (or the [compact alternative](PROJECT_INSTRUCTIONS_COMPACT.md) if the instruction field rejects it) to the Project's instructions **and upload the canonical algorithm documents as reusable Project sources**, so later vacancy chats can still access the full rules. See [ChatGPT setup](docs/01-CHATGPT-SETUP.md).
3. Upload your **complete factual/base resume** and, ideally, a **detailed project and achievements portfolio**. Keep private records in your own Project or connected private Drive, **not this public GitHub repository**. Follow [career evidence setup](docs/02-CAREER-EVIDENCE.md).
4. Tell ChatGPT your target roles, locations, work authorization, salary preferences, must-have exclusions, and willingness to relocate/travel. Use [the sample configuration](templates/USER_CONFIGURATION.example.yaml) as a checklist, not as an online disclosure form.
5. Configure LinkedIn alerts and email delivery; connect the Gmail and Google Drive/Sheets apps available to your ChatGPT account; create your own tracker using [the CSV header](templates/Job_Matches.csv).
6. Validate the process on 2–3 vacancies by hand. **Only then**, if supported by your account, configure and test recurring monitoring using [prompts/DAILY_MONITOR.md](prompts/DAILY_MONITOR.md).

**Important platform limit:** ChatGPT Scheduled tasks created in a Project may **not** be able to read uploaded files or other files stored in that Project. For autonomous daily work, use separately connected private source documents (for example, Google Drive) only after an **actual source-access test**. If they cannot be read at scheduled-run time, the task must stop before scoring rather than pretend it read them. See [monitoring setup](docs/05-SCHEDULED-MONITORING.md).

## Start with the instructions, not the settings

| Need | Read |
|---|---|
| One-page setup checklist | [docs/QUICK_SETUP_CHECKLIST.md](docs/QUICK_SETUP_CHECKLIST.md) |
| Installation manual for humans | [INSTALLATION_MANUAL.md](INSTALLATION_MANUAL.md) |
| ChatGPT-led onboarding | [START_HERE.md](START_HERE.md) |
| Copyable Project instructions | [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md), [compact fallback](PROJECT_INSTRUCTIONS_COMPACT.md) |
| Overall architecture | [docs/00-WORKFLOW.md](docs/00-WORKFLOW.md) |
| Setup guide | [docs/01-CHATGPT-SETUP.md](docs/01-CHATGPT-SETUP.md) |
| Career evidence and privacy | [docs/02-CAREER-EVIDENCE.md](docs/02-CAREER-EVIDENCE.md), [SECURITY.md](SECURITY.md) |
| LinkedIn/Gmail alerts | [docs/03-LINKEDIN-GMAIL.md](docs/03-LINKEDIN-GMAIL.md) |
| Private Google Sheets tracker | [docs/04-GOOGLE-SHEETS.md](docs/04-GOOGLE-SHEETS.md) |
| Recurring monitoring | [docs/05-SCHEDULED-MONITORING.md](docs/05-SCHEDULED-MONITORING.md) |
| Core evidence-based screening algorithm | [algorithm/SCREENING.md](algorithm/SCREENING.md) |
| Decision lanes, duplicate handling, corrections | [algorithm/DECISIONS-AND-RECONCILIATION.md](algorithm/DECISIONS-AND-RECONCILIATION.md) |
| Case-study failure modes | [algorithm/FAILURE-PATTERNS.md](algorithm/FAILURE-PATTERNS.md) |
| Interactive career-evidence questionnaire | [docs/09-EVIDENCE-ENRICHMENT.md](docs/09-EVIDENCE-ENRICHMENT.md) |
| Employer research and historical/manual backlog | [docs/10-TARGETED-RESEARCH.md](docs/10-TARGETED-RESEARCH.md) |
| Quality tests | [tests/ACCEPTANCE_TESTS.md](tests/ACCEPTANCE_TESTS.md), [offline regression tests](tests/test_privacy_validator.py) |
| Publish to your GitHub repo | [PUBLISHING.md](PUBLISHING.md), [privacy and Git-history audit](docs/11-RELEASE-PRIVACY.md) |
| Tailored applications and forms | [docs/06-APPLICATIONS.md](docs/06-APPLICATIONS.md) |
| One-vacancy application chat prompt | [prompts/VACANCY_APPLICATION_WORKFLOW.md](prompts/VACANCY_APPLICATION_WORKFLOW.md) |
| Stage-2 guide for a person and ChatGPT | [docs/12-VACANCY-APPLICATIONS.md](docs/12-VACANCY-APPLICATIONS.md) |

## Defaults, not universal facts

The default score is **45% defining duties + 25% required technical competencies + 15% specific domain + 10% seniority/ownership + 5% preferences**, with a **73% verified-match threshold**, applied only *after* hard screening gates. These are **transparent heuristics, not probabilities of an offer**, and may be configured for a new user after documenting the change. Missing evidence does not mean demonstrated inability: consequential unknowns go to manual review, never fabricated scores.

## No automatic job applications

Discovery and tracking do not submit applications, contact employers, send emails, edit resumes, or change account settings without the user's separate authorization. Any external connection depends on the user's available ChatGPT features and their own permissions. LinkedIn alerts provide leads, not an exhaustive job database.

## Distribution and maintenance

This repository is intentionally **candidate-agnostic**. Do not fork personal data, private sheet URLs, Gmail messages, resumes, credentials, or interview records into it. Keep your filled configuration and assessment logs private; only generic workflow improvements belong here. Read [SECURITY.md](SECURITY.md), [docs/08-MAINTENANCE.md](docs/08-MAINTENANCE.md) and [public-release privacy safeguards](docs/11-RELEASE-PRIVACY.md). **Commit author/committer emails may reveal a person even when all files are sanitized; the entire Git history needs separate review before sharing.**

**Continuity check:** The repository link is a bootstrap, not a permanent substitute for the methodology inside each user's Project. Save the canonical screening and reconciliation documents to that Project as sources and verify they remain readable in a **new vacancy chat**. A Scheduled task has different file-access limits and requires its own independent preflight.

**Supported onboarding modes:** (A) ChatGPT with access to this GitHub repository, (B) downloaded/uploaded ZIP, or (C) manually supplied project-instructions and prompts. Merely pasting a link does not grant Gmail/Drive/GitHub access or activate an automation.

**External setup references** are listed in [sources/REFERENCE_URLS.md](sources/REFERENCE_URLS.md); confirm current UI and feature availability before relying on them.
