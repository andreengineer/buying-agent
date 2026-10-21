---
name: nightly-goal-2026-10-21
description: Hermes 10h research run (starts at launch on 2026-10-21) for family cohort #1 — value data, rails, integrations; burns spare GPT subscription quota under a weekly guard. Read when running or reviewing this cycle.
alwaysApply: false
---

# Nightly Goal — 2026-10-21

**Budget:** $0.50 paid API (DeepSeek fallback only) · GPT subscription quota per the policy below
**Profile:** Bold on subscription quota · Lean on cash
**Cycle:** research-01
**Window:** 10h from launch (log the start time in `run.jsonl`) · report at launch + 10h
**Assumption:** "GPT API" here = the ChatGPT-login Codex quota (sunk cost). If an OpenAI API key with
credits is used instead, it is cash: the $0.50 freeze rule applies to it.

## Objective
Turn the family-cohort thesis into numbers: where a buying agent creates measurable value
(money, risk, time) and which payment rails and integrations are viable this month.

## Quota policy (read before launching anything)
1. Read the meters at start and every 60 min: Codex `/status` (5h and weekly). If no machine-readable
   meter exists, count messages per 5h window: gpt-6.1-sol ≤ 60, gpt-6-luna ≤ 800.
2. Bulk extraction → gpt-6-luna. Synthesis and judgment → gpt-6.1-sol, effort medium. Never `max`.
3. Build has first claim: if `~/isaura-data/ops/dispatch.md` shows a queued Codex build task, research
   pauses when the 5h meter reaches 70%.
4. **Weekly guard:** stop all research cards at 45% of the weekly meter. Finish writing outputs with what exists.
5. GPT exhausted → DeepSeek v4 flash for public-web cards only.
6. This goal's rules replace the generic 40%-per-model freeze for subscription quota. The 40% rule still applies to paid API dollars.

