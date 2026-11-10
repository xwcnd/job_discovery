# Privacy-first release and Git history repair

This guide is for the **maintainer publishing the reusable template**, not for job seekers installing their own private workflow.

## Why checking Markdown files is not enough

A GitHub commit includes author and committer names/emails even if no file contains an email address. GitHub web/profile email privacy settings protect **future** web commits but do **not** retroactively rewrite prior commit metadata. Public issues, pull requests, attachments, forks, comments and cached commit URLs may also disclose information.

The repository owner and username remain visible when the repository becomes public; an email-privacy change is **not anonymity**.

## Recommended safe release gate

1. Keep the repository **private** until this checklist passes. Do not invite friends until you are comfortable that commit metadata is visible to collaborators.
2. In GitHub **Settings > Emails**, select **Keep my email addresses private**. Prefer GitHub's provided `noreply` email for future command-line operations as well; optionally enable blocking command-line pushes that expose personal email.
3. Review all repository files, Git commit author/committer information, tags, branches, issues, pull requests, linked URLs and attachments. Never publish the filled personal configuration or career materials.
4. Before publishing, run `python3 -m unittest discover -s tests -p "test_*.py"` and, from a full local **Git clone**, `python3 scripts/validate_package.py --require-git-history`. It fails on ordinary personal author/committer emails and obvious file-level identifiers. A ZIP has no history and cannot pass this release check. For a public-ready check, use `--public-release`, which also requires a chosen `LICENSE` file.
5. If old commits reveal personal email, choose between keeping the repository private, creating a **new clean repository**, or a deliberate history rewrite (below). Changing GitHub settings alone is insufficient.
6. Select a redistribution license **yourself** (or deliberately keep the repository private/unlicensed). The template does not choose licensing rights for you.
7. Test from a separate account/chat with no access to the maintainer's private documents; then decide whether to publish or grant selected collaborators access.

## Controlled rewrite for a small, owner-only repository (manual)

Rewriting changes commit IDs and can disrupt clones, pull requests, branch protection and collaborator work. **Do not run these commands blindly.** First confirm the repository has no unmerged work, no shared clones to preserve, and that you own it; make a backup. If collaborators have already cloned it, coordinate with them. If you want zero history-risk, create a new private repository and import only the sanitized working tree with a privacy-safe first commit.

Once you have enabled GitHub email privacy and located your account's GitHub-provided `noreply` email in [email settings](https://github.com/settings/emails), an owner who deliberately chooses a fresh orphan history can, on their own computer, use this illustrative approach:

```bash
git clone https://github.com/OWNER/REPO.git
cd REPO
git fetch --all --tags
git status --short
# Confirm the working tree is clean and the current branch is up to date.
git switch --orphan clean-release
git add -A
GIT_AUTHOR_NAME="Project Maintainer" \
GIT_AUTHOR_EMAIL="YOUR_GITHUB_NOREPLY_EMAIL" \
GIT_COMMITTER_NAME="Project Maintainer" \
GIT_COMMITTER_EMAIL="YOUR_GITHUB_NOREPLY_EMAIL" \
git commit -m "Initial privacy-safe Job Discovery release"
# Stop here and inspect: git log -1 --format=fuller; git status --short
# Only after deliberate review, coordinate a force-with-lease update:
# git push --force-with-lease origin HEAD:main
```

The final force-push line is **commented out intentionally**. Do not execute it until you approve replacing the history and verify the target branch and repository. Even after a rewrite, old commit objects or cached links may remain accessible by exact SHA; GitHub explicitly warns that rewriting is not guaranteed erasure. Consider GitHub Support for qualifying sensitive-data exposure and do not claim complete deletion.

## Check what a release actually proves

- **Static validation:** Markdown paths, sample config, spreadsheet schema and likely file-level personal identifiers.
- **History validation:** author and committer **emails** in Git commits *reachable from locally fetched refs*. **Display names must also be reviewed manually**, because an email-only checker cannot determine whether a name identifies someone. This is not a full GitHub-hosted cache, fork, issue or screenshot scan.
- **Onboarding validation:** a separate-user trial, independently verifying connector access and the first real job assessment.
- **Operational validation:** a real Gmail/Sheets read/write cycle and, if enabled, a scheduled task with verified independent CV access.

Do not label the project *public-ready* until the relevant checks pass. A release can be fully usable **privately** while Git-history or licensing steps remain unresolved.

## Official references

- [GitHub: setting your commit email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)
- [GitHub: commit email and existing history](https://docs.github.com/en/account-and-profile/concepts/email-addresses)
- [GitHub: removing sensitive data and history-rewrite limitations](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
