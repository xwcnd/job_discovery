# Recurring Job Discovery — private ChatGPT task prompt template

**Only paste the body below into your own private task, after replacing its placeholders. Do not publish the filled version.** This template is a workflow description, not an automation by itself. Use the native Scheduled UI in ChatGPT/Work where supported, and verify task creation/enabled state.

---

Perform my **recurring evidence-based Job Discovery scan**. Read my **current full factual/base CV**, original project portfolio, private job-search configuration and private tracker **from the external, connector-accessible sources below**. No personal data may be sent to any public repository. Do not rely on a ChatGPT Project-uploaded file without testing access in this scheduled task; OpenAI currently documents that Scheduled tasks cannot access uploaded files/files stored in a Project.

**My private source configuration (fill privately before scheduling):**

- Authoritative complete/base CV, exact file/link and version: `[PRIVATE_BASE_CV_LINK_OR_ID]`.
- Original project list and other primary supporting evidence: `[PRIVATE_PROJECT_PORTFOLIO_LINK_OR_ID]`.
- Private preferences/authorization and source manifest: `[PRIVATE_CONFIG_AND_MANIFEST_LINK_OR_ID]`.
- My Google Sheets tracker (tab `Job Matches`, columns A:J): `[PRIVATE_GOOGLE_SHEET_LINK]`.
- Gmail account: `[CONNECTED_PERSONAL_GMAIL_ACCOUNT]`.
- Verified LinkedIn alert sender/search patterns: `[LIST_OBSERVED_SENDER_QUERIES_AND_OPTIONAL_FORWARDED_PATTERNS]`.
- Time zone and lookback: `[TIME_ZONE]`; rolling `7 days` unless explicitly changed.
- Default verified threshold: `73%`; weighting `45/25/15/10/5`; no hard-gate overrides.

### Phase 0 — read-access and configuration gate

1. Independently read the **complete current** authoritative CV and project portfolio at task runtime. Verify that the source ID/version matches my private manifest; do not silently substitute older tailored/generated CVs or memory. Check all mandatory connected-app permissions and required private preferences (jurisdiction/work authorization). If missing material sources, **STOP scoring and writing**; report `BLOCKED: CANDIDATE SOURCE INACCESSIBLE` and specify source name without exposing private content.
2. Read the actual current private Sheet `Job Matches` metadata, headers, rows and identifiers. If sheet read fails, report it. Reading Gmail alone does not authorize Sheet modification.
3. Respect existing user-configured scheduling; do not create a new task, alter this task's schedule, or re-enable paused tasks without the intended user controls.

### Phase 1 — inbox collection

Search each configured Gmail alert category **separately** within the rolling seven-day window. If sender patterns haven't been observed and verified, do not extrapolate another person's address. Generic **examples** for initial user validation:

```text
in:inbox from:jobalerts-noreply@linkedin.com newer_than:7d
in:inbox from:messages-noreply@linkedin.com newer_than:7d
```

For manually forwarded alerts, use only searches based on the current user's own forwarding account and validate the **original forwarded LinkedIn From header**; never treat every email from the forwarder as an alert. Search additional user-configured labels if messages are archived or filtered. Read full messages (not snippets); extract ALL distinct job cards, original URLs, LinkedIn IDs, titles, company names, locations, message IDs and dates. Distinguish explicit job advertisements from company-only news/notifications. A company-only mention may trigger focused research, not a fictitious job row. Record message counts and any read errors.

Deduplicate input by Gmail message ID and vacancy by employer ATS ID, LinkedIn job ID, canonical vacancy URL and grounded employer/title/location. Compare current Sheet and private audit to avoid repeated analysis/writes when there is no meaningful new information. A duplicated email does not necessarily mean an opening is closed.

**Optional older/manual backlog:** If my private config contains an accessible manual-review backlog, revisit 2–4 high-value unresolved exact vacancies after processing new alerts, within task limits. Reverify source, full JD, requirement depth and application state. If no configured backlog, do not invent one. The backlog is separate from `Job Matches`; do not score historical leads as current without new verification.

### Phase 2 — verify current exact openings

For each credible job, access the **same exact full current** employer/authorized ATS posting or, if not retrievable, a complete current employer-authored source. Record precise job ID, title, company, location, access date, original post date when available, source type (`LIVE-RENDERED`, `CURRENT FULL USER-SUPPLIED`, `CURRENT ATS API`, `SEARCH-INDEXED`, `THIRD-PARTY`), and whether the posting is current, closed or the application acceptance status is unresolved. Do not invent qualification bullets from snippets or combine job listings with similar titles. A visible JD is not always proof Apply is enabled.

Separately find the **exact direct official employer/authorized ATS vacancy URL**, if it exists, and verified **corporate homepage**. Keep the official job URL blank if only the generic employer careers page or a different requisition is found; a corporate homepage is not a job-specific source. Do not invent URLs.

