---
name: spec
description: Contract for family cohort #1 (2026-10-21→27) — intake, sourcing, scorecard, L1/L2/L3 delivery, autonomy A0/A1, ledger. Base while this feature is active.
alwaysApply: true
---

# Spec — Family cohort #1: request → ranked options → purchase

> **Source of truth.** Status: draft — approval = André merging PR `feat/0002-family-cohort-w1`.
> Tier: **architectural** (external marketplaces + payment rails). `design.md` is part of the same PR.

## Summary
A cohort member sends a purchase request in chat; within 10 minutes they get a ranked top-3
in chat, a full scorecard report, and a way to buy — without the agent ever submitting a payment
in week 1.

## Acceptance criteria

### AC-1: request is normalized
- **Given** a cohort member sends a purchase request (text, audio or photo) in the channel
- **When** the message is received
- **Then** a Request (`contracts/request.schema.json`) is stored locally and validates
- **And** the agent asks at most 2 clarifying questions, only for missing required fields
  (`budget_max_brl`, `cep`, or a must-have the category profile requires), within 60 s

### AC-2: one message in, one reply out
- **Given** the bot runs with one poller per token
- **When** 20 test messages are sent in sequence
- **Then** exactly 20 replies are delivered and 0 duplicates are logged

### AC-3: offers are sourced and scored
- **Given** a complete Request
- **When** sourcing runs
- **Then** at least 5 Offers from at least 3 sources are stored, each with `landed_cost_brl`
  (price + shipping to the Request CEP) and seller signals
- **And** each Offer gets a Scorecard row using the category weight profile
- **And** offers failing any assurance check are excluded from the top-3 and listed with the reason

### AC-4: top-3 arrives in chat (L1 + L2)
- **Given** a Scorecard with at least 3 non-excluded rows
- **When** delivery runs
- **Then** the requester receives in chat an L2 text table (rank, total score, landed cost,
  delivery date, seller badge, one-line why) and an L1 9:16 image of up to 6 options
- **And** time from complete Request to L2 is ≤ 10 min (median over the week)

### AC-5: full report (L3)
- **Given** an L2 was delivered
- **Then** an L3 report (PDF attached or web link) shows per-dimension scores, weights,
  evidence links, risks, excluded offers with reasons, and savings vs reference landed cost

### AC-6: purchase at the requester's autonomy level
- **Given** the requester taps "Comprar #N"
- **When** their autonomy level is A0
- **Then** they receive the offer's direct link and an Order is written with `status = link_sent`
- **When** their autonomy level is A1
- **Then** the agent advances checkout up to the payment step and returns a Pix copia-e-cola
  with amount and merchant, writes an Order with `status = pix_ready`, and does not pay

### AC-7: ledger and rating
- **Given** an Order exists
- **When** the requester confirms delivery (or 3 days pass after the delivery date)
- **Then** the agent asks for a 1–5 rating once and stores it in the Order

### AC-8: the agent never moves money in week 1
- **Given** any payment step
- **When** autonomy level is below A2 or the amount exceeds `PIX_CEIL`
- **Then** no payment is submitted by the agent and the attempt is logged

### AC-9: week metrics
- **Given** Sunday 2026-10-25
- **Then** a local `WEEK1.md` reports: requests, answered, purchased, median time-to-L2,
  median savings vs reference, mean rating, duplicates, quota used

## Decision matrix — purchase step

| Autonomy level | Amount vs `PIX_CEIL` | Requester enabled for level | Result | AC |
|---|---|---|---|---|
| A0 | — | — | Direct link; Order `link_sent` | AC-6 |
| A1 | — | yes | Checkout to payment step; Pix copia-e-cola; Order `pix_ready`; no payment | AC-6 |
| A1 | — | no | Fall back to A0 | AC-6 |
| A2 | any | any | Disabled in week 1 → fall back to A1 if enabled, else A0; log | AC-8 |
| any | above | — | No agent payment; log | AC-8 |

## Edge cases and errors
- Fewer than 3 valid offers → deliver what exists, say how many sources were tried, offer to widen budget or deadline.
- Every offer misses the deadline → say so first, then show the earliest delivery.
- Source returns 403/captcha → skip the source, never bypass; count it in the report footer.
- Price changed at checkout (A1) by more than 3% → stop, show old vs new, ask.
- Request outside the week-1 vertical → answer with L2 only and tag `out_of_vertical`.

## Out of scope
- Agent-submitted payments (A2/A3), Pix Automático, recurring purchases.
- Pharmacy and grocery as a vertical (data only, via research).
- Supplier RFQ by email (the UHNW product path).
- Affiliate or cashback revenue (settled: monetization is buy-side only).
- LGPD hardening beyond "family data stays local" — this is freemium discovery.
- WhatsApp as the cohort channel (Telegram in week 1).

## Traceability
- Product: [product.md](./product.md) · Design: [design.md](./design.md) · Tasks: [tasks.md](./tasks.md) · Week plan: [plan.md](./plan.md)
- Contracts: `./contracts/*.schema.json` · Sketch: `./sketch/rfq-flow.html`
- ADR to create if approved: ADR-0002 (autonomy ladder A0–A3 as the payment-delegation model)
