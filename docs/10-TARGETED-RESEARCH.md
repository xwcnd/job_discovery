# Employer research and ad-hoc market sweeps (beyond LinkedIn email)

The daily Gmail pipeline is a **lead collection channel**, not the complete job market. Users may request one-off research for specific employers, industries, role families, regions or a historic date range. These searches are useful but must follow exactly the same evidentiary standards as inbox-origin jobs.

## Scope and search plan

Before searching, establish the user's target role families, permitted locations and work authorization, chosen employers or sectors, and desired publication window (if any). Do **not** silently constrain the search to the candidate's most obvious job titles when adjacent genuinely transferable operations, quality, program, R&D or advisory work is within scope. Do not stretch generic titles into specialist domains either.

Search the employer's **current exact careers listings** and authorized ATS pages; use job boards or LinkedIn as supplementary discovery and provenance. If using a user-connected browser, state exactly which search-result pages were inspected. If searching a six-month historical window, distinguish **currently open roles** from postings found only in dated archives. A search may be broad, but never claim exhaustive coverage without a complete and verified source inventory.

## Exact-vacancy investigation

For each potential role:

1. Identify the actual employer/hiring unit and the exact current requisition ID, title, country/location and job-specific URL; preserve any LinkedIn original ID separately.
2. Check full current JD source quality (`LIVE-RENDERED`, `CURRENT FULL USER-SUPPLIED`, `CURRENT ATS API`, `SEARCH-INDEXED`, `THIRD-PARTY`). Search snippets and syndicated copies can be stale.
3. Check application state separately. **For older ads (e.g. 60+ days)**, seek both the employer's requisition/portal evidence and current reputable alternative postings. A viewable JD is not necessarily a working Apply link; a third-party 'expired' mark alone is not proof of closure.
4. Screen company, department, actual systems/processes, 2–4 defining duties, true mandatory and preferred clauses, legal conditions and specialist depth using [SCREENING.md](../algorithm/SCREENING.md).
5. Map those clauses to the user's real current primary career record, assign A/B/C according to [DECISIONS-AND-RECONCILIATION.md](../algorithm/DECISIONS-AND-RECONCILIATION.md), and compute the weighted fit only after both gates pass.
6. Read the existing private tracker and audit before any authorized A write; use IDs rather than old row numbers, and verify readback. Report source conflicts and unavailable links explicitly.

## Historical/manual-review backlog (optional)

The original operating model periodically revisited a few unresolved leads rather than endlessly reprocessing everything. A new user may keep a **private** manual backlog using [Manual_Review_Backlog.csv](../templates/Manual_Review_Backlog.csv), or private notes, without adding manual roles to the verified `Job Matches` tab. It can include employer, title, stable job ID/URL, reason unresolved, exact next check and last verified date. A scheduled run may review **2–4 high-value unresolved cases** after new alerts if this is configured and resources permit. Avoid stale row pointers and rechecking a confirmed `NOT MET` question without new information.

A private backlog is not proof of suitability. The user can prioritize a role and choose to apply despite documented gaps, but that choice never converts an unmet mandatory qualification into a verified match.

Use [TARGETED_SEARCH.md](../prompts/TARGETED_SEARCH.md) for an on-demand sweep.
