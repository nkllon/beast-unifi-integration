#!/bin/bash
# Setup script for GitHub secrets
# Usage: ./scripts/setup_github_secrets.sh

set -e

REPO="nkllon/beast-unifi-integration"

echo "=============================================================="
echo "GITHUB SECRETS SETUP"
echo "=============================================================="
echo ""
echo "This script will help you add secrets to your GitHub repository."
echo "Repository: $REPO"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "   Install: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub CLI"
    echo "   Run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI is installed and authenticated"
echo ""

# SONAR_TOKEN
echo "📋 Setting up SONAR_TOKEN..."
echo ""
echo "To get your SonarCloud token:"
echo "  1. Visit: https://sonarcloud.io/account/security"
echo "  2. Sign in with GitHub"
echo "  3. Generate a new token"
echo "  4. Copy the token"
echo ""
read -p "Enter your SONAR_TOKEN (or press Enter to skip): " sonar_token

if [ -n "$sonar_token" ]; then
    echo "$sonar_token" | gh secret set SONAR_TOKEN --repo "$REPO"
    echo "✅ SONAR_TOKEN added successfully"
else
    echo "⚠️  Skipped SONAR_TOKEN (add manually later)"
fi

echo ""

# PYPI_API_TOKEN
echo "📋 Setting up PYPI_API_TOKEN (optional)..."
echo ""
echo "To get your PyPI token:"
echo "  1. Visit: https://pypi.org/manage/account/"
echo "  2. Navigate to: API tokens"
echo "  3. Create a new token (project scope recommended)"
echo "  4. Copy the token (starts with pypi-)"
echo ""
read -p "Enter your PYPI_API_TOKEN (or press Enter to skip): " pypi_token

if [ -n "$pypi_token" ]; then
    echo "$pypi_token" | gh secret set PYPI_API_TOKEN --repo "$REPO"
    echo "✅ PYPI_API_TOKEN added successfully"
else
    echo "⚠️  Skipped PYPI_API_TOKEN (add manually later if needed)"
fi

echo ""
echo "=============================================================="
echo "✅ Secrets setup complete!"
echo "=============================================================="
echo ""
echo "To verify secrets:"
echo "  gh secret list --repo $REPO"
echo ""

