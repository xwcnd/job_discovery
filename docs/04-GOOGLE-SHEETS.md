# Private Google Sheets tracker

## Create the sheet

1. Create a **private** spreadsheet in the user's own Google Drive, for example `Job Discovery — My Matches`.
2. Add a worksheet exactly named **`Job Matches`**. Import or copy the header from [Job_Matches.csv](../templates/Job_Matches.csv); use **exactly 10 columns A:J**.
3. Freeze row 1; enable filters; set column G (`Fit %`) to **Percentage** (e.g., 82%, stored as numeric `0.82`, **not** the text `82%`).
4. Verify the Google Sheets connector can *read* the actual worksheet and, only after permission, write a test or a genuinely qualified job and read it back. Delete any test/synthetic row before using it as a real tracker.
5. Keep any historical/marginal research in your **private** optional audit, or in clearly labeled chat messages; the primary tab is verified-only.

## The standard schema

| Col | Name | Content |
|---|---|---|
| A | Date found | Date when newly discovered; not invented employer posting date |
| B | Company | Verified hiring organization, not a recruiter unless it is the actual employer |
| C | Position | Exact verified job title |
| D | Job URL | Original actual vacancy URL, not generic search page |
| E | Company job URL | Exact employer/authorized ATS **job-specific** URL, if verified; otherwise blank |
| F | Employer website | Verified corporate homepage, separate from E; blank if unverified |
| G | Fit % | Numeric 0.73–1.00 for qualified default-threshold jobs only |
| H | Strongest matching experience | Brief traceable **personal** evidence (company/project/role) |
| I | Gaps | Material non-disqualifying gaps, preferences or limitations; avoid sensitive details |
| J | Eligibility concerns | Real conditions and verification caveats, including posting/apply-state uncertainty |

## Allowed write policy

**Only Lane A** ([decision specification](../algorithm/DECISIONS-AND-RECONCILIATION.md)) may be inserted/updated into this sheet. A **real current exact job**, supported mandatory gates, demonstrated role-defining competence and passing numeric threshold are required. A promising vacancy missing a consequential required skill, exact JD or work authorization belongs to **manual chat review**, not here with a blank score. Do not copy the same job multiple times from several LinkedIn emails.

Before each batch, read the latest header, existing rows and sheet metadata. Match by stable job IDs and company/title/URL; preserve linked cells, formulas, number formats, data validation, filters and neighboring rows. Never assume a row index saved yesterday is still current.

## Corrections must be transactional

When a user disputes a score or when a job closes:

1. Re-check exact current vacancy/availability, employer and department, candidate evidence and both gating decisions.
2. Locate any existing qualified row **by identity**, not historic row number.
3. If it still qualifies, update its existing row, avoiding duplicates. If it no longer qualifies or is merely manual, **remove its entire row from `Job Matches`**, not only its score.
4. Record the reason in a private audit (the optional [Decision_Audit.csv](../templates/Decision_Audit.csv) header illustrates a separate historical record). Do not turn the verified tab into an audit log.
5. Read back the sheet and verify the rejected job has **zero** qualified rows, the intended records remain, and formulas/formatting are intact. Report failure if write/readback is unavailable.

Use explicit authorization for external changes, especially deleting rows. If a sheet contains existing mixed-status historical records, do not mass-delete them without evidence-based individual review.

## Source integrity

`Company job URL` must link to the **actual same job**, not to an employer homepage, generic careers index, different requisition, expired third-party copy or LinkedIn mirror. Missing E is allowed when the complete original posting is otherwise verifiable; however job application state should be reported accurately, with uncertainty where unresolved.
