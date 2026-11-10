# Job Discovery installation manual — for new users

This manual explains **what you need to provide, where to put it and how to verify each part**. For a shorter walkthrough, use the [one-page setup checklist](docs/QUICK_SETUP_CHECKLIST.md). No coding is required for the normal ChatGPT workflow.

## Before you begin

You need a ChatGPT account and your career information. LinkedIn alerts, Gmail and Google Sheets make the workflow more automatic, but you can start with manually pasted job links. You do **not** need to share this public GitHub repository's owner's Project or account.

### Stage 1 — Start with the repository in ChatGPT

Open ChatGPT and paste the repository link together with the message in [prompts/STARTER_PROMPT.md](prompts/STARTER_PROMPT.md). Ask ChatGPT to read [START_HERE.md](START_HERE.md) before recommending settings. If ChatGPT cannot access GitHub, upload the package ZIP to the chat and ask it to start from `START_HERE.md`. Check that it mentions the dual screening gates and separate verified/manual output; if not, ask it to verify it read the files.

### Stage 2 — Make your **private** ChatGPT Project

In the sidebar, choose **New project**, name it for your own use and keep it private. In **Project settings**, paste the content of [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md); if the field rejects the length, paste [PROJECT_INSTRUCTIONS_COMPACT.md](PROJECT_INSTRUCTIONS_COMPACT.md) instead. **Add the full [screening algorithm](algorithm/SCREENING.md), [decision/reconciliation rules](algorithm/DECISIONS-AND-RECONCILIATION.md) and [failure calibration cases](algorithm/FAILURE-PATTERNS.md) as separate source files to your private Project.** They must remain available to every new vacancy chat; a one-time link in a previous chat is not enough. If your plan cannot store the files, verify a reliable connected or retrievable equivalent and do not claim persistence otherwise. No personal CV should ever go into the public Job Discovery GitHub repo.

### Stage 3 — Upload personal career evidence to **that Project**

| Information | What is useful | Where it belongs |
|---|---|---|
| Complete/base CV | All employment, titles/dates, projects, education, substantive technical skills and factual results, not only a 1–2-page application resume | Private Project; optionally private Drive for scheduled access |
| Detailed projects | Personal actions, role, technical object, stakeholders, tools, tests, individual vs team outcomes and sources | Private Project; optionally private Drive |
| Education/certificates | Exact degree/discipline and confirmed certificates, when relevant | Private Project or stated facts |
| Work preferences | Target roles/industries, locations, remote/relocation, exclusions, travel, target salary and currency | Private config / chat |
| Eligibility | **Country-specific** work authorization, language level, required licenses; mark uncertain cases unknown | Private config / chat; identity-document numbers unnecessary |
| Historical corrections | Known gaps, corrected employer dates, what a project method actually involved | Private source manifest / chat |
| Jobs to review | Exact vacancy URL or full job description | A dedicated job/application chat within the Project |

Use [the private source manifest template](templates/PRIVATE_SOURCE_MANIFEST.example.md) to declare which document is the authoritative full/base CV. Tailored CVs and generated cover letters do **not** replace that source.

### Stage 4 — Set preferences with ChatGPT

Ask it to build your personal configuration from the topics in [templates/USER_CONFIGURATION.example.yaml](templates/USER_CONFIGURATION.example.yaml). You need not edit YAML yourself; ChatGPT can ask for answers conversationally and keep the result private. For example, specify countries, all acceptable cities, preferred roles and salary benchmark. Allow `UNKNOWN` rather than guessing any legal permission or professional qualification. Keep any filled config out of GitHub.

If important skills are missing from the written CV, use the optional [project-by-project evidence questionnaire](docs/09-EVIDENCE-ENRICHMENT.md) to establish the **actual** experience, not guessed qualifications.

### Stage 5 — Set up LinkedIn email alerts

On LinkedIn Jobs, create a few searches matching your role families and locations. Turn on job alerts; choose **daily email** delivery. Review your account's current alert limit and filter settings. Wait for and verify one genuine alert in your own mailbox. Details: [LinkedIn and Gmail guide](docs/03-LINKEDIN-GMAIL.md).

### Stage 6 — Link your own Gmail

If ChatGPT provides a Gmail connector, connect **your** account through the app controls and approve the needed read scope. Ask ChatGPT to inspect your actual LinkedIn sender pattern rather than importing someone else's sender assumptions. The basic method searches a seven-day rolling window, reads every job from each alert, and prevents repeats by message/job IDs. You can paste links manually instead if the connector is unavailable.

### Stage 7 — Create your own private tracker

In Google Sheets create a sheet named `Job Discovery — My Matches`, worksheet `Job Matches`, and import [the ten-column CSV header](templates/Job_Matches.csv). Set `Fit %` column G to numeric percentage. Do **not** publicly share the sheet. If a Sheets connector is available, verify the exact account, file, worksheet and write/readback authorization. Only fully verified eligible matches belong here. See [Sheets guide](docs/04-GOOGLE-SHEETS.md).

### Stage 8 — Test screening on real jobs

Paste [the on-demand assessment prompt](prompts/ON_DEMAND_ASSESSMENT.md) with a real current vacancy. Check that ChatGPT reads the exact complete job description, compares personal evidence, applies **actual mandatory gate** and **core role/function gate** separately, and gives a score only if both are met. Unresolved prospects should remain in chat with a targeted verification question. Check how a previously scored job would be removed if later disqualified.

For searches beyond alerts (specific companies, sectors, date windows, ad-hoc LinkedIn results), follow [targeted market research](docs/10-TARGETED-RESEARCH.md). Keep unresolved cases in chat or an **optional private manual backlog**, not the verified Sheet.

### Stage 9 — Optional daily monitoring

Only when the above works and your ChatGPT account supports Scheduled tasks, use [the daily prompt](prompts/DAILY_MONITOR.md). Replace all source-link placeholders **privately**. Crucially: **scheduled tasks may not access files uploaded to ChatGPT Projects**. First confirm that the scheduled task can access the authoritative full CV and project portfolio through another authorized source (for example, a connected private Google Drive file). If not, use manual/on-demand screening. Verify the created task's actual enabled state and run result; no GitHub link or copied prompt automatically activates one.

### Stage 10 — Maintain the setup

New career facts, changed preferences or user feedback must update the **private controlling source**, live tracker and saved task prompt where applicable. A corrected job that no longer qualifies must disappear **entirely** from the verified sheet, with its reason retained separately in private audit notes. Reassess after actual changes and avoid duplicates. Consult [maintenance guide](docs/08-MAINTENANCE.md).

## Final setup checklist

- [ ] My own private ChatGPT Project exists and contains the project instructions **and the full algorithm source files**, confirmed accessible in a new chat.
- [ ] ChatGPT can read my current complete/base CV and project evidence, not just a short tailored version.
- [ ] My location, travel, salary and country-specific authorization preferences are current.
- [ ] My LinkedIn alerts send genuine job emails to my mailbox (or I use a manual alternative).
- [ ] Gmail sender/query patterns were verified against my own received alerts.
- [ ] My private Google Sheet has the standard ten columns and numeric percent format.
- [ ] At least one real job was screened with the current complete JD and both gates.
- [ ] Verified vs manual vs excluded roles are kept separate.
- [ ] If a scheduled task exists, I checked its own access to full career sources, permissions, schedule, enabled state and first run.
- [ ] I know how to report a false positive and request correction to the actual tracker, not merely the score text.

**Expected result:** one private job-search system controlled by you, using a reusable public methodology, with a truthful distinction between demonstrated fit and promising opportunities still requiring verification.
