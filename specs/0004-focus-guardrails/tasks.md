---
name: tasks
description: Task split for focus guardrails (spec 0004) — Hermes runner, Codex gpt-6.1-sol low implementer, CC reviewer. Pull when building the calendar blocks and check-ins.
alwaysApply: false
---

# Tasks — Focus guardrails

> Codex runs `gpt-6.1-sol` effort `low` with stdin closed. `medium` only after a gate fails twice, and only via `escalate:`.
> Code lives where Hermes' skills live (CC finds it in F0). Data lives in `~/isaura-data/ops/`.

## Plan
| # | Task | Covers AC | Owner | Depends | Est | Gate | Status |
|---|---|---|---|---|---|---|---|
| F0 | Verify Hermes' Google Calendar + Telegram access (read-only: list calendars, send 1 test message to André) | AC-1, AC-4 | CC | — | 15m | 2-line report; if calendar access is missing, stop and tell André the single consent step he must do | todo |
| F1 | `blocks.yaml` loader + validator | AC-1 | Codex | F0 | 30m | test `AC-1`: template validates; bad block rejected | todo |
| F2 | Day planner: quiet hours, WIP, caps, blocked-first, value-first | AC-2, AC-3 | Codex | F1 | 60m | test `AC-2`, `AC-3`: the 5 decision-matrix rows | todo |
| F3 | Calendar writer: idempotent by block id (private extended property), André invited, agent runs free | AC-1 | Codex | F2 | 60m | dry-run prints events JSON; live run on a test day creates 1 event, re-run creates 0 | todo |
| F4 | Telegram: block start line, end buttons, one overrun nudge, `/park` | AC-4, AC-5, AC-6 | Codex | F1 | 60m | tests `AC-4`, `AC-5`, `AC-6` with a fake bot | todo |
| F5 | `blocks.jsonl` log, daily plan message, Sunday PNG chart | AC-8, AC-9 | Codex | F4 | 45m | test `AC-8`, `AC-9` on fixture logs; PNG opens | todo |
| F6 | Wire into Hermes cron: 09:30 plan · 5-min tick · Sunday review | AC-2, AC-8 | CC | F2–F5 | 30m | one full day observed in `blocks.jsonl` | todo |
| F7 | Agent rule for unplanned/after-midnight logging (CLAUDE.md + AGENTS.md) | AC-2, AC-7 | — | — | — | done in this PR | done |

Fallback if F0 finds no calendar access: CC (or the claude.ai session) creates this week's André blocks once from the template; F3 is then done later.

## Definition of Done
- [ ] AC-1 to AC-9 green by gate
- [ ] One real day run end-to-end; André confirms the calendar view is readable on his phone
