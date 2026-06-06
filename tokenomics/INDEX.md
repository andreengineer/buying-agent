# Tokenomics

**Central registry for token budgets, model costs, context allocation, and cost governance.**

Every agent (Hermes, Claw, Claude, ChatGPT, DeepSeek) reads its allocation here. Cérebro (Claude Opus) approves changes.

---

## Files

| File | What | Format |
|------|------|--------|
| `CURRENT.json` | Live budget: who gets what, current consumption, max caps | JSON |
| `MODEL_COSTS.md` | Per-model pricing table (input/output per 1M tokens) | MD |
| `ALLOCATION.md` | Context window allocation per agent/role | MD |
| `history/` | Archived snapshots when CURRENT.json version bumps | — |

## Current vs Previous files

Before this dir existed, tokenomic data lived in:
- `PROMPT_ENTRY.md` — progressive context loading + token budgets
- `architecture/ROUTING_RULES.md` — model routing cost rules
- `manifests/spread_registry.json` — per-model cost ranking
- Hermes memory entries (hot cache)

These should reference `tokenomics/` instead of duplicating data. Migrate on next edit.

## Governance

- Cérebro (Claude Opus) approves budget changes
- Commits are the audit log — `git log tokenomics/` shows every allocation change
- PRs for structural changes (new model, new allocation tier)

---

*Created: 2026-06-06 | Schema: tokenomics-v1*