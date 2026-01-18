#!/bin/bash
# Setup script for GitHub secrets across all Beastmaster repos
# Usage: ./scripts/setup_all_beast_secrets.sh

set -e

echo "=============================================================="
echo "BEASTMASTER REPOS SECRETS SETUP"
echo "=============================================================="
echo ""

# All Beastmaster repos
REPOS=(
    "beast-observatory"
    "beast-ai-dev-agent"
    "beast-orchestrator"
    "beast-node"
    "beast-mailbox-agent"
)

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

# Function to check secret status
check_secret() {
    local repo=$1
    local secret=$2
    if gh secret list -R "nkllon/$repo" 2>/dev/null | grep -q "^$secret"; then
        return 0
    else
        return 1
    fi
}

# Function to add secret
add_secret() {
    local repo=$1
    local secret_name=$2
    local value=$3
    echo "$value" | gh secret set "$secret_name" --repo "nkllon/$repo" 2>&1
}

echo "📋 Checking current status..."
echo ""

# Check what's missing
MISSING_SONAR=()
MISSING_PYPI=()

for repo in "${REPOS[@]}"; do
    has_sonar=$(check_secret "$repo" "SONAR_TOKEN" && echo "yes" || echo "no")
    has_pypi=$(check_secret "$repo" "PYPI_API_TOKEN" && echo "yes" || echo "no")
    
    if [ "$has_sonar" = "no" ]; then
        MISSING_SONAR+=("$repo")
    fi
    if [ "$has_pypi" = "no" ]; then
        MISSING_PYPI+=("$repo")
    fi
    
    echo "  $repo: SONAR_TOKEN=$has_sonar, PYPI_API_TOKEN=$has_pypi"
done

echo ""

# SONAR_TOKEN
if [ ${#MISSING_SONAR[@]} -gt 0 ]; then
    echo "📋 Setting up SONAR_TOKEN for ${#MISSING_SONAR[@]} repo(s)..."
    echo "   Repos: ${MISSING_SONAR[*]}"
    echo ""
    echo "💡 The same SonarCloud token works for all repos."
    echo ""
    read -p "Enter your SONAR_TOKEN (or press Enter to skip): " sonar_token
    
    if [ -n "$sonar_token" ]; then
        for repo in "${MISSING_SONAR[@]}"; do
            echo "  Adding to $repo..."
            add_secret "$repo" "SONAR_TOKEN" "$sonar_token" && echo "  ✅ Added to $repo" || echo "  ❌ Failed for $repo"
        done
    else
        echo "⚠️  Skipped SONAR_TOKEN"
    fi
    echo ""
else
    echo "✅ All repos have SONAR_TOKEN"
    echo ""
fi

# PYPI_API_TOKEN
if [ ${#MISSING_PYPI[@]} -gt 0 ]; then
    echo "📋 Setting up PYPI_API_TOKEN for ${#MISSING_PYPI[@]} repo(s)..."
    echo "   Repos: ${MISSING_PYPI[*]}"
    echo ""
    read -p "Enter your PYPI_API_TOKEN (or press Enter to skip): " pypi_token
    
    if [ -n "$pypi_token" ]; then
        for repo in "${MISSING_PYPI[@]}"; do
            echo "  Adding to $repo..."
            add_secret "$repo" "PYPI_API_TOKEN" "$pypi_token" && echo "  ✅ Added to $repo" || echo "  ❌ Failed for $repo"
        done
    else
        echo "⚠️  Skipped PYPI_API_TOKEN"
    fi
    echo ""
else
    echo "✅ All repos have PYPI_API_TOKEN"
    echo ""
fi

echo "=============================================================="
echo "✅ Secrets setup complete!"
echo "=============================================================="
echo ""
echo "To verify secrets for a repo:"
echo "  gh secret list --repo nkllon/<repo-name>"
echo ""

