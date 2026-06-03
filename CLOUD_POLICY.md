# CLOUD_POLICY.md — What Goes to Cloud vs Stays Local

**Every actor must read this before committing or syncing.**

---

## Decision matrix

### CLOUD-SAFE — may be committed to this repo

| Type | Example | Condition |
|---|---|---|
| Board reports | `BOARD_REPORT_01_claude.md` | No customer names, no credentials |
| Nightly goals | `2026-06-03_nightly_goal.md` | Budget numbers OK, no API keys |
| Runbooks | `RUNBOOK_marcela_paste.md` | No passwords in steps |
| Architecture docs | `today-stack-meta.md` | No IP ranges, no internal URLs with tokens |
| Schemas | `context_manifest.json` | Hashes only, no content |
| Scripts | `scan_context.sh` | No hardcoded secrets |
| Reference guides | `dual-brain-flow.md` | No PII |
| Agent instructions | `HERMES_README.md` | No credentials |

### LOCAL-ONLY — stays on SSD, never commits

| Type | Why | Example path |
|---|---|---|
| `.env` files | Contains API keys | `workspace/isaura/.env` |
| API keys / tokens | Obvious | any `.key`, `*_token.json` |
| OAuth credentials | Account takeover risk | `~/.config/google/` |
| SSH keys | Full machine access | `~/.ssh/id_*` |
| Browser cookies / sessions | Account hijack | `*.cookies`, `LocalStorage/` |
| Raw audio | May contain PII | `*.mp3`, `*.wav` |
| Raw WhatsApp transcripts | Customer PII | `transcripts/raw/` |
| Postgres data | Customer PII | Docker volume |
| n8n secrets | Credentials | Docker env |
| Evolution API session | WhatsApp auth | Docker env |
| Customer files | PII / legal risk | `clients/`, `suppliers/` |
| Personal financial data | Legal risk | any billing records |

### FORBIDDEN-TO-UPLOAD — never, under any circumstances

- API keys for Anthropic, OpenAI, Google, Twilio, or any paid service
- Passwords (email, server, database, VPN)
- OAuth refresh tokens or access tokens
- Private certificates (`.pem`, `.p12`, `.pfx`)
- SSH private keys
- Evolution API `AUTHENTICATION_KEY` or `API_KEY`
- n8n `N8N_BASIC_AUTH_PASSWORD` or `WEBHOOK_URL` with embedded tokens
- Any file flagged `SENSITIVE` by `sanitize_context.py`

---

## Escalation rule

**If unsure whether a file is safe → classify LOCAL-ONLY.**

The cost of over-classifying is low friction.
The cost of under-classifying is account compromise or customer data leak.

Default: **local-only**. Ask Andre to explicitly approve cloud upload.

---

## Sanitization pipeline

Before any file goes to this repo it must pass through:

```bash
scripts/scan_context.sh       # inventory
scripts/sanitize_context.py   # copy-safe + redact
scripts/check_context_integrity.py  # manifest + labels
scripts/sync_to_context_repo.sh     # commit + push
```

Never manually `git add` a file from the local workspace without running the sanitizer first.

---

## Public vs private

This repo is **PRIVATE**.

Making it public-unlisted is a last resort only if:
1. Andre explicitly approves in writing
2. No credentials, PII, or sensitive runbooks are present
3. All current files pass `sanitize_context.py` with zero warnings

Do not make public without Andre's explicit approval.

---

_Policy owner: Andre (CEO). Enforced by: Claw + Hermes._
