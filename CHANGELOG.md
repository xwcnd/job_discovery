# Changelog

## 2026-11-10 — vacancy-specific application workflow

- Added a separate, fully documented one-vacancy ChatGPT chat workflow after job discovery.
- Adapted a user-provided application prompt to a reusable source-faithful version while removing identifying contact details, specific status/location directives, named signatures and private style-reference links.
- Preserved exact JD mapping, contact research, explicit CV/CL approval checkpoints, Google Docs QA, anti-loss/whole-document review, ATS support, outreach rules and evidence integrity.
- Linked the prompt and human/assistant onboarding guide from the README, START_HERE, applications guide and quick setup checklist; added synthetic acceptance scenarios.
- No personal CVs, private Google Docs source URLs or personal account data are included in the new workflow files.

## 2026-11-08 - release hardening 1.2

- Added a one-page first-time-user checklist with required private documents, optional connectors, settings and step-by-step verification tests.
- Added four synthetic regression tests for the privacy validator and its email-redaction behavior.
- Added privacy-aware Git history and public-release validation, including the distinction between sanitized files and sensitive commit author/committer metadata.
- Added a safe, explicitly manual Git history remediation guide; no historical commits were silently rewritten and no license was selected for the owner.
- Linked the onboarding, publishing, security, reference and regression-test documents to the new checks.
- Live Gmail/Sheets/ChatGPT automation and new-user installation remain separate tests, not guaranteed by document validation.

## 2026-11-08 — QA revision 1.1

- Reconciled the published ZIP's full 34-file structure with the separately supplied directory; kept all support files together.
- Strengthened new-user Project continuity: save the full screening/reconciliation/calibration documents as Project sources and verify retrieval in a new vacancy chat, not only the original onboarding conversation.
- Added a staged, project-mapped career-evidence questionnaire with strict personal-action, metrics and formal-method attribution.
- Added targeted employer/industry/date-window market sweeps, ageing-listing checks and optional high-priority historical/manual-review backlog outside the verified Sheet.
- Added generic forwarded-alert Gmail search templates and explicit two-GitHub-account access troubleshooting.
- Added a sub-5,000-character compact Project-instructions fallback if the full instructions exceed an account's field limit.
- Expanded static release validation and synthetic acceptance tests; these are **not** proof of actual Gmail, Sheets or Scheduled-task live behavior.

## Unreleased — candidate-agnostic first edition

- Consolidated a multi-stage job-alert screening and qualification process into a canonical algorithm.
- Added ChatGPT Project onboarding, privacy-first career-evidence requirements, LinkedIn/Gmail setup, Google Sheets tracking, task-access preflight, reusable prompts and acceptance tests.
- Added mandatory/functional dual gates, score methodology, three-lane output, full-row reconciliation of rejected verified jobs, specialist-depth checks, current-JD provenance requirements and truthful application boundaries.
- Replaced historical personal vacancy evaluations and company-specific anecdotes with synthetic failure scenarios.
- No live account, data connection, scheduled task or remote GitHub repository is modified by distributing this package.
