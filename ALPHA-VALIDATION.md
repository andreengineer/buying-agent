# ALPHA-VALIDATION.md — Stack Validation Prompt for Alpha Launch

**Read this file first if you're a PremiumUI (Claude UI, GPT UI, Perplexity) tasked with validating or auditing the alpha launch stack.**

**Canonical repo:** `https://github.com/andreengineer/buying-agent`

---

## How to use this file

This is a **guided validation prompt** — not a checklist, but a *protocol*.

1. **Read in order.** Each stage depends on the previous one passing.
2. **Open referenced files** from the repo as you go (they contain the actual specs).
3. **Report blockages immediately** — flag anything that isn't green.
4. **If a stage is RED (blocked), repeat the validation after unblocking.**
5. **Only declare ALPHA-GREEN when ALL stages pass.**

---

## Stage 0 — Preflight: Repo & Navigation

- [ ] Repo exists and is accessible: `https://github.com/andreengineer/buying-agent`
- [ ] `CONTEXT_INDEX.md` read — understand where everything lives
- [ ] `BROWSER_LLM_PACKET.md` read — understand how PremiumUI consumes this repo
- [ ] `CLOUD_POLICY.md` read — understand what stays local

> **If repo is unreachable:** fall back to copy-paste packet (see `BROWSER_LLM_PACKET.md`).

---

## Stage 1 — System Services (all must be ON)

Read: [`architecture/ISAURA_SYSTEM_STATE.md`](architecture/ISAURA_SYSTEM_STATE.md)

| Port | Service | Status | Validation command |
|------|---------|--------|--------------------|
| 3099 | Isaura agent | ❓ | `curl localhost:3099/health` → `{status: "ok"}` |
| 8080 | Evolution API (WhatsApp) | ❓ | `curl localhost:8080/instance/connectionState/caju` → OPEN |
| 5678 | n8n | ❓ | `curl localhost:5678/health` → OK |
| 11434 | Ollama | ❓ | `curl localhost:11434/api/tags` → models list |
| 18789 | OpenClaw gateway | ❓ | `curl localhost:18789/health` → OK |
| 22 | SSH | ❓ | `ss -tlnp \| grep ':22'` → LISTEN |

**Validation order (critical):**
1. `/health` on Isaura first — if Isaura is down, nothing else matters
2. Evolution webhook endpoint: `POST http://localhost:3099/webhook/whatsapp` → 200
3. Everything else can be checked in parallel

> ❌ **If any service is DOWN** → block alpha. Fix that service first.

---

## Stage 2 — ENV Keys & Secrets