## Research cards
| Id | Question | Method | Output | Feeds |
|---|---|---|---|---|
| H1 | How much does comparison save, by category? | 30 SKUs: 10 durables/appliances, 10 electronics accessories, 10 pharmacy OTC. ≥ 5 offers each from aggregators (Buscapé, Zoom, Google Shopping) and public marketplace pages. Landed cost to a public reference CEP in central Vitória-ES (never André's) | `data/h1_offers.csv` · `charts/h1_dispersion.png` (box plot by category) · median and P90 of (median offer − best valid offer) / median offer | default vertical; savings-share pricing |
| H2 | How often is the cheapest offer a risky one? | For H1 offers: seller age, reviews, official store, CNPJ shown, complaint signals. Apply design §5 rules | `data/h2_assurance.csv` · `charts/h2_cheapest_risky.png` · % of cheapest offers failing ≥ 1 check | assurance thresholds and weight |
| H3 | Which popularity signals can the scorer trust? | 20 products: marketplace rating and count vs brand complaint signals vs return complaints | `h3_signals.md` (≤ 1 page) | popularity weight |
| H4 | How long does a human take to research a durable? | Reconstruct the manual path for 5 SKUs: pages, tabs, minutes; compare with pipeline time | `data/h4_time.csv` | value framing |
| H5 | Which rail can carry A2 (agent-paid Pix) later? | Jota, Magie, PicPay assistant, Asaas (CodeSpar MCP), Mercado Pago, Iniciador agentic Pix, Visa/Mastercard agentic tokens in Brazil: available to individuals?, API vs chat, limits, fees, KYC, dispute path | `data/h5_rails.csv` + 5-line recommendation | week-2 A2 decision |
| H6 | Integrate local delivery or deep-link it? | 99 Entrega, Uber Flash, Lalamove, Loggi in Vitória and Guarapari: coverage, price for 5 km and 15 km, API or link only | `data/h6_lastmile.csv` | integrate vs link |
| H7 | Who else does this and how do they charge? | International and LatAm peers (agentic checkout, human+AI concierges, WhatsApp-native finance). Buy-side models only; affiliate/cashback recorded as foregone revenue | `peers.md` (≤ 2 pages) | week-2 pricing questions |
| H8 | Which marketplaces can the agent use, and how? | Mercado Livre, Amazon BR, Magalu, Shopee, Americanas, Casas Bahia, + 2 pharmacy chains: official API / affiliate API / partner / browser only, terms on automation, lockout risk 1–5 | `data/h8_marketplaces.csv` + top-3 with integration path | T3 adapters, T7 marketplace |
| H9 | What else could create value? (last 60 min) | From H1–H8 data, propose ≤ 5 new value hypotheses ranked by expected value × testable this week, each with its cheapest test | `NEXT.md` | Sunday review; not executed |

## Output contract
Folder `research/2026-10-21/` — committed (public data only):
- `DIGEST.md` ≤ 2 pages: one row per card → number, n, date, confidence tag, sources, "so what" for week 1
- `data/*.csv` · `charts/*.png` (matplotlib, labeled axes, n in the title) · `peers.md` · `h3_signals.md` · `NEXT.md`
- `run.jsonl`: one line per card → model, messages, start, end, status, meter readings

Telegram at launch + 10h: 3 lines + the DIGEST path. No pings before that unless a freeze rule fires.

## Freeze rules
- Paid API spend > $0.50 → freeze, report.
- Weekly meter ≥ 45% → stop cards, write outputs.
- A card exceeds its timebox × 1.5 → stop it, mark `n-d`, continue.
- Login, account creation, purchase or captcha needed → skip that source, mark `n-d`. Never bypass.

## Hard rules
- Public web only. No family data, no chat content. Commit only public-data outputs.
- Every number carries n, date and a tag: [Certain] measured with source · [Likely] inferred · [Guessing].

## Evidence required
- [ ] `research/2026-10-21/DIGEST.md` committed
- [ ] ≥ 6 of 8 cards (H1–H8) with data files; `n-d` allowed and logged
- [ ] `run.jsonl` with per-card model and message counts
- [ ] meter readings at start and end

## Manifest (agent-to-agent)
```json
{
  "goal_id": "2026-10-21-research-01",
  "window": { "start": "at_launch", "duration_h": 10 },
  "quota": {
    "bulk_model": "gpt-6-luna",
    "synthesis_model": "gpt-6.1-sol",
    "synthesis_effort": "medium",
    "fallback_model": "deepseek-v4-flash",
    "weekly_guard_pct": 45,
    "yield_to_build_at_5h_pct": 70,
    "paid_api_cap_usd": 0.5
  },
  "cards": [
    { "id": "H1", "timebox_min": 120, "parallel_ok": true, "out": ["data/h1_offers.csv", "charts/h1_dispersion.png"] },
    { "id": "H2", "timebox_min": 60, "depends": ["H1"], "out": ["data/h2_assurance.csv", "charts/h2_cheapest_risky.png"] },
    { "id": "H3", "timebox_min": 45, "parallel_ok": true, "out": ["h3_signals.md"] },
    { "id": "H4", "timebox_min": 30, "parallel_ok": true, "out": ["data/h4_time.csv"] },
    { "id": "H5", "timebox_min": 75, "parallel_ok": true, "out": ["data/h5_rails.csv"] },
    { "id": "H6", "timebox_min": 30, "parallel_ok": true, "out": ["data/h6_lastmile.csv"] },
    { "id": "H7", "timebox_min": 60, "parallel_ok": true, "out": ["peers.md"] },
    { "id": "H8", "timebox_min": 90, "parallel_ok": true, "priority": 1, "out": ["data/h8_marketplaces.csv"] },
    { "id": "H9", "timebox_min": 60, "depends": ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"], "out": ["NEXT.md"] }
  ],
  "report": { "channel": "telegram", "at": "launch_plus_10h", "max_lines": 3 }
}
```
