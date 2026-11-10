# Canonical evidence-based job screening algorithm

**Version:** 1.0 — generic, candidate-independent.  
**Scope:** single-vacancy evaluation and batched monitoring, with optional private Google Sheets write.  
**Primary principle:** assess what the person has actually done against what the employer's **current exact job** actually requires. Don't inflate fit to fill a shortlist.

## 0. Required inputs and confidence

- Current explicitly designated **complete factual/base CV** (not a tailored derivative), original project portfolio and any other authorized source records.
- Private user's location, job-family preferences, work authorization by jurisdiction, willingness to relocate/travel, languages, compensation preference, and exclusions. Each may be `UNKNOWN` until confirmed.
- Identified **exact job**, with company, title, location, specific URL and ideally LinkedIn/ATS requisition ID.
- Complete current JD text and verifiable provenance. A search snippet alone is not complete.
- Connection to private tracker only if updates are authorized and supported. If unavailable, produce a report without claiming a write.

If crucial candidate records cannot be accessed at time of assessment, **STOP** before fit scoring. It is unacceptable to fall back silently to a generated CV, an old version or a model's impression from prior chats. Report the missing authoritative input and appropriate next step.

## 1. Establish provenance and job identity

Build a provenance record:

| Field | Notes |
|---|---|
| Employer / legal hiring entity | Distinguish actual employer from staffing agency and parent brand |
| Title / requisition ID | Exact title, original LinkedIn ID and authorized employer ATS ID separately |
| Location and working conditions | Remote, hybrid, travel, clearance, shifts, site work |
| Job-specific source URL | Direct URL for **same** job; retain original lead URL |
| Content provenance | `LIVE-RENDERED`, `CURRENT FULL USER-SUPPLIED`, `CURRENT ATS API`, `SEARCH-INDEXED`, `THIRD-PARTY` |
| Access date / publication date | Don't confuse when checked with when originally posted |
| Exact text coverage | `FULL JD`, `PARTIAL JD`, `SNIPPET ONLY`, unknown |
| Open/apply status | `CONFIRMED ACCEPTING`, `PAGE LIVE / APPLY UNKNOWN`, `CLOSED`, `UNVERIFIED` |
| Corporate homepage | A separately verified official corporate root/homepage |

**Source hierarchy for requirements:** full current user-supplied exact JD > current rendered official employer/authorized ATS page where no conflict > verified official current ATS API > search-indexed employer snippets > third-party mirrors. If there is a conflict between a user-supplied current screenshot and an indexed snippet, inspect the live exact employer page. Do not promote cached qualifications to mandatory. A current fully rendered employer page may supersede an older user copy if the changed version is demonstrable and dated.

**Complete-JD reconciliation:** Enumerate each bullet of the actual qualifications and responsibilities **in order and with the correct heading**. Make a second pass comparing every claimed gate against the same exact current source. Search for missing and extra hard requirements, particularly certifications, degrees, software and years. Quote only the decisive small phrases needed for proof, with source URL and section. Never import a qualification from another vacancy.

**Open/apply distinction:** A visible job description does not necessarily prove that a live application portal accepts submissions. Likewise, a stale aggregator flag cannot alone establish closure. Record uncertainty honestly. A clearly expired/withdrawn specific vacancy cannot be a new verified currently open match. **Default:** when a current complete employer-authored exact posting is substantiated and no credible evidence of closure exists, an untested Apply action does not by itself block otherwise qualifying Lane A; mark `PAGE LIVE / APPLY UNKNOWN` prominently in concerns. When there is **material contradictory evidence** of closure, the exact status or even the current posting is dubious, hold in Lane B until resolved; do not call it confirmed accepting. The user can configure a stricter policy, but must not erase the uncertainty.

## 2. Research the actual job before matching keywords

This is an independent **functional/domain context** check. Determine:

1. **Company:** what products/services/assets it sells, which industries and customers it serves, and actual physical/software processes.
2. **Hiring department or business unit:** the specific team, its mission, equipment/processes, and stakeholder relationships. `UNKNOWN` if the JD/employer materials do not reveal it.
3. **Two to four defining deliverables:** what the employee must accomplish in an ordinary working month, beyond a broad job title.
4. **Technical objects and environment:** the real devices/materials/markets/financial systems/regulations/engineering subsystems/operating scale, site/lab/office/customer environments and safety obligations.
5. **Independence and depth:** what decisions the new hire is expected to make themselves, what specialism is assumed, whom they lead and what evidence of product- or domain-specific competence is necessary.

Avoid synonym traps: `quality`, `innovation`, `R&D`, `project management`, `materials`, `process improvement`, `stakeholder management` and `instrument testing` may mean materially different things across departments and products. A generic lab background does not establish deep specialist competence in another field; equally, an employer's industry should not exclude a role whose defining PM/supplier/QA duties are genuinely transferable without needing prior specialist expertise.

