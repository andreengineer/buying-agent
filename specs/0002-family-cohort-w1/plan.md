---
name: plan
description: Week plan v2 for family cohort #1 (2026-10-21 → 10-27) — inputs, guardrails, GPT/Codex quota policy, day matrix, CC kickoff. Read first when orchestrating this week.
alwaysApply: false
---

# Week plan v2 — Family cohort #1 · 2026-10-21 → 2026-10-27

## What changed vs v1 (chat version)
| # | Change | Reason |
|---|---|---|
| 1 | Default vertical = durables (R$ 200–5k), not pharmacy + grocery | price gaps are largest on durables and electronics; basket-level grocery gaps are small ([product.md](./product.md) V1); the proven artifact is the beer-fridge report |
| 2 | Autonomy ladder A0 → A1 → A2 replaces "Pix in week 1" | the ceiling (R$ 300) is below a typical durable ticket; agent-prepares / human-pays is how the Brazilian agentic-Pix rails work today |
| 3 | Cohort and ops data live in `~/isaura-data/`, never in this repo | this repo is public |
| 4 | GPT/Codex quota policy with a weekly guard | the weekly cap, not the 5h window, is the binding limit for the build days |
| 5 | Hermes 10h research = `goals/2026-10-21_nightly_goal.md` | Hermes' `ls goals/ \| sort \| tail -1` picks `README.md`; point it at the file explicitly |
| 6 | All Codex/Hermes delegation on `gpt-6.1-sol` effort **low** | André's call; quota lasts longer; gates catch quality misses |
| 7 | Focus guardrails ([spec 0004](../0004-focus-guardrails/spec.md)): calendar block per task, Telegram check-ins, `/park` | ~18 initiatives in 15 days and 60 of 119 sessions under 4 messages; attention needs to be visible |
| 8 | No Notion, no Slack | a new tool is a new initiative; calendar + Telegram + repo already cover time, talk and truth |

## 0. André inputs (defaults apply Thu 2026-10-22 12:00)
| Key | Default | Where it is stored |
|---|---|---|
| VERTICAL | durables R$ 200–5k (home, appliances, electronics, gifts) | `~/isaura-data/cohort/INPUTS.md` |
| CEP | André's | local only |
| COHORT | André + 2 relatives, local aliases `fam_01..` | local only |
| AUTONOMY | A0 for all; A1 for André | local only |
| PIX_CEIL | R$ 300, applies from A2 (week 2+) | local only |
| CHANNEL | Telegram bot, one poller | — |
| CAL_INVITEE | the address of the calendar on André's phone | local only |

CC: ask these in one Telegram message. Never block more than 24h; apply the default and log it.

## 1. Guardrails (soft = warn + log; HARD = enforced)
| Rule | Type |
|---|---|
| Family message content (any channel) → Claude or GPT only | HARD |
| The agent never submits a payment in week 1 (A2 disabled) | HARD |
| Runtime state never mirrors across nodes | HARD |
| Workers on lat: read-only + write to their own output dir | HARD |
| Lanes per week: value 50% · self-org 30% · misc 20% | soft |
| New task triage: unblocks a value goal / < 15 min / friction ≥ 3×/week, else kill with one log line | soft |
| Quiet hours 00:00–09:00: no blocks, no invites, no nudges; sessions started then log `after_midnight` | soft |
| Session > 24h → write handoff, close | soft |
| Every session names its block id first; none → logged `unplanned` | soft |
| New idea mid-block → `/park <idea>`, not a new session | soft |
| WIP: 1 André block at a time · ≤ 4 blocks and ≤ 180 André min per day · ≤ 3 agent runs in parallel | soft |
| A new tool or initiative enters only by killing one (one line in the kill log) | soft |
| Default models: CC Sonnet low; Codex/Hermes `gpt-6.1-sol` low; `medium` only after a gate fails twice, via `escalate:` | soft |

## 2. GPT/Codex quota policy
Facts (checked 2026-10-21): Plus has a 5h window again since 2026-08-25 plus a weekly cap; Pro plans have no 5h window, weekly cap only; weekly numbers are unpublished. OpenAI's per-5h estimates on Plus: gpt-6.1-sol 15–160 messages, gpt-6-luna 350–3,000 ([source](https://justinmckelvey.com/blog/codex-usage-limits), [source](https://9to5mac.com/2026/08/24/openai-restores-5-hour-codex-and-work-limits-for-chatgpt-plus-users/)).

