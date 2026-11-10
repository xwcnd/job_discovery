# Job Discovery - one-page setup checklist

**For a new user:** work through these steps with ChatGPT. No coding or public upload of personal records is necessary; a public repository or release ZIP does not require your own GitHub account, while a private repository requires access. The [full installation manual](../INSTALLATION_MANUAL.md) explains each step.

| Step | You provide or do | ChatGPT helps with | Completion test |
|---|---|---|---|
| 1. Open the guide | Share this repository link or its release ZIP in a new chat | Read `START_HERE.md` and explain how the pipeline works | Assistant identifies **both** mandatory and core-function fit gates |
| 2. Create private Project | Create your own ChatGPT Project | Paste `PROJECT_INSTRUCTIONS.md` (or the compact version) and add the three `algorithm/` Markdown files as Project sources | A second, new Project chat can read the full screening rules |
| 3. Add career evidence | Upload your complete **base CV** (required), detailed project portfolio (strongly recommended), and any relevant factual records | Identify missing project-level evidence; keep tailored CVs subordinate to original records | Assistant can cite what **you personally did**, not just employer/team outcomes |
| 4. Set search criteria | Specify roles, locations, workplace preferences, compensation/currency, travel, languages, and **country-specific work authorization** | Save a private configuration based on `templates/USER_CONFIGURATION.example.yaml` | Unknown answers remain **UNKNOWN**, never invented or turned into disqualifiers |
| 5. Configure job alerts | On LinkedIn Jobs, save appropriate searches and enable email job alerts | Help select searches and check a genuine received email | One authentic alert arrives in your selected mailbox |
| 6. Allow Gmail access (optional) | Connect your own Gmail account if available | Discover actual sender addresses, parse all jobs in a digest, and deduplicate | A read-only test finds correct jobs; if unavailable, manually paste job links |
| 7. Create private tracker | Create a Google Sheet with `Job Matches` and import `templates/Job_Matches.csv` | Confirm 10 columns, percentage format, links and write permissions | A test entry can be written **once**, read back and removed if needed |
| 8. Test 2-3 jobs | Give current job links or complete current job descriptions | Verify the exact JD and employer/team, compare real evidence, apply both gates, then score only if qualified | One complete evidence matrix; verified, manual and rejected cases stay distinct |
| 9. Turn on monitoring (optional) | Choose schedule/time zone and allow connected sources | Configure **one** scheduled task and check its independent access to CV/projects, Gmail and tracker | Actual task state and a real run are verified; no access means no unattended score |
| 10. Maintain the system | Report corrected facts, withdrawn jobs and changing priorities | Reassess and reconcile the live tracker, keeping a private audit | Withdrawn jobs disappear **entirely** from verified matches; no duplicates |

## After discovery — optional application preparation

Once a candidate selects a real vacancy, create a separate private Project chat for **that exact job**, paste [the Stage-2 application prompt](../prompts/VACANCY_APPLICATION_WORKFLOW.md), and then provide the full JD. The [application guide](12-VACANCY-APPLICATIONS.md) lists the needed private sources, optional contact/signature preferences, Google Docs destination and two approval gates. The daily screening automation never automatically applies to a job.

## Keep these private

Full CV and project records, filled configuration, Google Sheet/Drive links, email contents, application details, work authorization documentation, and credentials belong only in your private workspace. **Never put them in this shared repository, issues, or pull requests.**

## Expected behavior

- **Verified job:** current exact JD, all true mandatory gates supported, role-defining work supported, score meets your configured threshold; add to `Job Matches` and read back.
- **Manual review:** promising but consequential evidence, job status or eligibility is uncertain; **no qualifying numeric score** and no verified row; ask one targeted question.
- **Excluded:** a confirmed mismatch, unmet required qualification, duplicate, or expired job; keep a brief private reason, not a false positive.

**Trouble?** Start with [troubleshooting](07-TROUBLESHOOTING.md). [Full onboarding](../START_HERE.md) is ChatGPT's instruction entry point; [installation manual](../INSTALLATION_MANUAL.md) is the detailed human guide. A repository link never connects accounts or activates automation by itself.
