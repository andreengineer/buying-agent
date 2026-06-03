# SPREAD_ARCHITECTURE.md — Multi-Model Spread Specification

**Status:** Browser-UI spread is ACTIVE. API spread is FUTURE (ROI-gated).
**Owner:** Hermes (Chairman) decides mode and depth per task.

---

## Notation

```
spread(MODE; DEPTH)

MODE:
  l  = linear  — sequential chain, each step compresses+critiques prior
  p  = parallel — simultaneous, Opus chairman converges outputs

DEPTH:
  integer N = use top-N models from the ranked registry below
```

### Examples

| Call | Meaning |
|---|---|
| `spread(l;5)` | Linear chain, top 5 strongest available models |
| `spread(l;3)` | Linear: R1 → Gemini 2.5 Pro → DeepSeek V3.2 |
| `spread(p;4)` | Parallel: Manus + Gemini + GPT + Perplexity → Opus |
| `spread(p;2)` | Parallel: GPT → DeepSeek only (quick, cheap) |
| `spread(l;1)` | Not a spread — just a single model call |

---

## Model Registry — Ranked by Strength

Rank 1 = strongest. Hermes selects top-N by this order.

| Rank | Model | Mode compat | Access | Cost tier | Notes |
|---|---|---|---|---|---|
| 1 | Claude Opus 4.7/4.8 | l+p (chairman only) | Browser UI (Pro) | sunk | Always last in linear, always converges parallel |
| 2 | GPT-5 | l+p | Browser UI | sunk | Best architecture + data lake reasoning |
| 3 | Gemini 2.5 Pro | l+p | API (GEMINI_KEY) + Browser | $1.25/$10 /1M | Vision, deep thinking |
| 4 | DeepSeek R1 | l | API (DEEPSEEK_KEY) | $0.55/$2.19 /1M | Chain-of-thought, reasoning dense |
| 5 | Kimi K2 | l+p (filter) | API (KIMI_KEY) | $0.55/$2.19 /1M | Long context, cheap filter |
| 6 | DeepSeek V3.2 | l+p | API (DEEPSEEK_KEY) | $0.27/$0.41 /1M | Fast, cheap, good generalizer |
| 7 | Qwen 2.5 72B | l+p | API (QWEN_KEY / Together) | $0.40/$0.40 /1M | BR perspective, backup |
| 8 | Manus | p only | Browser UI | sunk | Execution + deploy pipelines |
| 9 | Perplexity Pro | p only | Browser UI | sunk | Market research, live web |
| 10 | Llama 4 Scout | p only | API (Groq) | ~$0 | Local/fast, low stakes |

**Sunk** = paid subscription already active, marginal cost = $0.

---

## Mode Selection Guide

Hermes uses this to decide:

```
Task type                          → Recommended spread
─────────────────────────────────────────────────────────
Fast cross-validation (breadth)    → spread(p;4)
Architecture decision              → spread(l;3)
Complex strategy, low hallucination→ spread(l;5)
Market research (live data needed) → spread(p;2) + Perplexity slot
Quick gut-check                    → spread(p;2)
Chairman synthesis only            → no spread, direct Opus
Deploy order / execution plan      → spread(p;4) → Opus template
```

---

## Linear chain semantics

In `spread(l;N)`:

```
Step 1 [rank 2–N-1, strongest available after Opus]:
  Input:  bare topic
  Output: structured suggestion vector (5–7 points, confidence tagged)

Step 2..N-1 [next ranked models]:
  Input:  COMPRESSED output of all prior steps
  Output: critique + additions + compression
          mark each point [prior|new], drop low-confidence prior points

Step N [Opus, always last]:
  Input:  final compressed chain
  Output: chairman decision — resolves conflicts, final recommendation
```

**Compression rule:** Each non-Opus step must compress prior chain to <50% of input length before adding new points. This prevents hallucination stacking.

---

## Parallel spread semantics

In `spread(p;N)`:

```
All N-1 slots fire simultaneously:
  Each slot receives: same context.json + role-specific prompt
  Roles assigned by Hermes based on model strengths (see registry above)

Opus receives all N-1 outputs:
  Resolves conflicts — Opus decision is final, no vote
  Outputs: final_launch.md or equivalent decision doc
```

**Slot assignment example for spread(p;4):**
- Slot 1 → GPT-5: architecture + data model
- Slot 2 → Gemini 2.5 Pro: visual + technical implementation
- Slot 3 → DeepSeek V3.2: cost analysis + quick wins
- Slot 4 → Perplexity: market + competition

---

## Access paths

### Browser-UI models (current active path)

Requires Marcela or Andre to relay manually.
See: `runbooks/RUNBOOK_browser_spread.md`

Triggered when:
- `spread(p;N)` includes GPT-5, Manus, Perplexity, or Claude UI
- Hermes prints the Marcela packet and waits

### API models (future — ROI-gated)

**NOT default.** Use only when:
1. Task has measurable, quantified ROI that justifies API cost
2. Andre explicitly approves the spend
3. API keys are configured in `.env`

When activated: `tsx hermes-cortex/spread.ts` (parallel) or future `spread_linear.ts`
Cost guard: abort if estimated cost > $3.00 without Andre confirmation.

---

## What Hermes outputs for any spread call

```
# Spread Result — spread(MODE;DEPTH) — TOPIC

Mode: linear/parallel
Depth: N (models used: ...)
Cost: $X.XX estimated / $Y.YY actual (api only)
Access: browser-relay/api/mixed

## Chairman Output (Opus)
[final decision here]

## Raw Steps / Slots
[per-model outputs or Marcela paste confirmations]

## Evidence
[terminal output / paste timestamps / sha256 of output files]
```

---

## What Hermes must NOT do

- Never auto-spend API budget on a spread without ROI justification
- Never start a linear chain without confirming model keys are available
- Never skip Opus as chairman — Opus always converges
- Never expose `.env` keys in spread output files

---

_Spec owner: Andre (CEO). Enforced by: Hermes. Read by: Claw, Claude UI, GPT UI._
