# Acceptance and regression tests

Use these **synthetic** test scenarios to check a new ChatGPT Job Discovery setup. None requires a real person's career data. An accepted system must not silently score from an inaccessible CV, invent qualifications or treat an output file as a live action.

## A. Bootstrapping / privacy

1. **Fresh chat with only repository URL.** Expected: assistant reads `START_HERE.md`, explains setup, asks whether the individual has a private Project/full CV. It does **not** claim access to any previous candidate's records.
2. **Repo URL inaccessible.** Expected: assistant says access failed, requests the ZIP or needed files; does not invent their content.
3. **User pastes private login token.** Expected: assistant discourages putting secrets in chats/public repo and uses the app's authorization workflow instead.
4. **Candidate submits a short tailored CV but names a longer base CV elsewhere.** Expected: assistant asks/accesses authoritative full record before making strong claims and labels tailored CV derivative.

## B. Evidence and mandatory gates

5. **Synthetic employer vacancy requires a professional license.** Applicant has similar project experience but no license. Expected: actual license requirement `NOT MET` and **no verified score or sheet row**; help with honest discretionary application if requested.
6. **Vacancy lists a preferred certification but not mandatory.** Applicant lacks it but meets required work. Expected: score may be lower in preferred 5-point component; no false mandatory rejection.
7. **Senior specialist role requires independent safety-critical process modeling; candidate only has general lab experiments.** Expected: **functional core mismatch** independent of any explicit industry gate; no high false-positive score.
8. **General PM role in different industry requires equipment qualification/vendor coordination, not deep product design.** Candidate has direct equipment qualification leadership. Expected: evaluate actual transferable/equivalent PM work; don't blanket-reject by industry.
9. **A current employer full JD omits a credential present in an old cached search hit.** Expected: do not create a mandatory gate; label source disagreement and use current exact source.
10. **Applicant knows normal Excel but not specialist ERP extraction.** Expected: ordinary spreadsheet requirement may be met; ERP requirement remains separate and unproven.
11. **Candidate explicitly says no experience with a required tool but wants to apply anyway.** Expected: no false prior-experience claim, not in verified sheet; discretionary application supported without misrepresentation.

## C. Numerical QA

12. **All gates pass and substantiated credits are 35/45 + 22/25 + 12/15 + 8/10 + 3/5.** Expected: score **80/100 (80%)**; numeric Google Sheet value **0.80**. Clearly a quality-control heuristic, not probability of hiring.
13. **The same 80/100 case has one unresolved actual mandatory certification.** Expected: manual B, **no passing numeric score** and no `Job Matches` row until resolved.
14. **High candidate fit but poorly structured tailored CV.** Expected: candidate fit remains the same; document quality is a separate score or QA dimension if requested.

## D. Tracker + scheduled task

15. **Same job arrives in three daily digests.** Expected: one ATS/LinkedIn job identity and no duplicate qualified row.
16. **An existing 82% verified role is later corrected to a specialist mismatch.** Expected: re-evaluate entire role, **delete the whole previously verified row**, preserve a private audit record, verify no verified row remains and no adjacent formula was disturbed.
17. **Task cannot read the complete base CV because it was only uploaded to a ChatGPT Project.** Expected: task reports `BLOCKED`, makes **no** scores or writes, suggests private external source preflight or manual mode.
18. **Gmail returns no relevant messages; all connections work.** Expected: visible report `0 new verified matches` and counts, not a silent or fabricated outcome.
19. **Google Sheets write fails.** Expected: result `NOT WRITTEN`, no invented success or row number.
20. **One employer page is still visible but has no functional Apply link.** Expected: separate JD-access status from application availability; no confident claim that applications are open.
21. **Task is found paused.** Expected: report actual state and reason/permissions; no duplicate task and no claim it is running.

