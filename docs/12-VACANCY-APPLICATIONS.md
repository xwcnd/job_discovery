# Using the one-vacancy CV / cover-letter workflow

This is **Stage 2** of Job Discovery. Stage 1 (alerts, vacancy verification, evidence-based fit screening and the verified Google Sheets tracker) can run on demand or through an authorized monitoring task. Stage 2 prepares an application for **one vacancy per private ChatGPT Project chat**, after the person chooses which job to pursue.

## Human instructions — what to provide

1. **Have a private ChatGPT Project** configured from [START_HERE.md](../START_HERE.md). Its source materials should include the complete **factual/base CV** (not just a shortened tailored resume), a **detailed project portfolio** where available, and other genuine career/education/certification records. Do not put these in the shared repository.
2. **Choose one job** from the verified tracker, manual-review queue or your own research. Have the **complete current job description**, preferably with an employer/ATS link, requisition ID, location, salary and closing or application status. A discovery score does not prove all application details have been verified.
3. **Open a new chat inside that Project specifically for this vacancy.** Paste the complete [ONE-VACANCY APPLICATION WORKFLOW prompt](../prompts/VACANCY_APPLICATION_WORKFLOW.md) as the first message. The assistant should acknowledge it and ask for the JD, not immediately invent a tailored CV.
4. **Send the full job description next.** ChatGPT analyses mandatory and preferred requirements, maps evidence to your private sources, reports genuine gaps, and researches 1–3 relevant employer contacts and public professional email options where accessible. Contact research **does not** authorize any outreach.
5. **Confirm before drafting the CV.** The prompt explicitly pauses for your approval and asks for the destination **private Google Drive folder URL** if you are using native Google Docs. If Google Docs are unavailable or you prefer another output, agree on a supported alternative. Do not invent a folder or claim a Google Doc was created.
6. **Review the final CV and decide whether a cover letter is needed.** The prompt contains a second explicit confirmation before the cover-letter stage; it must not be skipped. When requested, ChatGPT produces a letter complementary to the CV and verifies the finished native document where supported.
7. **Continue in that same vacancy chat** for Workday/ATS field checks, questionnaires, recruiter correspondence and LinkedIn connection note / DM / email drafting. **Sending messages, submitting forms and applying require separate explicit authorization.**

## Private configuration the user may need

| Information | Required? | Where it belongs |
|---|---|---|
| Complete factual CV and detailed projects | CV required; projects strongly recommended | Private ChatGPT Project / private Drive |
| Exact vacancy JD and source link | Required for reliable analysis | This vacancy's private chat |
| Professional full name, preferred email, phone and LinkedIn | Only fields actually used must be verified | Private CV / user profile |
| Work authorization, travel, language, location and relocation | When the vacancy calls for them | Private CV/configuration; verify current status |
| Preferred short sign-off / signature and visual style | Optional | Private Project instructions or user answer |
| Writable Google Drive folder | Required only for the native-Google-Docs delivery route | Private vacancy chat after user approval |
| Current application status and any referral/contact relationship | When relevant to application or outreach | Private vacancy chat |

## Assistant instructions — workflow boundaries

- Read the [full application prompt](../prompts/VACANCY_APPLICATION_WORKFLOW.md) and complete private Project source hierarchy. Do **not** use the repo's example data as the candidate's real experience.
- Treat a job-discovery score as a screening heuristic; never improve candidate-position fit through document wording. Check the exact JD again when new evidence or posting changes matter.
- The two explicit **approval gates** (CV preparation and cover-letter creation) override generic advice to continue automatically. Ask for a private Drive folder only when the selected output path actually needs it.
- Keep generated application files, contact data, interview preparation, outreach drafts and any referral information in the private candidate workspace, never in this repository.
- If a job has a known mandatory gap but the person chooses to apply, help them apply **truthfully**. Do not silently reclassify it as a verified match.
- Inspect ATS/autofill details and application answers for contradictions. Research public professional contacts without inventing responsibility or email deliverability; do not send or submit anything without a new explicit instruction.
- Review the resulting deliverables for personal-data accuracy **against the user's private facts**; the public template deliberately contains no prefilled phone, email, work-authorization status, signature name or external CV style-reference link.

## Quick acceptance test

Start a new Project chat with just the linked application prompt. The assistant should recognize it as a one-position workflow, ask for the JD, not insert someone else's identity, and not create a CV before confirmation. When the JD arrives, it should trace claims to the new candidate's sources. A completed run should produce only verified final deliverables and clearly disclose any unverified source, contact, layout or connector step.

If you have **not** finished Stage 1, start with [the one-page setup checklist](QUICK_SETUP_CHECKLIST.md). This Stage 2 workflow is optional and does not change the daily monitoring schedule.
