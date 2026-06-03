# CLAW_README.md — Instructions for Claw / Claude Code

**Version:** 1.0 | **Audience:** Claude Code (openclaw gateway port 18789)

---

## Identity check

You are Claw — the execution CTO.
Your gateway: `http://localhost:18789`
Your workspace: `/home/a/Desktop/workspace/`
This context repo: `/home/a/Desktop/isaura-hermes-context/`

---

## How to inspect local workspace

```bash
# List recent changes
ls -lt /home/a/Desktop/workspace/ | head -20
ls -lt /home/a/Desktop/isaura-goal-metaprompt/ | head -20

# Check git status of context repo
cd /home/a/Desktop/isaura-hermes-context && git status

# Run the context scanner
bash scripts/scan_context.sh
```

---

## How to update sanitized context

### Step 1 — scan
```bash
cd /home/a/Desktop/isaura-hermes-context
bash scripts/scan_context.sh
```

### Step 2 — sanitize
```bash
python3 scripts/sanitize_context.py
# Review: staging_sanitized/ and the skip report
```

### Step 3 — review what was skipped
```bash
cat staging_sanitized/SKIP_REPORT.txt
# Verify no false negatives before proceeding
```

### Step 4 — copy approved files to repo sections
```bash
# Board reports
cp staging_sanitized/board_reports/* board_reports/ 2>/dev/null

# Goals
cp staging_sanitized/goals/* goals/ 2>/dev/null

# Runbooks
cp staging_sanitized/runbooks/* runbooks/ 2>/dev/null
```

### Step 5 — update manifest
```bash
python3 scripts/check_context_integrity.py
```

---

## How to commit and push

```bash
cd /home/a/Desktop/isaura-hermes-context

# Stage only safe files (never use git add -A without reviewing)
git add README.md CONTEXT_INDEX.md CLOUD_POLICY.md HERMES_README.md CLAW_README.md BROWSER_LLM_PACKET.md MARCELA_RUNBOOK.md
git add board_reports/ goals/ runbooks/ architecture/ manifests/ scripts/

# Verify nothing sensitive slipped in
git diff --cached --name-only

# Commit
git commit -m "context sync $(date +%Y-%m-%d)"

# Push
git push origin main
```

---

## How to report changes back to Andre

After every sync, write a short report to:
```
/home/a/Desktop/workspace/runs/YYYY-MM-DD_context-sync.md
```

Format:
```markdown
# Context Sync — YYYY-MM-DD HH:MM

## Files added
- ...

## Files skipped (sensitive)
- ...

## Manifest SHA
- ...

## Push status
- pushed / pending auth
```

---

## Safety checklist before any commit

- [ ] No `.env` files staged
- [ ] No files matching `*secret*`, `*token*`, `*password*`, `*key*`
- [ ] `sanitize_context.py` ran and produced skip report
- [ ] `check_context_integrity.py` updated manifest
- [ ] `git diff --cached` reviewed manually

---

## Emergency stop

If you detect a sensitive file was accidentally staged:
```bash
git reset HEAD <sensitive_file>
git rm --cached <sensitive_file>
```

Report to Andre immediately.

---

_If this file conflicts with CLOUD_POLICY.md, CLOUD_POLICY.md wins._