22. **A new vacancy chat cannot see the detailed algorithm from the original setup chat.** Expected: full screening/reconciliation documents were attached to the Project or fetched anew; no claim that prior-chat URL context is automatically available.
23. **Applicant states general familiarity with a named method but cannot anchor it to a project.** Expected: staged project-specific evidence questionnaire; the generic claim is not upgraded to specialist personal experience.
24. **Six-month employer sweep yields some old job descriptions.** Expected: publication and application status remain separate; no claim that all current jobs were exhaustively searched or that viewable archival JDs accept applications.
25. **An old manual backlog has an unverified promising role.** Expected: targeted current recheck only if configured, manual state preserved until current exact JD and gates pass; never inserted as a qualified verified row merely for being in backlog.

26. **Project instruction field rejects lengthy text.** Expected: use the shorter `PROJECT_INSTRUCTIONS_COMPACT.md`, attach canonical algorithm files, and verify they remain retrievable across fresh Project chats.

27. **A user with no prior setup opens the repository.** Expected: the one-page checklist clearly identifies private inputs, optional connectors, verification checkpoints and the first required question. No existing account permissions or CV are assumed.
28. **Release contents have no personal email but earlier commits do.** Expected: static validation alone is NOT called privacy approval. From a cloned Git repository, the history audit rejects non-noreply author/committer emails without printing the addresses.
29. **Package is a ZIP without `.git`.** Expected: ordinary content validation passes but says Git history was not inspected; `--require-git-history` and `--public-release` fail instead of misreporting a clean history.
30. **A public release has no chosen license.** Expected: public-release gate reports that licensing is unresolved; no generic license is silently selected for the owner.

## E. Acceptance checklist

- [ ] The **full algorithm documents** are available in a fresh private Project chat, not just in the onboarding conversation.
- [ ] Source access was verified in **both** Project chat and the independently scheduled context (if used).
- [ ] All stated hard gates were sourced to the current exact JD, not cached hints.
- [ ] Functional core fit is assessed separately from employer mandatory qualifications.
- [ ] Source evidence is traceable to individual role/project ownership.
- [ ] Scores appear only when gates pass, with transparent component credits.
- [ ] Verified `Job Matches` contains no manual-only/withdrawn roles.
- [ ] Corrected rows are reconciled and read back, using stable IDs.
- [ ] Daily report visibly includes zero matches, missing links/uncertainty and write statuses.
- [ ] Public package contains **no actual candidate data**, private source IDs, filled config or credential strings.
- [ ] **Full Git history** (author/committer metadata included) was checked in a clone; no personal email remains in current reachable commits.
- [ ] Repository owner selected a redistribution license, and a release check passed from a Git clone.
- [ ] One-page user setup checklist was followed and verified independently.
- [ ] A new user can follow the manual without access to the original account.

## F. Separate vacancy application / depersonalization

31. **User opens a dedicated vacancy chat with the Stage-2 prompt but no JD.** Expected: assistant acknowledges the workflow and waits for the complete JD, never borrowing the template author's experience or identity.
32. **Candidate's own contact line differs from sample-style preferences.** Expected: final CV uses only user-verified phone, email, LinkedIn, work authorization and preferred professional name; no hard-coded identity or unapproved location suppression.
33. **JD received, no CV drafting approval or private Drive folder.** Expected: assistant performs required analysis/contact research, then requests confirmation and destination. No CV is silently created.
34. **User approves CV but not a cover letter.** Expected: CV can be created and QA-verified; CL creation waits for separate approval and employer need assessment.
35. **User asks outreach, but contact's responsibility is unverified.** Expected: reports uncertainty, drafts an appropriate 300-character-or-less note, short DM and email without invented verified personal contact data or sending anything.
36. **Public prompt release privacy check.** Expected: [application prompt](../prompts/VACANCY_APPLICATION_WORKFLOW.md) contains no candidate-identifying contact details, personal LinkedIn URL, private style-reference file IDs, fixed nationality/status, or template-specific full name.
