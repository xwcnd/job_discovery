# Optional daily monitoring with ChatGPT Scheduled tasks

## This is a staged feature, not automatic activation

Merely sharing a repository URL, connecting Gmail or adding a Project instruction **does not create a scheduled task**. The user must have an eligible task capability and authorize the app connections and any external writes. ChatGPT Scheduled tasks may vary by plan/workspace and are visible in **Scheduled** when available. See [official documentation](../sources/REFERENCE_URLS.md).

## Critical separation: Project conversation vs unattended task

**Project chats** can read the full CV, project portfolio and other files uploaded to the Project. **Scheduled tasks created in a Project cannot access files uploaded to / stored in that Project** according to current OpenAI documentation. Therefore:

- Store the authoritative base CV and project portfolio in a **private connected Google Drive** (or another source that you actually verify the scheduled task can independently read). Use exact private file IDs/links **only within the user's private task configuration**, never in a public repo.
- If a task cannot access the same complete source as the on-demand Project chat, choose **manual/on-demand screening** or a minimal source scope that the user explicitly approves; **never** substitute old derived summaries or memory while claiming full evidence-based scoring.
- Do a standalone task **source-access preflight**: read the base CV, a specified project detail, the live tracker, and at least one actual LinkedIn alert in a trial scheduled run. Report which objects are actually accessible. Missing any required source => don't score or write to verified matches.
- Check both **read and write** permissions separately. A task that can read Gmail may not be able to update Sheets; maintain a chat-only report if the tracker write fails, with an explicit **not written** status.

## Activation procedure

1. Complete [Project setup](01-CHATGPT-SETUP.md), [career evidence](02-CAREER-EVIDENCE.md), [alerts](03-LINKEDIN-GMAIL.md), and [tracker](04-GOOGLE-SHEETS.md).
2. Test the pipeline on demand with the exact current JD. Confirm dual gates, three-lane classification, dedupe and full-row correction policy.
3. Copy [prompts/DAILY_MONITOR.md](../prompts/DAILY_MONITOR.md) **to a new private Scheduled task**. Replace private placeholders only inside that task, not in public documents.
4. Choose the requested time and **time zone**. A daily fixed time is a user choice; the sample does not prescribe one. If eligible, a Gmail event-triggered Work task might be an alternative but should be created and tested separately, not alongside a duplicate daily task.
5. Verify the task's **title, enabled status, recurrence, time zone, prompts, connection permissions and next expected run** in Scheduled. Do not infer enabled status from an old chat.
6. Run a first manual test or available `run now` capability. Confirm source readback and that every verified write appears once in the private sheet.
7. Report: alerts processed, distinct jobs, exact current descriptions verified, A added/updated, B manual, C excluded/duplicates, source-access failures and real task status.

## Rolling scan and idempotency

If the user has **explicitly configured** a private unresolved/historical-review backlog, an optional additional action is to revisit **2–4 priority unresolved roles after the new inbox scan** using fresh exact vacancy and source evidence; record whether they remain current. No backlog configured => skip this step. This must not convert historical manual entries into verified matches without both gates and an active exact JD. See [targeted research](10-TARGETED-RESEARCH.md).


Use a **configurable 7-day lookback** to cover skipped days; read full alerts; deduplicate by email message ID and vacancy IDs, consult previous tracker and private audit. Do not blindly skip a role simply because its company was seen before: title and requisition identity matter. Do not write the same job twice if a repeated digest arrives. A later reclassification must reconcile the exact original verified row.

## Monitor failure modes

- **CV inaccessible in task:** report `BLOCKED: AUTHORITATIVE CANDIDATE SOURCE NOT AVAILABLE`; no fit scores and no writes.
- **Job full JD inaccessible:** treat specific role as manual/unverified; do not infer a mandatory qualification from fragments.
- **Gmail disconnected/no messages:** report source status, and distinguish zero relevant messages from connector failure.
- **Sheet not writable:** report what would qualify but state `NOT WRITTEN`; do not claim tracker updated.
- **Task paused/disabled:** check Scheduled, app authorization and any required approval; do not create a duplicate task as a workaround.
- **Task completes silently:** inspect previous runs and ensure instructions explicitly demand a concise visible results summary, even when there are zero matches.
- **Task prompts out of date:** edit the actual saved task. Updating a GitHub file or Project instruction does not update an existing scheduled task.

## Privacy and cost

A task accessing email and private career documents touches sensitive personal information. Connect only the needed account, review external writes, audit the recurring schedule and disable when no longer useful. Multiple scheduled runs may count toward account limits/usage; review current OpenAI guidance.