For company-only leads, independently verify the employer and research CURRENT specific job openings in relevant target functions. Do not claim hiring solely from a company mention.

### Phase 3 — factual job-fit screening

For each exact current job, first establish:
- Employer business, hiring department and actual product/process/system.
- 2–4 defining day-to-day deliverables, relevant technical objects/operating environment and the required level of independent judgement.
- A 1:1 list of all **actual** JD mandatory, preferred, required working conditions and critical responsibilities, with short decisive wording and source section. Make a second pass for extra/missing requirements and stale-index conflicts.

Map each substantive criterion to real personal CV/project evidence, labeled `DIRECT`, `SUBSTANTIATED EQUIVALENT`, `TRANSFERABLE`, `WEAK`, `NONE`; distinguish personally performed from team/company results and exposure vs hands-on expertise. Apply two gates **BEFORE any score**:

**Gate A:** all true stated mandatory requirements are MET from direct evidence or legitimate substantiated equivalence. Unknown/ambiguous => manual only; known not met => excluded from verified tracker.

**Gate B:** defining actual technical/domain work and seniority are DIRECT or SUBSTANTIATED EQUIVALENT in depth. Generic cross-industry `R&D/Lean/QA/PM` buzzwords do not prove specialist product/regulated/safety/technical leadership skills. But do not impose a blanket industry exclusion on genuinely transferable PM, equipment, quality or manufacturing improvement roles.

Distinguish ordinary office-tool familiarity from specialized software expertise. If a user has admitted no hands-on experience with a mandated tool, do not infer it from willingness to learn or AI assistance. User-directed application despite a known gap remains possible, but is NOT a verified fit.

**Only after both gates pass:** compute credits `core duties /45`, `required technical /25`, `domain /15`, `seniority /10`, `preferred /5` with evidence multipliers DIRECT 1.00, EQUIVALENT 0.85, TRANSFERABLE 0.50, WEAK 0.20, NONE 0.00. Total /100 is candidate-position fit, **not hiring probability**. Threshold 73% by default. Never score a consequential unverified gate as if it passed.

### Phase 4 — three lanes and authorized tracker transaction

- **A VERIFIED:** exact current job + necessary eligibility + both gates passed + threshold met. Read existing `Job Matches` first; add/update exactly one row A:J; Fit % must be **numeric** (e.g., `.82` formatted as 82%), not a text string. Columns: Date found; Company; Position; Job URL; Company job URL; Employer website; Fit %; Strongest matching experience; Gaps; Eligibility concerns. Short source-linked explanation. Verify write/readback and preserve formatting, formulas and filters.
- **B MANUAL:** plausible but consequential JD/eligibility/core-specialism/status remains unresolved. No qualifying score and **no verified Sheet row**. Present a short chat shortlist with exact source and **one focused question/verification action each**. Do not ask questions already answered in candidate records.
- **C EXCLUDED / DUPLICATE:** clear mismatch, established unmet requirement, below-threshold valid score, closed or previously processed. Do not add. Report succinct counts, not long irrelevant lists.

**Correction transaction:** If new evidence reclassifies a prior verified A job to B or C, locate its actual row by stable job ID/company/title/URL, **remove the complete row** from verified `Job Matches` (not only the score), preserve decision history in a separate private audit, and read back to verify zero qualified rows remain. Do not blindly delete unrelated historical records. On any failed sheet write, report `NOT WRITTEN` truthfully.

### Phase 5 — visible daily report (required even with zero jobs)

In the task's visible result, give:

1. **Source/access status:** authoritative CV/projects read? Gmail account/query sources accessible? Sheet accessible/writable? Run time and lookback.
2. **Processing counts:** messages searched and relevant by category; company-only leads; individual jobs extracted; exact complete current JDs verified; duplicate IDs; A/B/C counts; unresolved statuses.
3. **Verified A rows:** company/title, true score (with 5 dimension credits if requested), direct job link, strongest supported personal evidence, row `ADDED/UPDATED/ALREADY PRESENT/NOT WRITTEN`, and genuine limitations.
4. **Targeted manual B:** only high-value cases, grounded job link, what matches, decisive blocker, one clear question or next verification action. User-accepted gaps should not generate repeated questions.
5. **C/excluded and blockers:** concise reasons/counts, any stale source conflicts, salary/jurisdiction concerns and **explicit zero** if no qualifying new jobs.
6. **Task/system state:** report actual current state when inspectable; do not infer enabled status from historic instructions. Do not pretend GitHub prompt edits alter the active Scheduled task.

**Never do these without separate authorization:** send/forward/archive Gmail, contact employers, submit job applications, auto-edit CV/cover letters, reveal private source details publicly, alter task schedule, change eligibility responses or create duplicate tasks.
