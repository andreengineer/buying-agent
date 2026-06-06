# CONTEXT_INDEX.md — Orchestration Navigation Map

**LLM entry point:** [`PROMPT_ENTRY.md`](PROMPT_ENTRY.md) — progressive context loading with token budgets.
**Universal entry:** [`llms.txt`](llms.txt) — one-line-per-file index for any LLM.

**This is the navigation map.** It tells you where everything lives and how to consume it.

---

## Token budget (entire repo)

| Level | Tokens | What fits |
|---|---|---|
| 🟢 Minimal | ~800 | Navigation + your role |
| 🟡 Standard | ~2,500 | Navigation + validation + routing |
| 🟠 Full | ~5,000 | Everything except manifests + scripts |
| 🔴 Max | ~8,000 | Entire repo |

**Always start with [`PROMPT_ENTRY.md`](PROMPT_ENTRY.md)** — it tells you exactly which files to read at each tier.

---

## System actors quick-reference

| Actor | Model | Read from | Write to | Notes |
|---|---|---|---|---|
| Hermes | DeepSeek V4-flash + OpenRouter | `goals/`, `board_reports/` | `goals/YYYY-MM-DD_nightly.md` | See `HERMES_README.md` |
| Claw (OpenClaw) | DeepSeek V4-flash | all files | `board_reports/`, sanitized context | Port 18789. See `CLAW_README.md` |
| Claude UI | Opus (browser) | this repo via GitHub or paste | board format `.md` artifacts | Reads `ALPHA-VALIDATION.md`, `PREMIUMUI-ACCESS.md` |
| GPT UI | GPT-5 (browser) | this repo via GitHub or paste | board format `.md` artifacts | See `BROWSER_LLM_PACKET.md` |
| Perplexity | Pro (browser) | this repo via GitHub | research memos | See `BROWSER_LLM_PACKET.md` |
| Andre | — | everything | approvals, git via Telegram/cron | CEO, final judgment |

---

## Where board reports live

**Cloud:** `board_reports/`
- Naming: `BOARD_REPORT_{cycle:02d}_{author}.md`
- Author codes: `claude`, `gpt`, `hermes`, `andre`
- Co-chairman cycle: Claude writes odd cycles, GPT writes even (or as agreed)
- Each report responds to the previous cycle's delta

**Local source:** `/home/a/Desktop/isaura-goal-metaprompt/BOARD_REPORT_*.md`

---

## Where Hermes goals live

**Cloud:** `goals/`
- Naming: `YYYY-MM-DD_nightly_goal.md`
- Format: JSON + MD dual format accepted
- Contains: budget, profile, phase breakdown, freeze rules

**Local source:** `/home/a/Desktop/isaura-goal-metaprompt/goal*.json`
**Local output:** `/home/a/Desktop/workspace/hermes-latest/output.md`

---

## Where Claw execution logs live

**Cloud:** `board_reports/` (sanitized summaries only)
**Local only:** `/home/a/Desktop/workspace/runs/YYYY-MM-DD_slug.md`
- Raw runs stay local — may contain sensitive data

---

## Where runbooks live

**Cloud:** `runbooks/`
- Operational procedures, integration guides, checklists
- Named: `RUNBOOK_{topic}.md`

**Local source:** `/home/a/Desktop/isaura-goal-metaprompt/references/*.md`

---

## Where architecture notes live

**Cloud:** `architecture/`
- System design, stack diagrams (SVG-exported as PNG if needed), decision records

**Local source:**
- `/home/a/Desktop/workspace/diagrams/`
- `/home/a/Desktop/workspace/design/`

---

## What stays LOCAL ONLY (never in this repo)

| Data type | Local path |
|---|---|
| `.env` files / API keys | `workspace/isaura/.env`, all `.env.*` |
| n8n secrets | Docker env |
| Evolution API credentials | Docker env |
| OAuth tokens / cookies | `~/.config/`, browser profiles |
| SSH keys | `~/.ssh/` |
| Raw audio / transcripts | `workspace/` and any local path |
| Customer PII | any `clients/` dir |
| WhatsApp session files | Evolution API container |
| Postgres data | Docker volume |

