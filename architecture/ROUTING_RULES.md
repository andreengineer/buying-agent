# ROUTING_RULES.md — Model Routing Decision Engine

**Problem this solves:** System was using DeepSeek V4-flash for everything.
Sunk-cost models (Claude Opus, Claude Code, GPT-5 UI) were idle.
API spend <$0.70/day while high-value tasks got cheap treatment.

**Principle:** Match model cost to task value. Expensive models for irreversible decisions only.
Route by task type, not by habit.

---

## Routing table

| Task type | Model | Access | Why | Frequency |
|---|---|---|---|---|
| Nightly goal draft | V4-flash | Hermes/API | routine, fast | daily |
| Quick synthesis, summaries | V4-flash | Hermes/API | cheap, good enough | high |
| Reasoning chain, 2nd opinion | DeepSeek R1 | OpenRouter | chain-of-thought | medium |
| Architecture decision | **Opus 4.8 extended** | Claude UI (sunk) | max reasoning, irreversible | low |
| Code review + implementation | **Claude Code** | local (sunk) | specialized, full context | daily |
| Market research, live data | Perplexity Pro | browser (sunk) | live web | as-needed |
| Vision, image pipeline | Gemini 2.5 Flash | OpenRouter | cheap vision | as-needed |
| Structured data, deep tech | Gemini 2.5 Pro | OpenRouter/browser | deep analysis | medium |
| Long context filter/compress | Kimi K2 | OpenRouter | 128k context cheap | spread only |
| Strategic board report | **Opus 4.8 extended** | Claude UI (sunk) | chairman-level | per cycle |
| Competitor pricing | Perplexity Pro | browser (sunk) | live BR prices | weekly |
| Execution/deploy plan | V4-flash → Opus review | API + browser | draft cheap, review expensive | per deploy |
| Spread parallel slot | see spread_registry.json | mixed | depends on slot role | per spread |

---

## Routing decision tree (Hermes uses this)

```
Is task routine / low-stakes?
  YES → V4-flash (default)
  NO  ↓

Is task irreversible or strategic?
  YES → Opus 4.8 extended (Claude UI, sunk cost, USE IT)
  NO  ↓

Does task need live web data?
  YES → Perplexity Pro (sunk)
  NO  ↓

Does task need code execution or full workspace context?
  YES → Claude Code (sunk)
  NO  ↓

Does task need deep reasoning chain?
  YES → DeepSeek R1 via OpenRouter
  NO  ↓

Does task need vision or image?
  YES → Gemini 2.5 Flash (OpenRouter, cheap)
  NO → V4-flash
```

---

## Sunk-cost models — use them first

These are PAID subscriptions. Marginal cost = $0. Use them before burning API tokens.

| Model | Subscription | Current usage | Target usage |
|---|---|---|---|
| Claude Opus 4.8 extended | Claude Pro | near zero | strategic decisions, board reports |
| Claude Code | Claude Code | underused | daily implementation, code review |
| GPT-5 UI | ChatGPT Plus | spread only | architecture slots, data model |
| Perplexity Pro | Perplexity | spread only | market research, live prices |
| Gemini Pro UI | Google One | rarely | vision, technical deep-dives |

---

## Token efficiency rules

1. **Draft on cheap, review on expensive.** V4-flash drafts; Opus reviews only if decision is irreversible.
2. **No research without a ship target.** Every research task must name the artifact it unblocks.
3. **Compress before escalating.** Never send raw context to Opus — compress with V4-flash first.
4. **One question per Opus call.** Don't batch unrelated questions into one extended-thinking call.
5. **Claude Code for all implementation.** Not Hermes, not V4-flash. Claude Code has full workspace context.

---

## What bad routing looks like (stop doing this)

- Using V4-flash to generate architecture decisions → use Opus or R1
- Using Opus for nightly goal summaries → use V4-flash
- Running 100M V4-flash tokens/4 days with zero Opus calls → imbalanced
- Doing spread(p;4) for a question answerable in one Opus call → overkill
- Calling OpenRouter when Claude Code + sunk Opus would answer it → waste

---

_Enforced by: Hermes routing check before every task dispatch._
_Owner: Andre. Review if spend pattern doesn't shift within 7 days._