Classify role-defining applicability as:

- **DIRECT:** firsthand work on substantially the same technical system/functions at comparable responsibility.
- **SUBSTANTIATED EQUIVALENT:** demonstrably comparable technical principles/functions, deliverables, scale and decision-making with an explainable transfer path.
- **TRANSFERABLE ONLY:** related practices but not the actual critical systems/functions at the expected specialist depth.
- **UNVERIFIED:** potentially possible, but important depth or technical details lack reliable evidence.
- **MISMATCH:** clearly different core work or seniority cannot be credibly met from current facts.

The classification is separate from formal employer mandatory qualifications. Do not invent a hard requirement simply because the employer works in a particular sector.

## 3. Parse mandatory, preferred and working conditions without invention

Build a one-to-one matrix for **every material JD requirement**:

| Item | Exact phrase + heading | Type | Candidate evidence source | Evidence | Mandatory gate | Context/notes |
|---|---|---|---|---|---|---|
| 1 | exact current JD text | MANDATORY / PREFERRED / CONDITION / DUTY | source + employer/project/period | DIRECT / EQUIVALENT / TRANSFERABLE / WEAK / NONE | MET / UNVERIFIED / NOT MET / N/A | decisive ambiguity |

Inspect education and allowed equivalents, certifications/licenses, years and *depth* of experience, technical platforms, domain practice, seniority, people/project/budget ownership, communication/language, legal work authorization, clearance, mandatory travel/onsite requirements and application-specific work samples. Keep **preferred/asset** requirements separate from employer-mandatory clauses.

For mandatory alternatives, accept only substantiated equivalence the JD actually permits or demonstrably meets. If a stated required certificate is absent, don't fill it with an unrelated award. A Bachelor's degree in a broad `science, engineering or related field` clause may legitimately cover different degrees; analyze its actual wording and intended work before categorically excluding or accepting.

**Gate states:**
- `MET — DIRECT`: clear relevant personal evidence.
- `MET — SUBSTANTIATED EQUIVALENT`: true comparable experience meeting the stated requirement without exaggeration.
- `UNVERIFIED`: source missing, meaning ambiguous, missing exact depth, unresolved jurisdiction/status, or unknown candidate fact; **not a No**.
- `NOT MET`: actual evidence shows lack of required prior experience, license, language or condition. A statement that a user can learn it does not change this state.

**Do not invent employer gates:** Company products alone, preferred fields, outdated web snippets and old application answers are not current mandatory bullets. However, missing role-defining practical competence may independently fail the **functional applicability** gate even if the employer doesn't explicitly call domain experience mandatory.

## 4. Depth-specific safeguards

When the role says `senior`, `technical lead`, `test architect`, `product owner`, `independent specialist`, `full lifecycle`, `most of the following`, `extensive knowledge` or similar, identify the **required breadth and depth** explicitly.

Examples applicable beyond any one domain:

- Using instruments -> building test setups -> automating measurements -> validating repeatable product-test methodology with uncertainty -> **leading domain-specific product reliability** are different stages. Do not skip stages.
- Mechanical/electrical/software system *integration* is different from creating the core engineering design, optimization, tolerance/error budget and design-to-delivery qualification.
- Supplier technical coordination is different from personal full product design or vendor's manufacturing output.
- Managing a particular workstream is not automatically owning an entire program financial plan, approvals or client commercial account.
- General manufacturing improvement is not direct expertise in every industry-specific chemical, regulated, safety-critical, energy, semiconductor or aerospace process.
- Basic Office/Excel/PowerPoint familiarity does **not** prove specialist MS Project, SharePoint administration, SQL, ERP/MES, production analytics or advanced Excel. But general Office knowledge **should** count when genuinely present; don't create gratuitous requalification requirements.
- Formal named methods and equivalent practical activities can both be relevant, but never certify named accreditation or training from an equivalent practice alone.

If a required list says **"most"**, map each component and count meaningful coverage; do not treat one headline keyword as meeting the breadth. If a required portfolio/sample involves specific design calculations or a delivered system, verify the actual firsthand deliverable.

## 5. Two independent qualification gates

**Gate A — Employer's actual mandatory requirements**: Each actual mandatory item must be MET directly or through a clearly allowable and supported equivalent. `UNVERIFIED` => Manual B. `NOT MET` => Exclude C for automatic verified shortlist, though user may still personally choose to apply truthfully.

