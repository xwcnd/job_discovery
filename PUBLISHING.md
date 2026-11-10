# Publishing this package to your own GitHub repository

The files in this distribution are sanitized templates. They do **not** include the prior owner's personal records or the private source repository history.

## Use your intended destination

1. Sign in to a GitHub account that has **write permission** to the destination repo.
2. If the repository is new or empty, upload the extracted files preserving the folder layout. If it already contains work, **review and merge** carefully rather than overwriting unrelated files.
3. Review [SECURITY.md](SECURITY.md), every document and **all Git author/committer metadata** for secrets, identifying career stories, resume data and private URLs before making the repository public. Follow [privacy and history repair](docs/11-RELEASE-PRIVACY.md).
4. In the repo's `README.md`, verify that the relative links and `START_HERE.md` entrypoint work after upload.
5. Test onboarding with the [one-page setup checklist](docs/QUICK_SETUP_CHECKLIST.md) from a separate, clean ChatGPT chat **that has no access to the original author's private Project**. Use the public repo link and [starter prompt](prompts/STARTER_PROMPT.md); check that it guides a new user rather than assuming access to existing CV/emails/trackers.
6. Decide on an explicit content license before broad redistribution. This draft does not presume that the repository owner has chosen one.

## Two GitHub accounts and a 404 from ChatGPT

If your source repository is accessible from one GitHub identity but the destination belongs to a **different identity**, a GitHub API `404 Not Found` is expected for an inaccessible private repository. It does **not** prove the destination is nonexistent.

- In ChatGPT open **Settings > Plugins > GitHub** (or **Apps** if labeled differently). Under **Connected accounts**, use **Connect another account** when available; authorize the account owning the destination and make sure the repository is included in the selected repository permissions. Recheck the actual repository before writing. Multiple account support depends on the app/account; do not disconnect a working source connection unnecessarily.
- Alternatively, from the destination owner's GitHub account, open the repository's **Settings > Collaborators > Add people**, invite the already-connected identity, and accept from that account. Verify **write** access and whether the GitHub app is permitted for that repository. This approach avoids adding a second GitHub connection.
- If permissions change, the repository may take several minutes to become available to ChatGPT. Reopen the connection's repository access settings and check the destination again.

Neither route grants authorization to publish personal applicant records. Review the destination's existing files, default branch and visibility before any changes. Official setup documentation: https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt and https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt .

## Git command-line example (if you are comfortable with Git)

After creating/accessing your destination repo, work in a clean directory with your own authenticated Git account:

```bash
git clone https://github.com/YOUR_OWNER/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
# Copy the *contents* of the downloaded job_discovery folder here.
# Review git status and the actual diff before committing.
git add README.md START_HERE.md INSTALLATION_MANUAL.md PROJECT_INSTRUCTIONS.md PROJECT_INSTRUCTIONS_COMPACT.md \
  SECURITY.md CHANGELOG.md PUBLISHING.md .gitignore docs algorithm prompts templates tests sources scripts
git diff --cached --stat
# Check privacy and source links (normal validation).
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -p "test_*.py"
# From an actual full clone, the public-release gate also checks commit metadata and license:
python3 scripts/validate_package.py --public-release
git commit -m "Add privacy-safe ChatGPT job discovery pipeline"
git push origin HEAD
```

Do not force-push or remove pre-existing repository content as a normal publishing step. **If an existing history contains personal email, that is a separate explicit remediation decision documented in [privacy and history repair](docs/11-RELEASE-PRIVACY.md).** If GitHub returns **404** or **permission denied**, the repository may be missing, private to another account or inaccessible to the connected identity. Resolve access first; do not publish personal documents elsewhere as a workaround.

## Publishing with ChatGPT's GitHub connector

The connected GitHub account must actually have **push/write** access to the specific repository. A successful read of a different private source repository does **not** grant write permission to the destination. Verify the exact repo and branch, write the sanitized files, then **read them back**. If the destination is inaccessible, preserve the downloadable ZIP and report that publication is incomplete.
