---
name: tasks
description: Task split for PalantirView since-last-open summaries (Codex on lat). Pull when implementing 0003.
alwaysApply: false
---

# Tasks — PalantirView: summary since last open

> Owner: Codex on lat, branch `pv-summaries` in the PalantirView repo. Read-only on chat data.
> CC reviews and merges. Model: gpt-6.1-sol effort low for everything; `medium` only after a gate fails twice.

## Plan
| # | Task | Covers AC | Depends | Gate | Status |
|---|---|---|---|---|---|
| 1 | `chat_state` table (chat_id, last_opened_ts, last_msg_id, summary_cache, cache_msg_id) + mark-read | AC-1, AC-7 | — | test `AC-7` | todo |
| 2 | Streaming chunker (40 msgs) + map-reduce merge | AC-4, AC-6 | 1 | test `AC-6`: 5,000-msg fixture, peak RSS < 300 MB | todo |
| 3 | Prompt + output formatter (≤ 12 lines, fixed order) | AC-3 | 2 | test `AC-3` on 3 fixture chats | todo |
| 4 | Size thresholds (≥ 50 / 10–49 / < 10) | AC-1 | 1 | test `AC-1` | todo |
| 5 | Cache by (chat_id, last message id) | AC-2 | 3 | test `AC-2`: reopen → 0 model calls | todo |
| 6 | Egress guard: allowlist of Claude/OpenAI hosts | AC-5 | — | test `AC-5`: other host → call fails + log | todo |
| 7 | UI: collapsible card at top of chat + progress line | AC-1, AC-4 | 3, 4 | test `AC-4`: 50–300 msgs < 30 s on lat | todo |

## Definition of Done
- [ ] AC-1 to AC-7 green by gate
- [ ] Manual check: "Asks for André" correct on 1 real group (André confirms)
