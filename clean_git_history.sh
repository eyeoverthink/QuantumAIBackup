#!/bin/bash
# Clean Git History - Remove Large Files
# This will rewrite git history to remove large files permanently

echo "🧹 Git Repository Cleanup Script"
echo "=================================="
echo ""
echo "⚠️  WARNING: This will rewrite git history!"
echo "⚠️  Make sure you have a backup before proceeding."
echo ""
read -p "Continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 1
fi

echo ""
echo "📊 Current repository size:"
du -sh .git

echo ""
echo "🔍 Finding large files in git history..."
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  sed -n 's/^blob //p' | \
  sort --numeric-sort --key=2 | \
  tail -20 | \
  cut -c 1-12,41- | \
  $(command -v gnumfmt || echo numfmt) --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest

echo ""
echo "🗑️  Removing large files from history..."

# Install git-filter-repo if not present
if ! command -v git-filter-repo &> /dev/null; then
    echo "Installing git-filter-repo..."
    pip3 install git-filter-repo
fi

# Remove large directories from history
git filter-repo --path venv --path qr_dna_env --path quantum_env --path face_qr_venv \
    --path consolidated_quantum --path quantum_extras/deep_learning/evolution_history \
    --path quantum_extras/deep_learning/checkpoints --invert-paths --force

echo ""
echo "🧹 Running garbage collection..."
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo ""
echo "📊 New repository size:"
du -sh .git

echo ""
echo "✅ Cleanup complete!"
echo ""
echo "📤 To push to GitHub, run:"
echo "   git push --force origin main"
echo ""
echo "⚠️  Note: Force push will rewrite remote history!"
