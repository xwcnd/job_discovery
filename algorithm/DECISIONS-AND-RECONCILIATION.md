# Decision lanes, duplicate identity and tracker reconciliation

## Lane A — Verified fit

Qualifying conditions (ALL): current exact vacancy is identifiable; complete reliable JD and actual employer/team/function verified; all real employer mandatory requirements supported; defining work at a credible direct/equivalent level; relevant legal/working condition gates resolved; score at/above configured threshold (default 73%); no established closure. An actual employer-specific apply URL is preferable, but a missing direct employer-controlled job URL is **not itself disqualifying** where the current complete job is otherwise verified. An otherwise validated currently advertised job may be Lane A with `PAGE LIVE / APPLY UNKNOWN` clearly noted, provided there is **no credible conflicting evidence of closure**. A contradictory/stale/possibly closed role goes to B for current-status verification; never assert acceptance merely from a viewable JD.

**Action:** add/update one row in the private `Job Matches` tab with numeric fit and concise evidence. Verify write and avoid duplicate entries. User-facing: company/title/direct source, fit QA score, strongest personal experience, non-disqualifying gaps, source status.

## Lane B — Promising but consequentially unverified

Use when one or more meaningful gates cannot be verified (complete JD unavailable, work authorization unknown, role-defining depth unclear, current apply status materially uncertain, ambiguous degree equivalence). Distinguish an actual question from an unknown that cannot be resolved through the candidate (e.g., employer website is blocked). Prioritize a short list of consequential prospects.

**Action:** do not assign a passing numeric score; do not write to verified `Job Matches`. In chat give an actual link, real matching evidence, the **specific blocker**, and **one useful next question or targeted verification action**. Avoid re-asking answers already known from primary records or previous corrections.

**Variant: User-accepted gap** — where candidate **knows** they have not met a listed requirement but still chooses to apply. Support honest application preparation while preserving the `NOT MET` status; it is not Lane A.

## Lane C — Excluded, nonmatch, closed or duplicate

Use for confirmed unmet hard gates, clearly insufficient specialist domain/technical leadership, non-target roles, expired openings, duplicates, or fit below threshold after valid gates. Report succinct counts with decisive reasons, not a flood of rejected listings. Keep useful historical reasoning privately to avoid repeating the same false positive.

## Stable job identity for deduplication

Priority of keys:
1. Exact employer/authorized ATS requisition ID + hiring entity (when known).
2. LinkedIn job ID + employer/title context.
3. Canonical exact vacancy URL, removing tracking parameters but keeping job-specific path/ID.
4. Company + exact job title + location (manual check; can be separate requisitions).

**Email message ID** is a separate input-processing key: the same job may appear in multiple digests or from multiple sources. A company lead without an exact vacancy is not a job identity.

Do not confuse genuinely distinct requisitions with duplicate posting IDs or replace one open title with a similar but different position.

## Reconciliation algorithm

For each new assessment or corrected existing job:

1. **Read the current spreadsheet**, not a screenshot or remembered row number. Confirm actual header, percentage format, formulas, filters and number of rows.
2. Search for the stable key(s), employer/title and URLs. Resolve same-title duplicates manually where job IDs differ.
3. Compare new Lane with any existing state:

| Previous state | New state | Transaction |
|---|---|---|
| No row | A | Insert once; store numeric score and current evidence; read back |
| A | A | Update existing row only if needed; verify no duplication |
| A | B | **Delete entire verified row**; preserve private reason; read back zero verified rows |
| A | C / closed / below threshold | **Delete entire verified row**; preserve private reason; read back zero |
| B/C | A | Verify complete new evidence and current JD; insert once |
| B/C | B/C | Keep out of verified tracker; optional private audit update |

4. Write authorized audit record in a **separate private** log (template provided). Record date, stable ID, previous/new decision, decisive evidence and whether the actual sheet was changed/read back.
5. If deletion affects row indices, do not reuse previously saved references; find subsequent targets again by ID. Preserve neighboring rows, styles, numeric formats, formulas and validation.
6. Report concrete results: `ADDED`, `UPDATED`, `REMOVED`, `ALREADY PRESENT`, `NOT WRITTEN / CONNECTOR ERROR`, `BLOCKED / REQUIRES AUTHORIZATION`. Never claim success before readback.

## Source conflicts and correction policy

Disagreement between indexed search text and a current rendered posting is a **source-quality problem**, not license to average requirements. Revisit exact current employer page and the candidate's complete screenshot. If the live qualification list omits a stale listed certificate, retract that purported hard requirement. If neither source is verifiable, classify unresolved and do not manufacture a pass/reject.

A user saying `this looks suitable` is an interest signal only. They may direct the assistant to work on the application regardless, but such a preference does not override factual eligibility or threshold classification.

## Privacy of decisions

Public algorithm files must not contain real user job URLs or private sheet IDs. Private actual trackers/audit may include personal context only within the user's own connected account and appropriate access permissions.
