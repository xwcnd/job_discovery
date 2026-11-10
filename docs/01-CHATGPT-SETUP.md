# Set up your private ChatGPT Project

## Prerequisites

A ChatGPT account capable of creating Projects, access to your own career documents, and optionally a LinkedIn account, a Gmail account that receives job alerts, and a Google account for a private tracker. Features, connected-app permissions and scheduled task limits vary by account/workspace.

## Steps

1. **Create the Project.** In the ChatGPT sidebar select **New project**; name it something like `Job Discovery — Personal`, and keep it private. Review the Project memory setting (project-only memory is an option when available), the sharing state, and who can see files.
2. **Install instructions and preserve the algorithm.** In the Project menu (`...`) choose **Project settings** and paste the full text of [PROJECT_INSTRUCTIONS.md](../PROJECT_INSTRUCTIONS.md), or [PROJECT_INSTRUCTIONS_COMPACT.md](../PROJECT_INSTRUCTIONS_COMPACT.md) if the full version does not fit the available field. **Upload [SCREENING.md](../algorithm/SCREENING.md), [DECISIONS-AND-RECONCILIATION.md](../algorithm/DECISIONS-AND-RECONCILIATION.md) and [FAILURE-PATTERNS.md](../algorithm/FAILURE-PATTERNS.md) as persistent Project sources.** If the full instructions exceed product limits, keep the short source hierarchy, dual gates, decision lanes and privacy rules in instructions. Confirm files and instructions are saved. A link once pasted into an earlier conversation is not proof that a new vacancy chat can read all the algorithm detail.
3. **Add primary career sources.** Upload an actual complete/base CV and a detailed project portfolio when available. Add supporting primary records only if permitted to share and useful. Never upload login credentials or confidential client documents.
4. **Create your private preference record.** Start from [USER_CONFIGURATION.example.yaml](../templates/USER_CONFIGURATION.example.yaml) in your private space; fill only the facts you know. Keep dates and work-authorization regions explicit; unknown eligibility stays unknown.
5. **Give ChatGPT a source manifest.** Use [PRIVATE_SOURCE_MANIFEST.example.md](../templates/PRIVATE_SOURCE_MANIFEST.example.md) to identify which file is the controlling base CV and which are project supplements. Make it a private file; do not publish it.
6. **Test the evidence boundary.** Ask: `Which source is my authoritative full CV, what are three direct factual examples from it, and what remains unverified? Do not infer missing details.` Correct any misattribution.
7. **Check a NEW chat within the Project.** Ask the assistant to retrieve a precise rule from each of the three algorithm source documents without relying on remembered summaries. Fix any missing-file access before continuing.
8. **Add a private tracker and alerts** following the next two guides. Use a manual on-demand screening session before considering automation.

## Connect apps only when needed

Review available Gmail and Google Drive / Sheets apps in ChatGPT's plugin/app settings and approve only the necessary account. A connected app is not the same as granting access to every private Drive file or enabling write operations. A candidate may also run the workflow manually by pasting current JDs and keeping their own spreadsheet if no connector is available.

## A crucial scheduled-task limitation

A ChatGPT Project can use uploaded files for Project conversations, but **scheduled tasks created in a Project cannot access uploaded files or files stored there**, according to OpenAI's current Scheduled tasks documentation. Do **not** create a daily run that silently assumes Project file access. Before enabling monitoring, supply an accessible **private connected Google Drive source** or another actually tested permitted source for each run; verify exact readback and candidate-record versions. If this is impossible, use on-demand manual screening and mark unattended screening unsupported.

## First-use check

- Can ChatGPT list the actual names and versions of your source files?
- Does it distinguish your personally performed work from team/company outcomes?
- Can it fetch and cite an exact current job description, without treating third-party snippets as current employer content?
- Does it withhold the verified score for an unknown mandatory requirement?
- Is the tracker private and accessible via your own account?
- Have you verified *all* necessary permissions before creating a scheduled task?

Do not share the personal Project merely to share the workflow. Share the generic repository link instead.
