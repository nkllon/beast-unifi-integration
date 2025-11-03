# Setting Up GitHub Secrets

## Quick Summary

You need to add secrets to your GitHub repository so CI/CD can work.

## Required: SONAR_TOKEN

1. **Set up SonarCloud project** (if not done):
   - Visit: https://sonarcloud.io/
   - Sign in with GitHub
   - Go to organization: **nkllon**
   - Click **"Add Project"**
   - Select **GitHub** and import **beast-unifi-integration**
   - SonarCloud will auto-detect `sonar-project.properties`

2. **Get SonarCloud token**:
   - Visit: https://sonarcloud.io/account/security
   - Sign in with GitHub
   - Click **"Generate"** under Tokens
   - Name: `beast-unifi-integration-github-actions`
   - **Copy the token** (you'll only see it once!)

3. **Add to GitHub** (choose one method):

   **Method A: Interactive Script** (easiest)
   ```bash
   ./scripts/setup_github_secrets.sh
   ```
   The script will prompt you to paste the token.

   **Method B: GitHub CLI**
   ```bash
   # It will prompt you for the token
   gh secret set SONAR_TOKEN --repo nkllon/beast-unifi-integration
   ```

   **Method C: Web UI**
   - Visit: https://github.com/nkllon/beast-unifi-integration/settings/secrets/actions
   - Click **"New repository secret"**
   - Name: `SONAR_TOKEN`
   - Value: (paste your token)
   - Click **"Add secret"**

## Optional: PYPI_API_TOKEN

Only needed if you want to publish packages to PyPI.

1. Visit: https://pypi.org/manage/account/
2. Navigate to **"API tokens"**
3. Click **"Add API token"**
4. Name: `beast-unifi-integration`
5. Scope: Choose "Entire account" or project-specific
6. **Copy the token** (starts with `pypi-`)
7. Add to GitHub using one of the methods above

## Verify

After adding secrets, check:
- GitHub Actions will run automatically on next push
- SonarCloud analysis will start working
- View status: https://github.com/nkllon/beast-unifi-integration/actions
