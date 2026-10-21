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

## 0. André inputs (defaults apply Thu 2026-10-22 12:00)
| Key | Default | Where it is stored |
|---|---|---|
| VERTICAL | durables R$ 200–5k (home, appliances, electronics, gifts) | `~/isaura-data/cohort/INPUTS.md` |
| CEP | André's | local only |
| COHORT | André + 2 relatives, local aliases `fam_01..` | local only |
| AUTONOMY | A0 for all; A1 for André | local only |
| PIX_CEIL | R$ 300, applies from A2 (week 2+) | local only |
| CHANNEL | Telegram bot, one poller | — |

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
| New session after 00:00 local → warn + log, reviewed Sunday | soft |
| Session > 24h → write handoff, close | soft |
| Default models: Sonnet low; Codex gpt-6.1-sol high; `max` and Opus only with `escalate:` | soft |

## 2. GPT/Codex quota policy
Facts (checked 2026-10-21): Plus has a 5h window again since 2026-08-25 plus a weekly cap; Pro plans have no 5h window, weekly cap only; weekly numbers are unpublished. OpenAI's per-5h estimates on Plus: gpt-6.1-sol 15–160 messages, gpt-6-luna 350–3,000 ([source](https://justinmckelvey.com/blog/codex-usage-limits), [source](https://9to5mac.com/2026/08/24/openai-restores-5-hour-codex-and-work-limits-for-chatgpt-plus-users/)).

| Lane | Model | Effort | Claim on quota |
|---|---|---|---|
| Build (Codex tasks in [tasks.md](./tasks.md)) | gpt-6.1-sol | high | first claim; research yields at 70% of a 5h window when a build task is queued |
| Research synthesis | gpt-6.1-sol | medium | until the weekly guard |
| Research bulk extraction | gpt-6-luna | default | until the weekly guard |
| Fallback, public web only | DeepSeek v4 flash | — | paid API cap $0.50/night |

Weekly guard: research stops at 45% of the weekly meter, leaving ≥ 55% for Thu–Tue builds. [Guessing on 45% — revise Sunday with real burn data.]

## 3. Day matrix
| Day | Item | Owner | Lane | Done = |
|---|---|---|---|---|
| Wed | P0.1 credential hygiene: rotate anything ever pushed anywhere, confirm at the provider | CC + André | value | provider dashboards show old keys revoked |
| Wed | P0.2 single Telegram poller (T2) | CC | value | AC-2 gate green |
| Wed, 10h from launch | Hermes research run H1–H9 | Hermes → Codex | value | `research/2026-10-21/DIGEST.md` + data + charts |
| Wed | T0 contracts | Codex | value | fixtures validate |
| Thu | T1 intake · T3 sourcing · T4 scorer · T5 renderers (parallel) | Codex | value | gates green |
| Fri | T6 flow wiring; first real request answered with L2 + L3 | CC | value | AC-4, AC-5 on a real request |
| Sat | T7 A1 runner · T8 ledger · T9 money guard; first A1 order (André) | CC / Codex | value | AC-6, AC-7, AC-8 |
| Thu→Sun | PalantirView since-last-open ([spec 0003](../0003-pv-since-last-open/spec.md)) | Codex @ lat | self-org | its gates green |
| Sun | T10 metrics + review of guardrail and kill logs | CC | value | `WEEK1.md` |

Week success: ≥ 3 real requests answered with L2 + L3 · ≥ 1 purchase (A0 or A1) · median time to L2 ≤ 10 min · 0 duplicate replies · mean rating ≥ 4 · savings vs reference measured on every request.

Parked (not this week): Medusa · device media (C65, iPhone, Redmi) · Drive reorg phase 2 · dual-boot · A2 agent payments · pharmacy/grocery vertical · international expansion.

## 4. CC kickoff (run in order)
1. Verify, 4 lines: Telegram poller count · lat reachable · `codex --version` + login + `/status` meters · Hermes up and which goal path it reads.
2. Create `~/isaura-data/{cohort,ops}`.
3. Start the Hermes run: point it at `goals/2026-10-21_nightly_goal.md` explicitly. Log the quota reading at start.
4. P0.1 and P0.2.
5. Send the §0 questions to André in one Telegram message.
6. Dispatch T0 to Codex. After T0 merges, dispatch T1, T3, T4, T5 in parallel (T3 waits for H8 if it has not landed).
7. Dispatch spec 0003 to Codex on lat.
8. End of session: update `docs/STATE.md`.
