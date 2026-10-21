---
name: spec
description: Contract for André's visible focus guardrails — calendar time blocks per task, Telegram check-ins, parking lot, quiet hours, WIP, weekly planned-vs-actual. Pull when building or running the focus system.
alwaysApply: false
---

# Spec — Focus guardrails (calendar + check-ins)

> **Source of truth.** Status: draft — approval = merge of PR `feat/0002-family-cohort-w1`.
> All rules are **soft**: they show, warn and log. They never refuse or block work.
> Lane: self-org. Runner: Hermes (has the Google account). Code: Codex `gpt-6.1-sol` low. Review: CC.

## Why (from André's own usage data, 2026-10-06 → 10-20)
| Observed | Number | Guardrail that answers it |
|---|---|---|
| Sessions abandoned almost at once | 60 of 119 sessions had < 4 messages | every session starts by naming a block (AC-7) |
| Initiatives running at once | ~18 in 15 days; 4 blocked on André | WIP 1 + blocked-on-André first (AC-3) |
| Value goals with zero execution | 3 of 3 | value blocks scheduled before self-org (AC-3) |
| Sessions never closed | 34h, 91h, 93h, 234h open | block end check-in + handoff (AC-4) |
| Same work started twice | brain index built in 2 threads 14 min apart | parking lot instead of new session (AC-6) |
| Work after midnight | this plan was written 02:52 → 05:48 | quiet hours 00:00–09:00 (AC-2) |
| Hardware unplugged mid-run | C65 left half-committed | agent runs visible as calendar events (AC-1) |

The principle: **time and attention made visible outside André's head**. Calendar = time map. Telegram = the only conversation. Repo = the only truth. No new tool.

## Acceptance criteria

### AC-1: every task has a visible block with an estimate
- **Given** a block in `blocks.yaml` (template: `./week-2026-10-21.blocks.yaml`)
- **When** the day plan runs
- **Then** an event exists on Hermes' calendar with André invited (`CAL_INVITEE` from local inputs)
- **And** the title is `[V|S|M] <id> <task> — <est>m` for André blocks (busy) and `[bot] <id> <task> — ~<est>m` for agent runs (free)
- **And** the description holds: Done =, Start here (one link), "Something else came up? /park it in Telegram"
- **And** re-running the planner updates the same event (idempotent by block id), never duplicates it

### AC-2: quiet hours
- **Given** any time between 00:00 and 09:00 local
- **Then** no block is scheduled in that window, no invite is sent, and no Telegram nudge is sent
- **And** an agent session started in that window logs `after_midnight` once and continues

### AC-3: one thing at a time, value first
- **Given** the day's candidate blocks
- **Then** the planner schedules at most 4 André blocks and at most 180 André minutes per day,
  never overlaps two André blocks, and runs at most 3 agent runs in parallel
- **And** any block tagged `blocked_on_andre` is placed first in the day as a ≤ 15 min decision block
- **And** value-lane blocks are placed before self-org and misc blocks on the same day

### AC-4: block start and end check-in
- **When** an André block starts
- **Then** Telegram gets one line: id, task, minutes, Done =, link
- **When** it reaches its estimate
- **Then** Telegram asks with 3 buttons: `done` · `+15m` · `park`
- **And** the answer and actual minutes are appended to `~/isaura-data/ops/blocks.jsonl`

### AC-5: one overrun nudge, then silence
- **Given** a block at 150% of its estimate with no answer
- **Then** exactly one nudge is sent; nothing more until the next block

### AC-6: parking lot instead of a new session
- **When** André sends `/park <text>` to the Hermes bot
- **Then** the text is appended to `~/isaura-data/ops/parking.md` with time and current block id
- **And** the bot replies `parked #N` and starts nothing

### AC-7: unplanned sessions are visible
- **Given** an agent session whose first user message names no block id (`T#`, `H#`, `F#`, `PV#`, `A#`)
- **Then** the agent logs `unplanned` to `~/isaura-data/ops/guardrail.log` and continues normally

### AC-8: daily plan message
- **At** 09:30 local (or the first message after 09:00, whichever is later)
- **Then** Telegram gets: today's André blocks with times and total minutes, today's agent runs,
  yesterday planned vs actual minutes, open parking-lot count

### AC-9: weekly review
- **On** Sunday at the review block
- **Then** a PNG chart shows planned vs actual minutes per lane, the estimate ratio (median actual ÷ estimate),
  counts of `unplanned` and `after_midnight`, and the parking lot list for keep/kill

## Decision matrix — planner placement

| Block type | Tag | Time now | Result | AC |
|---|---|---|---|---|
| André | `blocked_on_andre` | 09:00–23:59 | first slot of the day, ≤ 15 min | AC-3 |
| André | value | 09:00–23:59 | after decision blocks, before S/M | AC-3 |
| André | self-org / misc | 09:00–23:59 | after value blocks; skipped if day > 180 min | AC-3 |
| any | — | 00:00–08:59 | not scheduled; no invite; no nudge | AC-2 |
| agent | — | any | free event; ≤ 3 parallel; queued beyond | AC-3 |

## Out of scope
- Notion, Slack or any new tool (see `plan.md` — a new tool must kill one existing tool first).
- Hard blocking, app blockers, refusals.
- Tracking André's phone or screen time.

## Traceability
- Tasks: [tasks.md](./tasks.md) · Blocks template: `./week-2026-10-21.blocks.yaml` · Week plan: [../0002-family-cohort-w1/plan.md](../0002-family-cohort-w1/plan.md)
