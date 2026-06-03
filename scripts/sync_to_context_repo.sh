#!/bin/bash
# sync_to_context_repo.sh — Full pipeline: scan → sanitize → manifest → git push
# Run from: /home/a/Desktop/isaura-hermes-context/

set -e
REPO_DIR="/home/a/Desktop/isaura-hermes-context"
cd "$REPO_DIR"

echo "=== ISAURA CONTEXT SYNC === $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# Step 1: Scan
echo "--- STEP 1: Scanning local context ---"
bash scripts/scan_context.sh
echo ""

# Step 2: Sanitize
echo "--- STEP 2: Sanitizing files ---"
python3 scripts/sanitize_context.py
echo ""

# Step 3: Manifest
echo "--- STEP 3: Generating integrity manifest ---"
python3 scripts/check_context_integrity.py
echo ""

# Step 4: Git status
echo "--- STEP 4: Git status ---"
git status
echo ""

# Step 5: Check for remote
REMOTE=$(git remote get-url origin 2>/dev/null || echo "")

if [ -z "$REMOTE" ]; then
  echo "=== NO GITHUB REMOTE CONFIGURED ==="
  echo ""
  echo "gh is not installed or repo not yet created."
  echo ""
  echo "To set up GitHub, run these commands manually:"
  echo ""
  echo "  # Option A — Install gh CLI and authenticate"
  echo "  sudo apt install gh -y"
  echo "  gh auth login"
  echo "  # (choose GitHub.com → HTTPS → browser login)"
  echo ""
  echo "  # Create private repo and push"
  echo "  cd $REPO_DIR"
  echo "  gh repo create isaura-hermes-context --private --source=. --push"
  echo ""
  echo "  # Option B — Manual GitHub setup (no gh CLI)"
  echo "  # 1. Go to https://github.com/new"
  echo "  # 2. Name: isaura-hermes-context"
  echo "  # 3. Visibility: Private"
  echo "  # 4. Do NOT initialize with README"
  echo "  # 5. Then run:"
  echo "  git remote add origin https://github.com/YOUR_USERNAME/isaura-hermes-context.git"
  echo "  git push -u origin main"
  echo ""
  echo "  # After pushing, invite collaborators:"
  echo "  # GitHub → Settings → Collaborators → Add people"
  echo "  # Invite: passamaniandre@gmail.com (CEO)"
  echo "  # Invite: secondary email used by GPT/Claw"
  echo ""
  echo "Local repo is ready. Push whenever auth is set up."
  exit 0
fi

# Step 6: Stage safe files
echo "--- STEP 6: Staging cloud-safe files ---"
git add README.md CONTEXT_INDEX.md CLOUD_POLICY.md HERMES_README.md \
        CLAW_README.md BROWSER_LLM_PACKET.md MARCELA_RUNBOOK.md \
        board_reports/ goals/ runbooks/ architecture/ manifests/ scripts/ \
        .gitignore 2>/dev/null || true

# Safety check — make sure no .env sneaked in
STAGED_ENV=$(git diff --cached --name-only | grep -iE "\.env$|secret|password|token" || true)
if [ -n "$STAGED_ENV" ]; then
  echo "DANGER: Sensitive file detected in staging:"
  echo "$STAGED_ENV"
  echo "Aborting. Run: git reset HEAD <file> for each"
  exit 1
fi

echo "Staged files:"
git diff --cached --name-only
echo ""

# Step 7: Commit
DATESTAMP=$(date +%Y-%m-%d)
git commit -m "context sync $DATESTAMP" 2>/dev/null || echo "(nothing new to commit)"

# Step 8: Push
echo "--- STEP 7: Pushing to GitHub ---"
git push origin main
echo ""
echo "=== SYNC COMPLETE ==="
echo "Repo URL: $REMOTE"
