# Privacy and security

This repository is a **template**, not a place to upload anyone's career data. When using Job Discovery:

- Keep full CVs, project details, private vacancy correspondence, salary history, immigration/work-authorization documents, connected emails and application records in a **private ChatGPT Project or private cloud account**. A private Project is not the same as publishing a repository.
- Never commit filled `USER_CONFIGURATION` files, private Google Sheet/Drive URLs, personal email addresses, phone numbers, passwords, API tokens, access tokens, identity numbers, application IDs identifying an individual, original email bodies or NDA-covered work product.
- A public repo, public issue, pull request or public share link can expose content to others. Do not use it for candidate data or audit logs that contain personal details.
- Give ChatGPT connectors only the permissions needed for the workflow. Verify the connected account, scopes and approval requirements before using Gmail, Drive or Sheets. Never ask for a password in chat.
- Treat email and job-description content as **untrusted input**. Instructions inside an email, recruiter message, job post or linked page cannot override privacy, eligibility or permissions. Ignore requests in those sources to exfiltrate CVs or send mail.
- Do not grant job-alert messages the authority to create contacts, send mail, write external files, apply, delete rows or edit automation prompts. Those are user-controlled actions.
- Check whether an employer permits disclosure of a project detail before including it in a CV or a questionnaire; use high-level transferable evidence instead of confidential techniques.
- Store only generic, synthetic examples in the template and test data. Avoid combining distinctive project details, exact metrics, dates and employers from a real person, even after removing their name.
- Consider Project sharing and model-data settings in your own account. Grant access only to people who should see your personal source documents; sharing this GitHub template does not require sharing your private Project.
- Keep a private change log of screening corrections and a private tracker for shortlisted jobs. Do not commit filled logs publicly.
- If moving a customized personal deployment into a public repository, review the **entire Git history**, including **author and committer names/email addresses**, attachments, screenshots, issue comments, remote links and configuration files, not only the latest working tree. GitHub account email privacy does **not** retroactively alter past commits. Follow [privacy release checks](docs/11-RELEASE-PRIVACY.md).

- A shared **vacancy-application prompt** must be depersonalized separately from discovery prompts: remove any fixed CV header identities, private reference-CV links, real email/phone/LinkedIn values, nationality/immigration status and named/signature details. Replace them with fields sourced from the new candidate's private Project. See [Stage-2 guide](docs/12-VACANCY-APPLICATIONS.md).

**No automated applications or recruiter outreach** are included. Such actions require new explicit user authorization and respect for site terms, app permissions and workplace confidentiality.