Read: [`architecture/ISAURA_SYSTEM_STATE.md`](architecture/ISAURA_SYSTEM_STATE.md#env-keys)

| Key | Required for | Status |
|-----|-------------|--------|
| TAVILY_API_KEY | Web search | ❓ |
| GROQ_API_KEY | LLM inference | ❓ |
| TELEGRAM_BOT_TOKEN | Telegram channel | ❓ |
| TELEGRAM_MASTER_ID | Admin alerts | ❓ |
| EVOLUTION_API_KEY | WhatsApp send/receive | ❓ |
| GEMINI_API_KEY | Vision pipeline | ❓ |
| RESEND_API_KEY | **Email delivery** | ❌ **CRITICAL — blocks user email** |
| PPLX_KEY | Research (optional alpha) | ❓ |

**Validation:**
```
grep -E "RESEND_API_KEY" /path/to/isaura/.env
# If empty → BLOCKED. Create Resend account first.
```

**Critical path for ENV:**
1. RESEND_API_KEY is the only **blocking** missing key
2. PERPLEXITY/ANTHROPIC/OPENAI are **not** alpha-blocking (use browser UI instead)

---

## Stage 3 — Module Readiness

Read: Source files at `src/reports/`, `src/channels/`, `src/infra/`, `src/alfa/`

### 3a — Core modules (must compile, must respond)

| Module | File | Function | Validation |
|--------|------|----------|------------|
| Premium comparison | `src/reports/premium-comparison.ts` | WA comparison + PDF | `POST /research/premium` → PDF URL |
| PDF renderer | `src/reports/pdf-renderer.ts` | B&W minimal PDF, 15pt | Check output.pdf has content |
| Image pipeline | `src/reports/image-pipeline.ts` | HD WhatsApp images | `w_800,h_800` confirmed? |
| Email | `src/infra/email.ts` | Resend + Mailgun fallback | `POST /test-email` → inbox |
| Evolution | `src/infra/evolution.ts` | sendText + sendImage + sendMedia | Check sendImage works with HD |
| WhatsApp | `src/channels/whatsapp.ts` | Number sanitizer, quietSend | Extract + send test msg |
| Research webhook | `src/channels/research-webhook.ts` | `POST /research/premium` | Returns 200 with JSON |

### 3b — Alpha buying modules

| Module | File | Function | Validation |
|--------|------|----------|------------|
| Buy handler | `src/alfa/buy-handler.ts` | Parse "quero X até R$Y" + scrape | Test with real query |
| Browser scraper | `src/alfa/browser-scraper.ts` | Playwright marketplace scrape | Run with test product |
| Lucky mode | `src/alfa/lucky-mode.ts` | Pick best deal automatically | Test with scraped results |
| Telemetry | `src/alfa/telemetry.ts` | Log all transactions | SQLite file created? |

### 3c — Core infra

| Module | File | Function | Validation |
|--------|------|----------|------------|
| Concierge router | `src/core/concierge-router.ts` | Intent classification | Shadow mode logging? |
| Router | `src/core/router.ts` | Message routing | Trace a test message path |
| Feature flags | `src/core/feature-flags.ts` | Toggle alpha features | `FEATURE_CONCIERGE_ROUTER_SHADOW` |

**Validation:**
```
# All modules compile
cd /path/to/isaura && npx tsc --noEmit
# Exit code 0 = compile OK
```

> ❌ **If ANY module fails compile** → fix before alpha. No partial compile.
> ⚠️ **image-pipeline.ts** — confirm `w_50,h_50` was changed to `w_800,h_800`

---

## Stage 4 — WhatsApp Integration (the critical user path)

This is the **primary user interface** — every alpha user interacts through WhatsApp.

### 4a — Evolution API instance

| Check | Command | Expected |
|-------|---------|----------|
| Instance exists | `GET /instance/caju` | `{instance: {instanceName: "caju"}}` |
| Connection state | `GET /instance/connectionState/caju` | `"OPEN"` |
| Webhook configured | `GET /instance/webhook/caju` | URL points to `http://172.17.0.1:3099/webhook/whatsapp` |
| QR code expired? | Check connection state | Should be permanently connected |

### 4b — Send pathway

```
WhatsApp user → Evolution API → POST /webhook/whatsapp → Isaura processes → Evolution sendText → User receives
```

**Validation:**
1. `curl -X POST http://localhost:3099/webhook/whatsapp -H "Content-Type: application/json" -d '{"data":{"key":{"remoteJid":"5527999068846@s.whatsapp.net"},"message":{"conversation":"olá"}}}'` → 200
2. Send real WhatsApp message from user's phone → Isaura responds within 30s
3. `tail -f /home/a/hermes-isaura-actions.log` during test → action logged

### 4c — Image send pathway

```
Isaura → sendImage (HD) → Evolution API → WhatsApp user
```

**Validation:**
1. Request a product comparison → check image arrives HD (w_800)
2. Check Evolution API call: `sendImage` with `mediatype: "image"` and URL

> ❌ **WhatsApp send + receive must both work.** No partial WhatsApp.
> ⚠️ If Evolution webhook fails → check `docker logs evolution_api --tail 50`

---

## Stage 5 — Email Integration

| Check | Command | Expected |
|-------|---------|----------|
| Resend configured | `grep RESEND_API_KEY .env` | Present |
| DKIM set up | Resend dashboard | Domain verified |
| Send test | `curl -X POST http://localhost:3099/test-email` | Email arrives inbox |
| Mailgun fallback | `grep MAILGUN .env` | Optional but recommended |

> ❌ **RESEND_API_KEY missing = block.** User cannot receive invoices/receipts.
> ⚠️ Without DKIM → emails go to spam → user doesn't see them → trust broken.

---

## Stage 6 — Domain & DNS (izzza.app)

Read: [`architecture/ISAURA_SYSTEM_STATE.md`](architecture/ISAURA_SYSTEM_STATE.md#domain-decisions)

| Check | Command | Expected |
|-------|---------|----------|
| Domain registered | `whois izzza.app` | Registrar = Cloudflare |
| DNS points to server | `dig izzza.app +short` | Server IP |
| Resend DKIM records | Resend dashboard | TXT records added |
| Cloudflare proxy | `dig izzza.app +short` | Cloudflare IP (if proxied) |

**Implementation order:**
1. Buy domain (Cloudflare Registrar) → **BLOCKING**
2. Add DNS records (A record → server IP)
3. Configure Resend DKIM
4. Test email delivery

> ❌ **No domain = no email = no alpha.** This is the first blocking external dependency.

---

## Stage 7 — Compile & Deploy

### 7a — TypeScript compile

```bash
cd /path/to/isaura
npx tsc --noEmit  # Check types ONLY
npm run build      # Full build
```

### 7b — PM2 deployment

```bash
pm2 list
# Expected: isaura running, uptime > 0
pm2 logs isaura --lines 50 --nostream
# Check for error messages
```

### 7c — Git state

```bash
git branch
# Expected: hermes-alfa (or release/alpha-v1)
git status
# Expected: clean working tree
```

### 7d — Release branch

- [ ] `release/alpha-v1` branch created from `hermes-alfa`
- [ ] All uncommitted changes committed or stashed
- [ ] `git log --oneline origin/release/alpha-v1..HEAD` = 0 (up to date)

> ❌ **If compile fails** → fix before alpha. No exceptions.
> ⚠️ Running on `hermes-alfa` branch is fine for alpha — stable branch is nice-to-have.

---

## Stage 8 — End-to-End Smoke Test

**Run this in order. Do not proceed to next step if current step fails.**

### 8.1 — Basic health
```
curl http://localhost:3099/health
# → {"status":"ok","agent":"isaura",...}
```

### 8.2 — Webhook acceptance
```
curl -X POST http://localhost:3099/webhook/whatsapp \
  -H "Content-Type: application/json" \
  -d '{"data":{"key":{"remoteJid":"5527999068846@s.whatsapp.net"},"message":{"conversation":"quero um fone bluetooth até R$ 150"}}}'
# → 200, JSON response
```

### 8.3 — Research API
```
curl -X POST http://localhost:3099/research/premium \
  -H "Content-Type: application/json" \
  -d '{"product":"fone bluetooth","budget":150}'
# → 200, comparison results
```

### 8.4 — PDF generation
```
curl -X POST http://localhost:3099/research/premium/pdf \
  -H "Content-Type: application/json" \
  -d '{"product":"fone bluetooth","budget":150}' \
  -o /tmp/test-comparison.pdf
file /tmp/test-comparison.pdf
# → PDF file, not empty
```

### 8.5 — WhatsApp real send (MANUAL)
```
1. User sends "quero um fone bluetooth até R$ 150" from phone
2. Isaura responds within 30s
3. Response has: product name, price, link, photo (HD)
4. User can ask follow-up: "tem mais barato?" → Isaura responds
```

### 8.6 — Email delivery (MANUAL)
```
1. Trigger email from Isaura (e.g., report send)
2. Check recipient inbox
3. NOT in spam folder
```

---

## Stage 9 — Alpha Launch Declaration

### Pass criteria (ALL must be green)

- [ ] **STAGE 1** All services running (Isaura, Evolution, n8n, Ollama, OpenClaw)
- [ ] **STAGE 2** All critical ENV keys present (RESEND_API_KEY the last blocker)
- [ ] **STAGE 3** All modules compile without errors
- [ ] **STAGE 4** WhatsApp send + receive works end-to-end
- [ ] **STAGE 5** Email sending works (Resend + DKIM)
- [ ] **STAGE 6** Domain izzza.app registered + DNS configured
- [ ] **STAGE 7** Code compiled, PM2 running, git clean
- [ ] **STAGE 8** E2E smoke test passed (health → webhook → research → PDF → real WhatsApp)

### Alpha launch = ON when

```
1 real user sends WhatsApp → Isaura responds
Response time < 30s
Zero crashes for 24h
Images delivered in HD (w_800)
```

### If any stage is blocked

```
BLOCKER: [stage name]
REASON: [what's missing]
UNBLOCK PATH: [what needs to happen]
OWNER: [Andre / Hermes / External]
```

---

## Implementation Order (condensed critical path)

```
1. 🏆 BUY izzza.app                 ← Andre, 5min, cloudflare.com
2. 🌐 DNS → Cloudflare              ← Andre, 10min
3. 📧 Resend account + DKIM         ← Andre, 15min
4. 🔑 RESEND_API_KEY → .env         ← Hermes, 2min
5. 📱 Z-API trial (optional)        ← Andre, 30min (test first!)
6. ⚙️ image-pipeline: w_50→w_800    ← Hermes/Claude Code, 10min
7. 💾 SQLite cache for Gemini Vision ← Hermes, 15min
8. 🔄 PM2 restart after .env update  ← Hermes, 2min
9. 🧪 Run ALL Stage 8 smoke tests    ← Hermes + Andre
10. 🚀 Onboard first user            ← Andre
```

**Do NOT skip steps. Do NOT reorder. Each step unblocks the next.**

---

## Appendix A — Quick commands

```bash
# Health check
curl localhost:3099/health

# Check Evolution webhook
curl -s localhost:8080/instance/caju | python3 -m json.tool | grep -A5 webhook

# Test WhatsApp webhook endpoint
curl -X POST localhost:3099/webhook/whatsapp -H "Content-Type: application/json" -d '{}' -w "\nHTTP %{http_code}\n"

# Follow action log
tail -f /home/a/hermes-isaura-actions.log

# Check PM2
pm2 list
pm2 logs isaura --lines 20 --nostream

# TypeScript compile check
cd /path/to/isaura && npx tsc --noEmit

# Git status
git log --oneline -5
```

## Appendix B — Rollback triggers

Stop alpha and roll back if:
- Any WhatsApp message is **lost** (Isaura doesn't respond)
- Any API key is **exposed** in logs or repo
- Email sending fails completely (>3 attempts)
- Response time > 60s for 3+ consecutive messages
- Evolution API connection drops (instance closes)

---

*Generated for: Andreengineer/buying-agent · Alpha launch validation protocol*
*PremiumUI: read this file from the GitHub repo, not from local storage.*