# isaura-hermes-context

**Canonical shared knowledge base for the Isaura / Hermes / Claw AI orchestration system.**

This repo is the single source of truth for non-sensitive project context.
Every orchestration actor — Hermes, Claw, Claude UI, GPT UI, Perplexity — reads from here.

---

## Who uses this repo

| Actor | Role | Access method |
|---|---|---|
| **Andre** | CEO — final judgment | Direct Git, browser |
| **Hermes** | Chairman / nightly goal generator | Git pull + file read |
| **Claw (Claude Code)** | Execution CTO | Git pull/push, local workspace |
| **Claude UI** | Browser LLM — planning & reports | GitHub web or copy-paste packet |
| **GPT UI** | Browser LLM — co-chairman cycle | GitHub web or copy-paste packet |
| **Perplexity** | Browser LLM — research | GitHub web or copy-paste packet |
| **Marcela** | Human relay — copy-paste only | MARCELA_RUNBOOK.md |

---

## What lives here

- Sanitized board reports, goals, runbooks, architecture notes
- Context index and navigation map
- Scripts for scanning, sanitizing, and syncing local files
- Manifests with file integrity checksums

**Start reading:** [`CONTEXT_INDEX.md`](CONTEXT_INDEX.md)

---

## What MUST NEVER be uploaded

- `.env` files or any API keys / tokens / passwords
- SSH keys, OAuth cookies, browser session files
- Raw private audio or transcripts
- Local databases unless explicitly sanitized
- Any file from `workspace/isaura/.env` or similar

**Full policy:** [`CLOUD_POLICY.md`](CLOUD_POLICY.md)

---

## Security model

```
LOCAL SSD (sensitive vault)          CLOUD (this repo)
─────────────────────────────        ─────────────────────────────────
.env files                           board_reports/*.md
API keys / tokens                    goals/*.md / *.json (sanitized)
raw audio / transcripts              runbooks/*.md
OAuth sessions                       architecture/*.md
customer PII                         manifests/context_manifest.json
Evolution API credentials            CONTEXT_INDEX.md
n8n secrets                          scripts/*.sh / *.py
```

---

## Repo structure

```
isaura-hermes-context/
├── README.md               ← you are here
├── CONTEXT_INDEX.md        ← navigation wiki for all actors
├── CLOUD_POLICY.md         ← what can and cannot be uploaded
├── MARCELA_RUNBOOK.md      ← PT-BR step-by-step for Marcela
├── HERMES_README.md        ← Hermes agent instructions
├── CLAW_README.md          ← Claw / Claude Code instructions
├── BROWSER_LLM_PACKET.md  ← copy-paste packet for browser LLMs
├── board_reports/          ← sanitized board cycle reports
├── goals/                  ← nightly goal outputs
├── runbooks/               ← operational procedures
├── architecture/           ← system design docs
├── manifests/              ← integrity manifests
│   └── context_manifest.json
├── scripts/                ← automation scripts
│   ├── scan_context.sh
│   ├── sanitize_context.py
│   ├── check_context_integrity.py
│   └── sync_to_context_repo.sh
└── staging_sanitized/      ← local only, gitignored
```

---

_This file is stable. Update only when repo structure changes._
