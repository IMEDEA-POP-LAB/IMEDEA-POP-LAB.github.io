#!/bin/bash
# Manual script to update repositories data locally
# Usage: ./scripts/update_repositories.sh [GITHUB_TOKEN]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Check if GITHUB_TOKEN is provided as argument or environment variable
if [ -n "$1" ]; then
    export GITHUB_TOKEN="$1"
elif [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ Error: GITHUB_TOKEN is required"
    echo "Usage: $0 [GITHUB_TOKEN]"
    echo "Or set GITHUB_TOKEN environment variable"
    exit 1
fi

export GITHUB_ORG="IMEDEA-POP-LAB"

echo "🔄 Updating repositories data..."
echo "Organization: $GITHUB_ORG"

cd "$PROJECT_ROOT"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required"
    exit 1
fi

# Install dependencies if needed
pip3 install requests pyyaml --quiet

# Run the update script
python3 .github/scripts/update_repositories.py

echo "✅ Repositories data updated successfully!"
echo "📄 Check _data/repositories.yml for the updated data"