---

## Active services (for agent orientation)

| Port | Service | Notes |
|---|---|---|
| 18789 | OpenClaw gateway | Claw execution arm |
| 8080 | Evolution API | WhatsApp — credentials stay local |
| 5678 | n8n | workflow automation |
| 11434 | Ollama | local LLM inference |
| 22 | SSH | remote access |

---

## How browser LLMs should consume this context

1. Read `CONTEXT_INDEX.md` (this file) first
2. Read `PREMIUMUI-ACCESS.md` — tells you which files to consume per role
3. If tasked with alpha validation → read `ALPHA-VALIDATION.md` — complete stack validation protocol
4. Read the relevant section file (`board_reports/`, `goals/`, etc.)
5. Produce output in board `.md` format
6. Do NOT request `.env`, raw transcripts, or any local-only data
7. If a file is missing, ask Andre — do not assume

**Full packet for pasting into browser:** [`BROWSER_LLM_PACKET.md`](BROWSER_LLM_PACKET.md)

---

## Spread orchestration

Multi-model spread notation: `spread(MODE;DEPTH)`
- `spread(l;5)` = linear chain, top 5 models
- `spread(p;4)` = parallel, 4 slots → Opus converges
- `spread(p;2)` = quick parallel (e.g. GPT → DeepSeek)

Full spec: [`architecture/SPREAD_ARCHITECTURE.md`](architecture/SPREAD_ARCHITECTURE.md)
Model registry + slot assignments: [`manifests/spread_registry.json`](manifests/spread_registry.json)
Browser relay procedure: [`runbooks/RUNBOOK_browser_spread.md`](runbooks/RUNBOOK_browser_spread.md)

**API spread = FUTURE / ROI-gated. Browser-UI relay is the active path.**

---

## Manifest

Current integrity manifest: [`manifests/context_manifest.json`](manifests/context_manifest.json)
Spread model registry: [`manifests/spread_registry.json`](manifests/spread_registry.json)
Run `scripts/check_context_integrity.py` to refresh.

---

## Archive (compressed context)

Files older than 14 days are auto-compressed into ~75-token summaries.

- **Archive index:** [`archive/ARCHIVE_INDEX.md`](archive/ARCHIVE_INDEX.md)
- **Originals preserved:** `archive/raw/<category>/<file>`
- **Compression tool:** `python3 scripts/compress_context.py`
- **Preview:** `python3 scripts/compress_context.py --dry-run`

### File sizes (token estimates)

| File | Lines | ~Tokens |
|---|---|---|
| `CONTEXT_INDEX.md` | 155 | ~390 |
| `PROMPT_ENTRY.md` | 100 | ~250 |
| `llms.txt` | 55 | ~140 |
| `ALPHA-VALIDATION.md` | 381 | ~950 |
| `HERMES_README.md` | 196 | ~490 |
| `CLAW_README.md` | 141 | ~350 |
| `BROWSER_LLM_PACKET.md` | 94 | ~235 |
| `PREMIUMUI-ACCESS.md` | 98 | ~245 |
| `MARCELA_RUNBOOK.md` | 103 | ~260 |
| `CLOUD_POLICY.md` | 91 | ~230 |
| `CLAUDE_PROJECT_INIT.md` | 157 | ~390 |
| `architecture/SPREAD_ARCHITECTURE.md` | 171 | ~430 |
| `architecture/ROUTING_RULES.md` | 97 | ~240 |
| `architecture/ACCOUNTABILITY_GOVERNOR.md` | 139 | ~350 |
| `architecture/ISAURA_SYSTEM_STATE.md` | 106 | ~265 |
| `goals/2026-06-03_alpha_launch_todo.md` | 84 | ~210 |
| `runbooks/RUNBOOK_browser_spread.md` | 139 | ~350 |
| `manifests/spread_registry.json` | 220 | ~550 |
| `manifests/context_manifest.json` | 504 | ~1,300 |

**Total repo: ~3,400 lines / ~8,000 tokens / 500KB**

---

_Last updated by: Isaura / 2026-06-06_