**Gate B — Role-defining functional applicability**: The real core work must be `DIRECT` or `SUBSTANTIATED EQUIVALENT` at the depth and seniority required, not merely generic transferable overlap. `UNVERIFIED` => Manual B, `TRANSFERABLE ONLY` or `MISMATCH` for specialist core => exclude from automatic shortlist. Domain-agnostic PM/process/QA roles can pass when their actual central duties have genuine supported equivalence.

**No passing numerical score** while either gate is failed or consequentially unresolved. A non-disqualifying preference gap may be scored fractionally if gates pass.

## 6. Transparent weighted fit (after both gates)

Default components, totaling 100:

| Component | Max points | What to evaluate |
|---|---:|---|
| Defining/core responsibilities | 45 | 2–4 actual main deliverables and their activity/depth requirements |
| Required technical competencies | 25 | Required hard and applied skills relevant to exact systems |
| Specific product/domain/process | 15 | Actual role context, not company's broad industry alone |
| Seniority, autonomy, leadership | 10 | Personal scope, independence, delivery ownership, management depth |
| Explicitly preferred qualifications | 5 | Actual assets, not invented fit bonuses |

Inside each component, allocate criterion weights according to significance (not word count) and score using substantiated evidence coefficients:

- `DIRECT` = **1.00**
- `SUBSTANTIATED EQUIVALENT` = **0.85**
- `TRANSFERABLE` = **0.50**
- `WEAK` = **0.20**
- `NONE` = **0.00**

Component credit = sum of (criterion's point allocation × coefficient). Final result = sum of 5 component credits / 100, expressed as percent (e.g. 82% => numeric spreadsheet `0.82`). Record component credits so another person can audit the rationale. The complete absence of preferred qualifications can lower 5 points but is not itself a hard gate.

Default automatic threshold = **73%**, configurable for individual preference **only after transparent documentation**, never as a way to override a missing employer mandatory requirement. A score is a quality-control ranking heuristic, **not a predicted probability of an interview or an offer**. Be wary of implausibly high scores generated from generic category names; rerun role context before accepting them.

A rejected/manual role may have a **private illustrative estimate** only when the user explicitly requests such a counterfactual, labeled **NOT QUALIFIED / NOT FOR TRACKER**. The default operation uses **no qualifying numeric score** for unresolved mandatory or functional gates.

## 7. Source-linked result and presentation

For each job show:

```text
Employer — exact title — location [job-specific source URL]
Exact requisition / LinkedIn ID; date verified; page status; application status
Company, hiring unit, actual technical objects and 2-4 core tasks
Mandatory gate: MET / UNVERIFIED / NOT MET; each decisive bullet and source
Functional applicability: DIRECT / EQUIVALENT / TRANSFERABLE ONLY / UNVERIFIED / MISMATCH
Evidence map: criterion -> factual source and specific personal action
Meaningful gaps: missing direct depth, preferred tools, condition and verification issues
Decision: A verified / B manual / C exclude
If A: category credits (x/45 + x/25 + x/15 + x/10 + x/5 = total/100) and exact tracker write result
If B: one decisive manual check with exact link; no qualifying score
If C: concise reason, no tracker entry
```

Preserve **current vacancy links** for every referenced historical or newly found role. A job title alone is not usable provenance. Don't display stale personal email links, copied confidential content, or internal repository details to external readers.

## 8. Feedback and truthfulness

When the candidate disputes a requirement, source status or score, **inspect their evidence first** and reconcile with current source, rather than defending stale snippets. Distinguish new factual testimony from subjective interest. If the user chooses to pursue a vacancy despite known software or domain gaps, mark `USER-ACCEPTED GAP — MAY APPLY`, assist with honest documents, but leave it outside verified Lane A. Don't ask again about a confirmed missing skill unless circumstances change.

A correction affecting a tracked role must update the **live actual spreadsheet row** (or remove the whole no-longer-qualified row) and private audit log. A change to generic GitHub instructions alone is not a correction to an existing connected workbook or scheduled task.

## 9. Multi-job run order

1. Verify current access to authoritative candidate sources and private configuration.
2. Read configured Gmail sources separately with rolling window; record source failures explicitly.
3. Extract every job link and company-only lead; dedupe by message and vacancy IDs.
4. Verify exact current JD and context for each credible job; no guessing from title.
5. Apply gate A and gate B; separate B uncertainties from C disqualifications.
6. Score qualifying roles, apply threshold, prepare A rows.
7. Read live tracker and audit for duplicates and prior reclassifications.
8. Write authorized new/updated A rows; reconcile deletions if prior A becomes B/C; verify readback.
9. Post short visible report including zero matches and blocked capabilities.
10. Privately record substantive corrections and update actual live automation prompt if screening behavior changed and the user authorized it.

A role can be rejected as irrelevant early if clearly outside target preferences and no employer research is warranted. Never report it as fully JD-screened unless the exact JD was actually read.
