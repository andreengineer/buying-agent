# ISAURA_SYSTEM_STATE.md — Live System Snapshot

**Last updated:** 2026-06-03  
**Source:** Hermes live system scan + context.json

---

## Services

| Port | Service | Status | Notes |
|---|---|---|---|
| 3099 | Isaura agent | ON | branch hermes-alfa |
| 8080 | Evolution API (WhatsApp) | ON | instance: caju, OPEN |
| 5678 | n8n | ON | workflow automation |
| 11434 | Ollama | ON | local LLM inference |
| 18789 | OpenClaw gateway | ON | Claw execution arm |
| 18791 | OpenClaw internal | ON | auth required |
| 22 | SSH | ON | remote access |

---

## WhatsApp

- **Instance:** caju (profileName: Compras, owner: 5527992228547)
- **Webhook:** `http://172.17.0.1:3099/webhook/whatsapp` ✅ fixed 2026-06-02
- **Previous bug:** webhook was pointing to n8n:5678 instead of Isaura:3099 — fixed

---

## ENV keys

| Key | Status |
|---|---|
| TAVILY_API_KEY | ✅ present |
| GROQ_API_KEY | ✅ present |
| TELEGRAM_BOT_TOKEN | ✅ present |
| TELEGRAM_MASTER_ID | ✅ present |
| EVOLUTION_API_KEY | ✅ present |
| GEMINI_API_KEY | ✅ present |
| RESEND_API_KEY | ❌ missing — blocks email |
| PERPLEXITY_API_KEY | ❌ missing |
| ANTHROPIC_API_KEY | ❌ missing (not needed — use UI) |
| OPENAI_API_KEY | ❌ missing (not needed — use UI) |

---

## Modules (src/)

| File | Status | Function |
|---|---|---|
| reports/premium-comparison.ts | ✅ ready | WA comparison + PDF premium |
| reports/pdf-renderer.ts | ✅ ready | B&W minimal, 15pt font, images embedded |
| reports/image-pipeline.ts | ⚠️ needs fix | w_50→w_800 for HD WhatsApp |
| infra/email.ts | ✅ ready | Resend primary + Mailgun fallback |
| infra/evolution.ts | ✅ ready | sendText + sendImage + sendMedia |
| channels/whatsapp.ts | ✅ ready | extractNumber sanitizer, quietSendText |
| channels/research-webhook.ts | ✅ ready | POST /research/premium, /research/premium/pdf |

---

## Domain decisions

- **izzza.app** — available, ~R$30/yr, Cloudflare Registrar — RECOMMENDED
- **izzza.ai** — ~$60-90/yr, verify availability — skip for alpha
- **Email:** isabel@izzza.app (cleaner than isabel_compras@)

---

## WhatsApp provider strategy

| Provider | Cost | Status | Role |
|---|---|---|---|
| Evolution API | $0 | ✅ running | primary (working) |
| Z-API | R$89/mo | not configured | premium fallback |
| Meta Cloud API | $0-15/mo | not configured | alternative |

---

## Hardware

| Device | Status | Notes |
|---|---|---|
| Desktop i7 | main server | always on |
| Dell Latitude 7750 | functional | bad battery, ugly |
| iPhone 7 | legacy | — |
| Claro SIM | new | use as hotspot if needed |

---

## Budget

- Fixed monthly: $22/mo (UI subs + API)
- Headroom: $200
- New costs estimated: ~R$92/mo ($18) — WITHIN fixed budget
  - izzza.app: R$2.50/mo
  - Z-API: R$89/mo
  - Resend: $0
- Current API spend: <$0.70/day (problem: sunk models idle, V4-flash doing everything)

---

## Git state (as of 2026-06-02)

- Branch: `hermes-alfa`
- Commits pending merge: 6e45c18 ← f86eea7 ← 464830d ← eaea721 ← 31e0e0b
- Release branch target: `release/alpha-v1`
