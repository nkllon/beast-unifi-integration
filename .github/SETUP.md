# GitHub Repository Setup

This document outlines the steps to set up the GitHub repository and configure CI/CD.

## 1. Create GitHub Repository

```bash
# Create repository on GitHub (via web UI or GitHub CLI)
gh repo create nkllon/beast-unifi-integration \
  --public \
  --description "UniFi network data integration with ServiceNow via Beastmaster framework" \
  --homepage "https://github.com/nkllon/beast-unifi-integration"
```

Or create it manually at: https://github.com/new

## 2. Push Initial Code

```bash
# Add remote (after creating repo)
git remote add origin https://github.com/nkllon/beast-unifi-integration.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 3. Configure GitHub Secrets

Navigate to: **Settings → Secrets and variables → Actions**

Add the following secrets:

### SONAR_TOKEN
1. Go to [SonarCloud](https://sonarcloud.io/)
2. Navigate to **My Account → Security**
3. Generate a new token
4. Copy token and add as `SONAR_TOKEN` secret

### PYPI_API_TOKEN (Optional, for publishing)
1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Navigate to **API tokens**
3. Create a new API token
4. Copy token and add as `PYPI_API_TOKEN` secret

## 4. Set Up SonarCloud Project

1. Go to [SonarCloud](https://sonarcloud.io/)
2. Navigate to your organization (nkllon)
3. Click **Add Project**
4. Select **GitHub** and import `beast-unifi-integration`
5. SonarCloud will automatically detect the `sonar-project.properties` file

## 5. Verify CI/CD

After pushing, check:
- **Actions tab**: CI workflow should run automatically
- **SonarCloud**: Analysis should trigger on push
- **Status badges**: Will appear once workflows complete

## Status Badges

Add these to your README:

```markdown
![CI](https://github.com/nkllon/beast-unifi-integration/workflows/CI/badge.svg)
![SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=nkllon_beast-unifi-integration&metric=alert_status)
```

