# PREMIUMUI-ACCESS.md — How Browser LLMs Consume This Repo

**For:** Claude UI (Claude Opus), GPT UI (GPT-5), Perplexity Pro, and any other browser-based LLM
**Repo URL:** `https://github.com/andreengineer/buying-agent`

---

## Three access modes

### Mode A — Direct GitHub access (PREFERRED)

If the browser LLM can open URLs (most can):
```
1. Open: https://github.com/andreengineer/buying-agent
2. Navigate to the file you need
3. Read directly — you have full repo access
```

**Starting point:** `llms.txt` (universal entry) → `PROMPT_ENTRY.md` (token-budgeted loading) → `CONTEXT_INDEX.md` (full navigation)

### Mode B — Raw file URLs (ideal for copy-paste)

```
https://raw.githubusercontent.com/andreengineer/buying-agent/main/CONTEXT_INDEX.md
https://raw.githubusercontent.com/andreengineer/buying-agent/main/ALPHA-VALIDATION.md
https://raw.githubusercontent.com/andreengineer/buying-agent/main/goals/2026-06-03_alpha_launch_todo.md
```

Just open these URLs — they render as plain text.

### Mode C — Marcela relay (fallback, SLOW)

If GitHub is unreachable and the LLM can't open URLs:
1. Ask Marcela to open `https://github.com/andreengineer/buying-agent`
2. She navigates to the file you need
3. She copies the content and pastes it to you

> Marcela is copy-paste only — do NOT ask her to interpret or modify content.

---

## Which files each PremiumUI role should read

### Claude UI (Co-chairman / Alpha auditor)
- `CONTEXT_INDEX.md` — navigation
- `ALPHA-VALIDATION.md` — this validation protocol
- `goals/` — latest goals and TODOs
- `architecture/ROUTING_RULES.md` — model routing
- `architecture/ACCOUNTABILITY_GOVERNOR.md` — anti-escapism
- `board_reports/` — latest co-chairman reports

### GPT UI (Architecture / Data model reviewer)
- Same as Claude UI, plus:
- `architecture/SPREAD_ARCHITECTURE.md` — spread orchestration
- `manifests/spread_registry.json` — model ranking

### Perplexity Pro (Research)
- `goals/` — understand what's being researched
- `architecture/ISAURA_SYSTEM_STATE.md` — system context
- Direct your research to specific product/category questions

---

## Files you should NEVER request

PremiumUI should never ask Marcela or Andre for:
- `.env` files / API keys / tokens / passwords
- `~/.ssh/` or any SSH key files
- Raw audio transcripts or customer PII
- Local database files
- Browser session cookies or OAuth tokens

If you need data not in this repo → **ask Andre directly**. Do not assume or hallucinate.

---

## Quick reference: key paths

```
Repo root
├── ALPHA-VALIDATION.md         ← VALIDATION PROTOCOL (read this for alpha checks)
├── CONTEXT_INDEX.md            ← NAVIGATION MAP (read first)
├── BROWSER_LLM_PACKET.md       ← Copy-paste session init packet
├── PREMIUMUI-ACCESS.md         ← This file
├── goals/
│   └── 2026-06-03_alpha_launch_todo.md  ← Active TODO
├── architecture/
│   ├── ISAURA_SYSTEM_STATE.md
│   ├── ROUTING_RULES.md
│   └── ACCOUNTABILITY_GOVERNOR.md
├── board_reports/              ← Co-chairman cycles
├── runbooks/                   ← Marcela & spread protocols
└── manifests/                  ← Model registry & integrity
```

---

*Last updated: 2026-06-04*
*This file is read by PremiumLLMs. Marcela can relay its content if needed.*