| Lane | Model | Effort | Claim on quota |
|---|---|---|---|
| Build (Codex tasks in [tasks.md](./tasks.md) and spec 0004) | gpt-6.1-sol | low | first claim; research yields at 70% of a 5h window when a build task is queued |
| Research (all cards) | gpt-6.1-sol | low | until the weekly guard |
| Fallback, public web only | DeepSeek v4 flash | — | paid API cap $0.50/night |

Weekly guard: research stops at 45% of the weekly meter, leaving ≥ 55% for Thu–Tue builds. [Guessing on 45% — revise Sunday with real burn data.]

## 3. Day matrix
| Day | Item | Owner | Lane | Done = |
|---|---|---|---|---|
| Wed | P0.1 credential hygiene: rotate anything ever pushed anywhere, confirm at the provider (block A3) | André | value | provider dashboards show old keys revoked |
| Wed | P0.2 single Telegram poller (T2) | CC | value | AC-2 gate green |
| Wed, 10h from launch | Hermes research run H1–H9 | Hermes → Codex | value | `research/2026-10-21/DIGEST.md` + data + charts |
| Wed | T0 contracts | Codex | value | fixtures validate |
| Thu | T1 intake · T3 sourcing · T4 scorer · T5 renderers (parallel) | Codex | value | gates green |
| Fri | T6 flow wiring; first real request answered with L2 + L3 | CC | value | AC-4, AC-5 on a real request |
| Sat | T7 A1 runner · T8 ledger · T9 money guard; first A1 order (André) | CC / Codex | value | AC-6, AC-7, AC-8 |
| Thu→Sun | PalantirView since-last-open ([spec 0003](../0003-pv-since-last-open/spec.md)) | Codex @ lat | self-org | its gates green |
| Sun | T10 metrics + review of guardrail and kill logs | CC | value | `WEEK1.md` |

### André's attention budget (from `../0004-focus-guardrails/week-2026-10-21.blocks.yaml`)
| Day | André blocks | André min | Agent min (est, sol low) |
|---|---|---|---|
| Wed | A1 merge PR · A2 inputs · A3 rotate keys · A4 read reports | 75 | 720 (incl. 600 research) |
| Thu | A5 invite relatives · A6 life-admin unblocker 1 | 50 | 945 |
| Fri | A7 dogfood request · A8 life-admin unblocker 2 | 45 | 120 |
| Sat | A9 pay first A1 Pix | 15 | 270 |
| Sun | A10 PalantirView check · A11 weekly review | 60 | 30 |
| **Week** | **11 blocks** | **245 (~4h)** | **~2,085 (~35h)** |

André's job this week is ~4h of decisions and checks. Everything else is agent time; it shows on the calendar as free `[bot]` events.

Week success: ≥ 3 real requests answered with L2 + L3 · ≥ 1 purchase (A0 or A1) · median time to L2 ≤ 10 min · 0 duplicate replies · mean rating ≥ 4 · savings vs reference measured on every request.

Parked (not this week): Medusa · device media (C65, iPhone, Redmi) · Drive reorg phase 2 · dual-boot · A2 agent payments · pharmacy/grocery vertical · international expansion.

## 4. CC kickoff (run in order)
CC orchestrates; it delegates every implementation and research task to Codex/Hermes on `gpt-6.1-sol` effort low.
Check the exact flags first (`codex exec --help`; [Likely] `-m gpt-6.1-sol -c model_reasoning_effort=low`), always with stdin closed.

1. Verify, 5 lines: Telegram poller count · lat reachable · `codex --version` + login + `/status` meters · Hermes up and which goal path it reads · Hermes' Google Calendar access (F0).
2. Create `~/isaura-data/{cohort,ops}`; copy the blocks template to `~/isaura-data/ops/blocks.yaml`.
3. Start the Hermes run: point it at `goals/2026-10-21_nightly_goal.md` explicitly. Log the quota reading at start.
4. If F0 found calendar access: have Hermes create this week's André blocks from `blocks.yaml` now (static events are enough; F1–F6 automate later). If not: tell André the one consent step.
5. P0.2 (T2). P0.1 is André's block A3 — do not do it for him.
6. Send the §0 questions to André in one Telegram message (this is block A2).
7. Dispatch T0 to Codex. After T0 merges, dispatch T1, T3, T4, T5 in parallel (T3 waits for H8 if it has not landed).
8. Dispatch F1–F5 (spec 0004) to Codex on i7 and spec 0003 to Codex on lat. Keep ≤ 3 agent runs in parallel.
9. End of session: update `docs/STATE.md`.
