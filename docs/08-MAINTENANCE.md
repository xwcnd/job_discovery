# Maintenance and user corrections

## Two different kinds of changes

**Personal operational changes** (new CV, salary preference, work authorization, score correction, job closure) belong in **the user's private Project/configuration, task and tracker**. **Generic method improvements** belong in the reusable repository. Never commit personal job records, emails, private Drive links or fact-specific resumes to a public repo.

## Feedback protocol

For each useful correction:

1. Capture exactly what changed, its source, relevant role/project/requirement, and what earlier statement it supersedes.
2. Determine effect on job mandatory gates, company/domain screening, candidate evidence, source versions, fit score, current tracker, chat output, task prompt and private application documents.
3. Reassess the **whole affected job** with the current JD; do not patch one score cell while retaining a disqualified row.
4. Update the actual authorized operational systems: candidate source manifest/config, connected tracker and, if rule changes, **the live scheduled task prompt** (not just a GitHub file).
5. Read back affected sheet row(s) and automation configuration; preserve unrelated records and existing schedule unless the user wants it changed.
6. Record a concise **private** change log using [CHANGE_LOG.md](../templates/CHANGE_LOG.md) and report what was actually done, what remains blocked and why.
7. Abstract generalizable lessons into generic documentation only after removing all person-specific details and distinctive combinations.

## Source freshness

- Before substantive screening, confirm which base CV version is authoritative and that the candidate did not replace it with a narrower tailored document.
- Verify exact current JD and distinguish page content from cached search results.
- For older postings, inspect exact requisition and current application pathway; age alone is not proof that an opportunity is closed.
- Do not replace a missing employer-specific link with a generic careers page.
- When sheet rows are deleted, never trust saved row numbers.

## Regression check

Re-run the examples in [tests/ACCEPTANCE_TESTS.md](../tests/ACCEPTANCE_TESTS.md) after rule changes: false positive wrong industry, specialist depth, stale hard gate, user-accepted gap, and full-row reconciliation. Confirm real candidate fit and document quality remain separate.

## Optional skill elicitation and independent job searches

A generic skills list is not always enough for specialist scoring. Where important evidence is missing, use the staged, project-specific [evidence-enrichment questionnaire](09-EVIDENCE-ENRICHMENT.md), saving new real facts only to private records and retaining formal vs equivalent-method and team-vs-person distinctions. Don't repeatedly ask already settled questions.

For employer-targeted or historical-date-window sweeps, follow [targeted research](10-TARGETED-RESEARCH.md); distinguish what was actually searched from exhaustive coverage. Keep optional high-priority manual leads in a **private** backlog and reverify the exact current vacancy before promoting any role into the verified Sheet.

## Sharing with friends

Share only this **generic repository**. Every recipient must create their **own** private Project, connect their own Gmail/Drive, fill private profile and verify their own automation. The maintainer's existing scheduled task, private sheet and candidate files do not transfer through the link.
