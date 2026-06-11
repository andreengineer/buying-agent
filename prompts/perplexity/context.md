# Context — Isaura Project

## What is Isaura

Isaura is a **UHNW purchasing concierge** that answers "Vale Esse Preço?" (Is it worth this price?) — curatorship of price-to-value for luxury goods. NOT price comparison (Buscapé/Zoom).

Target customers: UHNW individuals who value time over savings. They want to know if a product's quality, status, craftsmanship, provenance, and market positioning justify its asking price.

## Current State

| Aspect | Detail |
|--------|--------|
| MVP category | Premium wine (Brazilian market) |
| Tech stack | Node/TypeScript, Express (:3099), Playwright (Claw), Tavily API |
| Data pipeline | Tavily search → price comparison → WhatsApp delivery (Evolution API) |
| KNOWN_STORES | 41 Brazilian wine stores configured |
| Tests | 180/180 PASS, TypeScript clean |
| Budget | $22/month APIs, $200 headroom |
| Runtime | Linux, PM2, Docker (Evolution API, n8n) |

## Pipeline Flow

```
User: "Vale esse preço?" 
  → Tavily search product + price + reviews
  → scrape product images (rate-limited: 3/run)
  → compare across known stores
  → generate valuation report
  → deliver via Telegram/WhatsApp
```

## Known Constraints

- **No Claude API** — Claude (Fable 5) only via browser (claude.ai)
- **No GPT API** — only via browser (chatgpt.com)
- **No vector DB** — no PostgreSQL available for Isaura data
- **Tavily rate-limit** — 3 image searches per pipeline run (race condition P0)
- **premium_ui_broker** — broken for 13 days ($60/mo sunk)
- **Mobile-first** — CEO operates 80% from Android phone

## Fable 5 Sprint

| Metric | Value |
|--------|-------|
| Model | Claude Fable 5 (Mythos-class) |
| Cost | $10/$50 per M tokens |
| Limits remaining | ~9% (resets Sat 8am) |
| First run | Aircraft PoC (10h, 27k ctx) |
| GPT 5.5 free window | +11 days |

## What We Need From This Research

The core IP of Isaura is the **valuation engine** — the logic that determines "is this worth the price?" This research will feed into GPT 5.5 extended thinking, which will generate the prompt for Fable 5 to design the engine.