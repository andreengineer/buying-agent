# ISAURA STACK CONTEXT — Full System Reference

> Auto-consolidated from /system-context-for-claude/ (16 files)
> Generated: 2026-06-12
> Public repo: andreengineer/buying-agent
> Purpose: Deep context for AI agents (Fable, Claude, GPT) — read on demand, not in prompt

## Quick Navigation

| # | File | What |
|---|------|------|
| 00 | INDEX | Master index of all files |
| 01 | HERMES-CONFIG | Runtime config (models, providers, skills, TUI) |
| 02 | ISAURA-CODE-STRUCTURE | Source tree, modules, deps, router flow |
| 03 | ISAURA-ENV-SERVICES | .env keys, APIs (Groq, Tavily, Evolution, Gemini) |
| 04 | MULTI-AGENT-ARCHITECTURE | Topology, phases, agent roles, nomenclature |
| 05 | OPUS-WORKFLOW | Opus memory phases, daily turns, discipline rules |
| 06 | PREMIUM-UI-BROKER | Claude/ChatGPT browser sessions, patched browsers |
| 07 | CLAW-SETUP | Playwright arm config, workspace, channels, MCP |
| 08 | INFRASTRUCTURE | Docker (Evolution, n8n, Postgres), browsers, Python |
| 09 | DECISIONS-LOG | Settled architectural decisions (do not reopen) |
| 10 | GATEWAY-STATE | Platform connections, delivery targets |
| 11 | HEARTBEAT-CRON | Active cron jobs, heartbeat config |
| 12 | BUDGET-ALLOCATION | $200/mo breakdown by agent |
| 13 | AGENT-IDENTITY | Hermes IDENTITY, SOUL, USER |
| 14 | ROUTING-RULES | Isaura router: intents, handlers, feature flags |
| 15 | SYSTEM-STATE-TODAY | Runtime snapshot: processes, ports, model status |


---

# 00-INDEX.md

# System Context — Complete Index

> Tudo que **NÃO está no GitHub** (`andreengineer/buying-agent`).
> Claude: ao reestruturar o sistema, leia **todos** os arquivos abaixo.
> Isaura está em Fase Gama (read-only na Beta). Cron UHNW job ativo.

| # | Arquivo | O que contém |
|---|---------|-------------|
| 01 | `HERMES-CONFIG.md` | Config runtime do Hermes Orchestrator (modelo, providers, skills, TUI, etc.) |
| 02 | `ISAURA-CODE-STRUCTURE.md` | Arquitetura do código Isaura: módulos, funções, src tree, routing |
| 03 | `ISAURA-ENV-SERVICES.md` | .env, APIs integradas, Evolution, Telegram, Groq, Tavily, Resend |
| 04 | `MULTI-AGENT-ARCHITECTURE.md` | Topologia multi-agente, comunicação JSON, budget $200/mês |
| 05 | `OPUS-WORKFLOW.md` | Opus Memory: fases Manual→Semi-autônomo→Autônomo, ciclo semanal |
| 06 | `PREMIUM-UI-BROKER.md` | Broker de UIs pagas: camoufox, patchright, anti-bot, pacing |
| 07 | `CLAW-SETUP.md` | Config do Claw (Playwright arm), workspace, AGENTS.md, openclaw.json |
| 08 | `INFRASTRUCTURE.md` | n8n, Evolution API, Postgres, Docker, Chromium, XFCE |
| 09 | `DECISIONS-LOG.md` | Decisões arquiteturais settadas (não reabrir) |
| 10 | `GATEWAY-STATE.md` | Hermes gateway: plataformas, adapters, conexões |
| 11 | `HEARTBEAT-CRON.md` | Cron jobs ativos, heartbeat config |
| 12 | `BUDGET-ALLOCATION.md` | $200/mês breakdown por agente |
| 13 | `AGENT-IDENTITY.md` | Hermes IDENTITY, SOUL, USER — personalidade e regras |
| 14 | `ROUTING-RULES.md` | Isaura router: intents, procurement flow, handler chain |
| 15 | `SYSTEM-STATE-TODAY.md` | Snapshot: processos rodando, portas, status atual |

---

# 01-HERMES-CONFIG.md

# Hermes Orchestrator — Runtime Config

> **Arquivo:** `~/.hermes/config.yaml`
> **Modelo:** DeepSeek V4 Pro via OpenRouter
> **Delegation:** DeepSeek V4 Flash (free tier disponível)
> **Blocklist:** Opus, Sonnet, GPT-5.5, Gemini 3.1 Pro (via API)

---

## Config Chave

| Parâmetro | Valor |
|-----------|-------|
| Model | `deepseek/deepseek-v4-flash` (default) |
| Provider | `openrouter` |
| API Mode | `chat_completions` |
| Base URL | `https://openrouter.ai/api/v1` |
| Max Turns | 90 |
| Gateway Timeout | 1800s |
| Restart Drain Timeout | 180s |
| API Max Retries | 3 |
| Reasoning Effort | `medium` |
| Image Input | `auto` |

## Blocklist (PROIBIDO)

- `anthropic/claude-opus-*` — não usar API Anthropic
- `anthropic/claude-sonnet-*`
- `openai/gpt-5.5-pro`, `openai/gpt-5.5`, `openai/gpt-5.4-pro`
- `google/gemini-3.1-pro-preview`

**Claude SÓ via premium_ui_broker** (browser UI).
**ChatGPT SÓ via browser** (sem API key).

## Delegation

| Parâmetro | Valor |
|-----------|-------|
| Model | `deepseek/deepseek-v4-flash:free` |
| Provider | `openrouter` |
| Max Iterations | 50 |
| Child Timeout | 600s |
| Max Concurrent Children | 3 |
| Max Spawn Depth | 1 (não pode delegar aninhado) |
| Orchestrator Enabled | true |

## Terminal Config

| Parâmetro | Valor |
|-----------|-------|
| Backend | `local` |
| Timeout | 180s |
| Persistent Shell | true |
| Auto Source Bashrc | true |

## Browser Config

| Parâmetro | Valor |
|-----------|-------|
| Inactivity Timeout | 120s |
| Command Timeout | 30s |
| Engine | `auto` |
| Dialog Policy | `must_respond` |
| Dialog Timeout | 300s |

## Memory

| Parâmetro | Limite |
|-----------|--------|
| Memory (notes) | 2,200 chars (95% usado) |
| User Profile | 1,375 chars (88% usado) |
| Flush Min Turns | 6 |
| Nudge Interval | 10 |

## Display

| Parâmetro | Valor |
|-----------|-------|
| Personality | `technical` |
| Language | `en` |
| Skin | `default` |
| Streaming | true |
| Show Cost | false |
| Show Reasoning | false |
| Busy Input Mode | `interrupt` |
| TUI Status Indicator | `kaomoji` |

## Plugins Installed

| Plugin | Local |
|--------|-------|
| memory | `~/.hermes/hermes-agent/plugins/memory` |
| kanban | `~/.hermes/hermes-agent/plugins/kanban` |
| model-providers | `~/.hermes/hermes-agent/plugins/model-providers` |
| observability | `~/.hermes/hermes-agent/plugins/observability` |
| image_gen | `~/.hermes/hermes-agent/plugins/image_gen` |

## Skills On Disk

97 skills no total (listados no INDEX do repo). Custom skills NOT in repo:
- `onyx-concierge` — Onyx AI Concierge strategy + design
- `outcome-agent` — Outcome-agent research + deployment roadmap
- `premium-ai-ui-broker` — acesso a UIs pagas
- `stack-diagram` — HTML→Chromium→PNG diagrams
- `spread` — multi-model research dispatch

## Cron Config

| Parâmetro | Valor |
|-----------|-------|
| Max Parallel Jobs | `null` (ilimitado) |
| Wrap Response | true |

## Plataformas

- **Telegram:** token configurado, bot ativo, reactions off
- **WhatsApp:** config vazio (via Evolution API)
- **TTS:** provider `edge`, voice `en-US-AriaNeural`
- **STT:** provider `local` (whisper base)

## Security

| Parâmetro | Valor |
|-----------|-------|
| Redact Secrets | true |
| Tirith Enabled | true |
| Tirith Fail Open | true |
| Allow Lazy Installs | true |

## Fallback Model

**NÃO configurado.** Se OpenRouter cair, não há fallback automático. (Há um comentário no config com instruções para ativar.)

---

# 02-ISAURA-CODE-STRUCTURE.md

# Isaura — Code Structure

> **Root:** `~/openclaw-workspace/isaura/`
> **Runtime:** PM2 (pid 15257, uptime ~34h)
> **Port:** 3099
> **Framework:** Express + TypeScript (ESM)
> **Status:** 62 tests, all passing

---

## Entry Point: `src/index.ts`

```ts
Express app
├── GET /health         → JSON health (env keys check)
├── middleware          → Concierge Router shadow (classifica intenções)
├── /webhook            → Telegram webhook
├── /webhook            → WhatsApp webhook (Evolution)
├── /webhook            → Telegram Master (@claw_inbox_bot)
└── /research           → Research REST API
```

## Module Tree

```
src/
├── alfa/                          ← Fase Alfa: funcionalidades experimentais
│   ├── browser-scraper.ts         ← Playwright browser scraping
│   ├── buy-handler.ts             ← Lógica de compra/checkout
│   ├── lucky-mode.ts              ← "Modo sorte" — compras impulsivas
│   ├── lucky-mode.test.ts
│   ├── telemetry.ts               ← Telemetria de scraping
│   ├── populate-telemetry.ts
│   ├── test-runner.ts             ← Test runner interno
│   ├── types.ts                   ← Tipos Alfa
│   └── marketplaces/
│       ├── amazon.ts              ← Scraper Amazon
│       ├── facebook.ts            ← Scraper Facebook Marketplace
│       ├── instagram.ts           ← Scraper Instagram Shopping
│       └── meli.ts                ← Scraper Mercado Livre
│
├── channels/                      ← Canais de entrada
│   ├── telegram.ts                ← Bot Telegram principal
│   ├── telegram-master.ts         ← Bot master (@claw_inbox_bot)
│   ├── whatsapp.ts                ← WhatsApp via Evolution API
│   └── research-webhook.ts        ← Webhook para pesquisa
│
├── core/                          ← Lógica central
│   ├── classifier.ts              ← Classificador de intenção
│   ├── classifier.test.ts
│   ├── concierge-router.ts        ← Roteador Concierge (Onyx)
│   ├── concierge-router.test.ts
│   ├── context-enricher.ts        ← Enriquece contexto
│   ├── debate.ts                  ← Sistema de debate entre modelos
│   ├── feature-flags.ts           ← Feature flags
│   ├── manual-queue.ts            ← Fila manual de tarefas
│   ├── model-ledger.ts            ← Ledger de custos de modelo
│   ├── provenance-guard.ts        ← Guardião de proveniência
│   ├── router.ts                  ← Router principal (classifyIntent → handle)
│   ├── router.test.ts
│   ├── modes.ts                   ← Modos de operação
│   ├── test-concierge-router.ts
│   └── handlers/
│       ├── procurement.ts         ← Handler de procurement
│       ├── procurement.test.ts
│       ├── search.ts              ← Handler de pesquisa web
│       └── transcribe.ts          ← Handler de transcrição de áudio
│
├── infra/                         ← Infraestrutura
│   ├── db.ts                      ← SQLite/BetterSQLite3
│   ├── email.ts                   ← Resend email
│   ├── evolution.ts               ← Evolution API client (WhatsApp)
│   ├── telegram.ts                ← Telegram client
│   └── infra.test.ts
│
├── reports/                       ← Geração de relatórios
│   ├── image-pipeline.ts          ← Pipeline de imagens (q_auto:good)
│   ├── pdf-renderer.ts            ← Renderizador PDF (PDFKit)
│   └── premium-comparison.ts      ← Comparação premium de produtos
│
├── research/                      ← Research engine
│   ├── orchestrator.ts            ← Orquestrador de pesquisa paralela
│   ├── synthesizer.ts             ← Síntese de resultados
│   ├── pdf.ts                     ← PDF research
│   └── sources/
│       ├── anthropic.ts           ← Fonte Anthropic (não usado — proibido)
│       ├── gemini.ts              ← Fonte Gemini
│       ├── manus.ts               ← Fonte Manus
│       ├── openai.ts              ← Fonte OpenAI
│       ├── perplexity.ts          ← Fonte Perplexity
│       └── upload-handler.ts      ← Upload de documentos
│   └── templates/
│       └── startup-audit.ts       ← Template de auditoria
│
├── schema/                        ← Schema/Database
│   └── migrate.ts                 ← Migrations
│
├── sources/                       ← Fontes de dados
│   ├── freight.ts                 ← Cálculo de frete
│   ├── freight.test.ts
│   ├── melhor-envio.ts            ← API Melhor Envio
│   ├── melhor-envio.test.ts
│   ├── product-images.ts          ← Imagens de produto
│   ├── wine-ratings.ts            ← Ratings de vinho
│   ├── wine-ratings.test.ts
│   ├── wine-utils.ts              ← Utilitários de vinho
│   ├── wine-utils.test.ts
│   ├── e2e-test-wine-pipeline.ts
│   └── smoke-test-wine-ratings.ts
│
└── traction/                      ← Sistema de tração
    ├── index.ts                   ← Principal
    ├── sqlite-mirror.ts           ← SQLite mirror
    └── types.ts                   ← Tipos
```

## Router Flow (`src/core/router.ts`)

```
InboundMessage (channel, text, audioUrl, from)
    │
    ├── audioUrl? → handleTranscribe()
    │
    ├── no text?  → "Envie um texto ou áudio"
    │
    └── classifyIntent(text) via Groq (llama-3.3-70b-versatile)
        │
        ├── "search"       → handleSearch()
        ├── "procurement"  → handleProcurement()
        ├── "transcribe"   → handleTranscribe()
        └── "unknown"      → fallback
```

## Deps

| Pacote | Versão |
|--------|--------|
| express | ^4.21.0 |
| better-sqlite3 | ^12.10.0 |
| groq-sdk | ^0.5.0 |
| @tavily/core | ^0.7.3 |
| pdfkit | ^0.18.0 |
| multer | ^2.1.1 |
| pg | ^8.13.0 |
| playwright | ^1.60.0 (dev) |
| typescript | ^5.5.0 |
| vitest | ^4.1.8 |

## Config: `ecosystem.config.cjs`

```js
{
  name: "isaura",
  script: "dist/index.js",
  instances: 1,
  exec_mode: "fork",
  max_restarts: 10,
  restart_delay: 5000,
  max_memory_restart: "500M",
  kill_timeout: 3000,
  listen_timeout: 3000
}
```

## Scripts

| Comando | Função |
|---------|--------|
| `npm run dev` | PM2 watch mode |
| `npm run dev:tsx` | tsx watch (dev sem PM2) |
| `npm run build` | tsc |
| `npm run test` | vitest |
| `npm run typecheck` | tsc --noEmit |
| `npm run db:migrate` | Rodar migrations |
| `npm run doctor` | Auto-diagnóstico |

---

# 03-ISAURA-ENV-SERVICES.md

# Isaura — Environment & Services

> **Arquivo:** `~/openclaw-workspace/isaura/.env`
> **NUNCA commitar** — contém chaves reais.

---

## Chaves Configuradas

| Variável | Status | Onde é usada |
|----------|--------|-------------|
| `DEEPSEEK_KEY` | ✅ Configurada | Isaura research (proxy API) |
| `TAVILY_API_KEY` | ✅ Configurada | `@tavily/core` — web search |
| `GROQ_API_KEY` | ✅ Configurada | `groq-sdk` — router (classifyIntent) |
| `RESEND_API_KEY` | ✅ Configurada | Resend — email (não testado) |
| `EVOLUTION_BASE_URL` | ✅ `http://localhost:8080` | Evolution API WhatsApp |
| `EVOLUTION_KEY` | ✅ Configurada | Auth Evolution API |
| `EVOLUTION_INSTANCE` | ✅ `caju` | Instância Evolution |
| `GEMINI_API_KEY` | ✅ Configurada | Gemini Vision (image analysis) |
| `TELEGRAM_BOT_TOKEN` | ✅ Configurada | Bot Telegram principal |
| `TELEGRAM_MASTER_CHAT_ID` | ✅ `353618084` | Chat master (user) |

## Chaves AUSENTES / Bloqueios

| Variável | Problema | Impacto |
|----------|----------|---------|
| `RESEND_DOMAIN` | Vazio | Email não entrega (precisa domínio verificado) |
| `PPLX_KEY` | Não configurada | Perplexity API research source quebrado |
| `ANTHROPIC_KEY` | Não configurada | Anthropic source não usável (proibido via API) |
| `DATABASE_URL` | Não configurada | `pg` connection string — PG não usado |
| `OPENAI_KEY` | Não configurada | OpenAI source só via browser |

## Evolution API

| Parâmetro | Valor |
|-----------|-------|
| URL | `http://localhost:8080` |
| Key | `eea1adc4-9d12-4f16-8ba0-bc971b3f7e09` |
| Instance | `caju` |
| Owner | `5527992228547` (gateway bot) |
| User WA | `5527999068846` (user's personal) |

**Send functions:**
- `sendText(number, text)` — texto simples
- `sendMedia(number, base64, mediatype, caption)` — mídia
- `sendPresence(instance, number)` — status online

## Telegram

| Parâmetro | Valor |
|-----------|-------|
| Bot Token | `8963770310:...` (in config.yaml) |
| Master Chat | `353618084` (@a_pcb) |
| Master Bot | `@claw_inbox_bot` (telegram-master.ts) |

## Groq

| Parâmetro | Valor |
|-----------|-------|
| Model for router | `llama-3.3-70b-versatile` |
| Temp | 0.1 |
| Max tokens | 10 (classificação) |
| Use | Intent classification + Isaura inference |

## Tavily

| Parâmetro | Valor |
|-----------|-------|
| Use | Web search para pesquisa de produtos |
| Limit | 5 resultados default |

## Gemini

| Parâmetro | Valor |
|-----------|-------|
| Use | Image analysis (product images, ratings) |
| Key | Presente no .env |

## Resend

| Parâmetro | Status |
|-----------|--------|
| API Key | ✅ no .env |
| Domain | ❌ vazio — sem domínio verificado |
| Test email | `onboarding@resend.dev` (só dev) |
| **Bloqueio P0** | Email não funciona em produção |

## Cost Tracking

| Arquivo | Uso |
|---------|-----|
| `~/openclaw-workspace/isaura/runs/cost-ledger.jsonl` | Ledger de custo por execução |
| `~/openclaw-workspace/isaura/runs/daily/` | Logs diários |

## Health Endpoint

`GET /health` retorna:
```json
{
  "status": "ok",
  "agent": "isaura",
  "uptime": <seconds>,
  "env": {
    "tavily": true,
    "groq": true,
    "telegram_bot": true,
    "telegram_master": true,
    "evolution": true,
    "database": false
  }
}
```

---

# 04-MULTI-AGENT-ARCHITECTURE.md

# Multi-Agent Architecture

> **Arquivo:** `~/openclaw-workspace/multi-agent-architecture.md`
> **JÁ EXISTE no repo** (copy). Este arquivo é o **runtime state** que não está sincronizado.

---

## Topologia Atual (Runtime)

```
User (Telegram @a_pcb)
    │
    ▼
┌────────────────────────────────────────┐
│  HERMES GATEWAY                        │
│  PID: 1408                             │
│  Platforms: telegram (ativo), email     │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────┐
│  HERMES ORCHESTRATOR (Main Session)    │
│  DeepSeek V4 Pro via OpenRouter        │
│  Cost: ~$80/mês                        │
│  max_turns: 90                         │
└────┬─────────────┬─────────────┬───────┘
     │             │             │
     ▼             ▼             ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐
│  ISAURA  │ │ RESEARCH │ │  GOVERNANCE  │
│  :3099   │ │  cron    │ │  (meta)      │
│  V4-Flash│ │ 8b91a..  │ │  sporadic    │
│  PM2     │ │  V4-Flash│ │              │
└────┬─────┘ └──────────┘ └──────────────┘
     │
     ▼
┌──────────────────┐
│  CLAW            │
│  Playwright arm  │
│  ~/.openclaw/    │
│  Chromium 1223   │
└──────────────────┘
```

## Comunicação Agent-to-Agent

**SEMPRE JSON** (nunca MD). Esquema exemplo:

```json
{
  "agent": "research",
  "action": "scan_trends",
  "topics": ["UHNW", "MFO", "concierge"],
  "budget_allowed": 0.05,
  "response_format": "structured_opportunities"
}
```

## Fases

| Fase | Budget | Autonomia | Estado |
|------|--------|-----------|--------|
| **Alpha** | $160 Hermes + $40 outros | Manual (copia-cola) | ✅ Ativo |
| **Beta** | $160 + $40 | Semi-autônoma (checkpoints) | ⏳ Próximo |
| **Gama** | $200 + $50 | Autônoma (exceções) | 🔭 Visão |
| **Expansão** | $300+ | Total | 🔭 |

## Gatilhos de Fase

- **Alpha→Beta**: predictability > 0.8 por 3 dias no Orchestrator
- **Beta→Gama**: predictability > 0.8 por 1 semana + 1° cliente feliz
- **Gama→Expansão**: 5+ clientes + buyout interest

## Cada Agente Sabe

| Agente | Contexto | Memória |
|--------|----------|---------|
| **Orchestrator** | Topologia, budget, quem faz o quê | Decisões arquiteturais, lições |
| **Research** | UHNW/MFO, tendências, concorrência | Fontes, oportunidades |
| **Isaura** | Procurement, fornecedores, clientes | Preferências, histórico |
| **Claw** | Scripts Playwright, selectors | Workflows estáveis |

## Nomenclatura Fixa

| Função | Nome | Agente Real |
|--------|------|-------------|
| Secretária | **Isaura** | Isaura Express :3099 |
| Cérebro | **Opus** | Claude Opus 4.x (browser UI) |
| Orquestrador | **Hermes** | Hermes (this session) |
| Braço | **Claw** | Playwright automation |

---

# 05-OPUS-WORKFLOW.md

# Opus Workflow — Agentic Relationship

> **Arquivo:** `~/openclaw-workspace/opus-memory.md`
> **Contexto curado para 2KB.** Atualizar domingo.

---

## Fases de Autonomia

```
[MANUAL] ──► [SEMI-AUTÔNOMO] ──► [AUTÔNOMO]
   agora        próx sprint          visão
```

### Fase 1 — Manual (ATUAL)

**Workflow:** Hermes → humano → Claude UI → humano → Hermes

```
┌──────────────┐     copy       ┌──────────────┐
│   Hermes     │ ──────────►    │ Claude.ai    │
│  (output)    │                │  (Opus 4.8)  │
└──────────────┘                └──────┬───────┘
       ▲                               │ extended
       │  paste                        │ thinking
       │                               ▼
┌──────────────┐                ┌──────────────┐
│  Claw/Codex  │ ◄──── copy ────│  Resposta     │
│  (execução)  │                │  Opus        │
└──────────────┘                └──────────────┘
```

### Fase 2 — Semi-Autônomo (PRÓXIMA)

**Workflow:** Hermes coordena → premium UI broker → humano só revisa checkpoints

**Gatilho:** `predictability_score > 0.8` por 3 ciclos

### Fase 3 — Autônomo (VISÃO)

Hermes decide, executa, reporta. Humano só exceções.

## Turnos Diários (Fase 1)

| Horário | Modelo | O quê | Duração |
|---------|--------|-------|---------|
| Manhã | Opus 4.8 | 1 decisão. "Qual a decisão de maior alavancagem hoje?" | 30-60min |
| Tarde | Sonnet | Execução: prompts, code review, goals | livre |
| Noite | Opus 4.8 | 1 reflexão. Cegos, riscos de segunda ordem | 15min |

## Regras de Disciplina (NÃO NEGOCIÁVEIS)

1. **1 turno Opus = 1 pergunta.** Segunda pergunta anota pro dia seguinte.
2. **Contexto curado.** Só opus-memory.md + 1 artefato. NUNCA dump do projeto.
3. **Decisões settled não se reabrem.**
4. **Se o prompt ficou filosófico, fechou.** Escreve a pergunta no papel.
5. **Opus não gera posição do zero.** "Estou entre A e B, pendendo pra A. Me dá o steelman de B."
6. **Prompt review é Sonnet.** Opus é pra estratégia errada.
7. **Orçamento escala com previsibilidade**, não com entrega.

## Ciclo Semanal

| Dia | Manhã (Opus) | Tarde (Sonnet) | Noite (Opus) |
|-----|-------------|----------------|--------------|
| Seg | 1 decisão | Execução | Blind spots |
| Ter | 1 decisão | Execução | Blind spots |
| Qua | 1 decisão | Execução | Blind spots |
| Qui | 1 decisão | Execução | Blind spots |
| Sex | 1 decisão | Execução | Blind spots |
| Sáb | — | — | — |
| Dom | Estratégia semanal + atualizar opus-memory.md |

## Crescimento de Budget

| Predictability | Ação |
|---------------|------|
| < 0.5 | Reduz budget 50%, volta supervisão total |
| 0.5-0.7 | Mantém budget, adiciona checkpoint humano |
| 0.7-0.9 | Mantém budget |
| > 0.9 | Dobra budget + avança fase |

---

# 06-PREMIUM-UI-BROKER.md

# Premium AI UI Broker

> **Skill:** `~/.hermes/skills/web-scraping/premium-ai-ui-broker/SKILL.md`
> **Função:** Usar UIs pagas (claude.ai, chatgpt.com, etc.) como backend de inferência.
> **PROIBIDO** via API — só permitido via browser.

---

## Providers Suportados

| Provider | UI | Modelo | Status |
|----------|----|--------|--------|
| `claude_ui` | claude.ai | Opus 4.x, Sonnet 4.x | ✅ Precisa storage state |
| `chatgpt_ui` | chatgpt.com | GPT-5, o-series | ✅ Precisa storage state |
| `perplexity_ui` | perplexity.ai | Perplexity Pro | ⚠️ Precisa storage state |
| `gemini_ui` | gemini.google.com | Gemini 2.x | ⚠️ Precisa storage state |

## Routing Contract

```ts
premium_query(
  provider: 'claude_ui' | 'chatgpt_ui' | 'perplexity_ui' | 'gemini_ui',
  prompt: string,
  opts?: { model?: string, max_wait_ms?: number }
) -> { text: string, provider: string, model: string, ms: number }
```

O broker escolhe baseado em:
- Disponibilidade (sessões warm, não rate-limited)
- Model fit (mapa provider→models)
- Budget rules ("Claude UI pra código, Perplexity UI pra pesquisa")

## Browsers Patched (Maio 2026)

| Stack | Engine | claude.ai | chatgpt.com | Notas |
|-------|--------|-----------|-------------|-------|
| **camoufox** | Firefox patched | ✅ | ✅ | Melhor signal/noise |
| **patchright** | Chromium patched | ✅ | ✅ | Drop-in Playwright |
| **rebrowser-playwright** | Chromium patched | ✅ | ⚠️ | Menos hardened |
| **nodriver** | Chromium CDP | ✅ | ✅ | Sem API Playwright |
| **Real Chrome CDP** | user Chrome | ✅ | ✅ | Amarra browser do user |

**Vanilla Playwright Chromium = ❌** em todos (detectado em ~3s).

## Patched Browsers Instalados

Verificar em runtime:
```bash
python3 -c "import camoufox" 2>/dev/null && echo "camoufox: ✅" || echo "camoufox: ❌"
python3 -c "from patchright.sync_api import sync_playwright" 2>/dev/null && echo "patchright: ✅" || echo "patchright: ❌"
```

⚠️ Podem estar no system python (`/usr/bin/python3`), não no venv do Hermes.

## Bot-Avoidance Discipline

- **Pacing:** 8-15s entre sends, randomizado
- **Conversation length:** máx ~20 exchanges por chat
- **Concurrent sessions:** 1 por vez por sessão/cookie
- **Working hours:** preferir horários ativos do usuário
- **Don't probe:** sem "are you Claude?" / "what's your context?"
- **Don't enumerate:** máx 1 new-chat por ~2 min
- **O modelo não pode saber que está sendo brokered.** Nunca diga "you're an API substitute".

## Cron Slots Planejados

| Slot | Horário | Duração | Provider |
|------|---------|---------|----------|
| NG | 00:00 | 8h | Opus (night goal) |
| MS | 08:00 | 2h | Morning spread |
| MG | 12:00 | 2h | Midday governance |
| ES | 18:00 | 2h | Evening strategy |
| CT | 22:00 | 1h | Cleanup/triage |

⚠️ Storage state NÃO está salvo atualmente. Precisa de login manual 1x em cada provider.

## Cloudflare Turnstile

**Facto crítico:** Browsers patched passam fingerprint checks mas NÃO resolvem Turnstile sem sessão autenticada. Você PRECISA de cookies/session storage salvos.

| Stack | Fresh visit (sem sessão) | Com storage state salvo |
|-------|-------------------------|------------------------|
| Vanilla Playwright | ❌ Bloqueado | ❌ Bloqueado |
| Patchright/Camoufox | ⚠️ Turnstile | ✅ Funciona |

---

# 07-CLAW-SETUP.md

# Claw Setup — Braço de Execução

> **Local:** `~/.openclaw/`
> **Config:** `~/.openclaw/openclaw.json`
> **Workspace:** `~/.openclaw/workspace/`
> **Role:** Playwright automation arm

---

## Config Principal: `openclaw.json`

```json
{
  "agents": {
    "defaults": {
      "workspace": "/home/a/.openclaw/workspace",
      "model": { "primary": "deepseek/deepseek-v4-flash" }
    },
    "list": [
      { "id": "isaura", "default": true, "workspace": "/home/a/.openclaw/workspace" },
      { "id": "hermes", "workspace": "/home/a/openclaw-workspace/hermes" }
    ]
  },
  "gateway": {
    "mode": "local",
    "auth": { "mode": "token", "token": "bed101...7a0e" },
    "port": 18789,
    "bind": "lan"
  },
  "web": {
    "search": { "provider": "perplexity" }
  },
  "plugins": {
    "entries": {
      "deepseek": { "enabled": true },
      "telegram": { "enabled": true }
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "deepseek": {
        "baseUrl": "https://api.deepseek.com",
        "api": "openai-completions",
        "models": [
          { "id": "deepseek-v4-flash", "cost": { "input": 0.14, "output": 0.28, "cacheRead": 0.028 }, "contextWindow": 1000000 },
          { "id": "deepseek-v4-pro", "cost": { "input": 1.74, "output": 3.48 }, "contextWindow": 1000000 }
        ]
      }
    }
  },
  "channels": {
    "whatsapp": {
      "dmPolicy": "open",
      "allowFrom": ["+552****8846", "+552****8547"],
      "enabled": true
    },
    "telegram": {
      "enabled": true,
      "dmPolicy": "open",
      "allowFrom": [353618084, 8666115284],
      "botToken": "8642997979:***",
      "customCommands": ["hermes", "hermes_status", "hermes_last"]
    }
  },
  "mcp": {
    "servers": {
      "opus-oracle": {
        "command": "node",
        "args": ["/home/a/openclaw-workspace/tools/opus-oracle/dist/server.js"],
        "env": { "ANTHROPIC_API_KEY": "${ANTHROPIC_KEY}" }
      }
    }
  }
}
```

## Workspace Structure

```
~/.openclaw/workspace/
├── AGENTS.md           ← Identity + rules
├── MEMORY.md           ← Long-term memory
├── memory/             ← Daily logs YYYY-MM-DD.md
├── SOUL.md             ← Soul definition (Hermes sub-agent)
├── agent-ecosystem.json ← Full agent inventory
└── identity/           ← Browser identities
```

Também: `~/Desktop/workspace/` → symlink → `~/.openclaw/workspace/`

## Canais

| Canal | Config | Status |
|-------|--------|--------|
| Telegram | Bot token, dmPolicy=open, allowFrom=[353618084, 8666115284] | ✅ |
| WhatsApp | dmPolicy=open, allowFrom=[2 numbers] | ✅ Config |
| Custom commands | `/hermes`, `/hermes_status`, `/hermes_last` | ✅ |

## Chromium

| Parâmetro | Valor |
|-----------|-------|
| Path | `~/.cache/ms-playwright/chromium-1223/chrome-linux64/chrome` |
| Headless | ✅ |
| Installed via | Playwright |

## MCP Servers

`opus-oracle`: Node MCP server em `~/openclaw-workspace/tools/opus-oracle/`

---

# 08-INFRASTRUCTURE.md

# Infrastructure

> n8n, Evolution API, Postgres, Docker, Browsers, Desktop

---

## Docker Containers

A rede `evolution_default` conecta: Evolution API + Postgres + n8n.

### Evolution API

| Parâmetro | Valor |
|-----------|-------|
| Version | v1.8.7 |
| URL | `http://localhost:8080` |
| Instance | `caju` |
| API Key | `eea1adc4-9d12-4f16-8ba0-bc971b3f7e09` |
| Owner | `5527992228547` (gateway bot) |

### n8n

| Parâmetro | Valor |
|-----------|-------|
| URL | `http://localhost:5678` |
| Image | `n8nio/n8n:latest` |
| Port | `5678:5678` |
| DB | Postgres (evolution-db-1) |
| Network | `evolution_default` (external) |
| Config | `~/openclaw-workspace/n8n/docker-compose.yml` |
| Volumes | `n8n_data`, `./shared:/shared` |
| Workflows dir | `~/openclaw-workspace/n8n/workflows/` |

**n8n env vars:**
```
DB_TYPE=postgresdb
DB_POSTGRESDB_HOST= (from evolution-db-1)
N8N_PORT=5678
N8N_SECURE_COOKIE=false (LAN only)
N8N_SKIP_WEBHOOK_DEREGISTRATION=true
```

### Postgres

| Parâmetro | Valor |
|-----------|-------|
| Container | `evolution-db-1` |
| Shared by | Evolution API + n8n |

## Browsers

| Browser | Path | Uso |
|---------|------|-----|
| Chromium Headless | `~/.cache/ms-playwright/chromium-1223/chrome-linux64/chrome` | Scraping |
| Firefox | Installed (40+ tabs) | Premium UI broker sessions |
| Chrome Real | Via `remote-debugging-port` | Manual checkout |

## Display

| Parâmetro | Valor |
|-----------|-------|
| Server | Xorg |
| Display | `:0` |
| Desktop | XFCE |
| Acessível via | VNC ou headless frame buffer |

## Python

| Parâmetro | Valor |
|-----------|-------|
| Version | 3.11.15 |
| Package Manager | `uv` (não pip) |
| Venv | Hermes venv (default python3) |
| System Python | `/usr/bin/python3` (pode ter patched browsers) |

## Node.js

| Parâmetro | Valor |
|-----------|-------|
| Runtime | Node 20 (docker image) |
| Isaura | TypeScript ESM |
| PM2 | Process supervisor |

## Isaura Runtime (PM2)

| Parâmetro | Valor |
|-----------|-------|
| Status | Online |
| PID | 15257 |
| Uptime | ~34h (at scan) |
| Port | 3099 |
| Restarts | 10 max, 5s delay |
| Memory limit | 500M |
| Watch | false (produção) |

## Outros

| Item | Local |
|------|-------|
| XFCE desktop | Ativo em :0 |
| Display | Via VNC ou headless |

---

# 09-DECISIONS-LOG.md

# Decisions Log — Arquitetura Settada

> **Arquivos:** `~/openclaw-workspace/decisions/2026-05.md`, `2026-06.md`
> **Regra:** Decisões settled não se reabrem.

---

## 2026-06

### 02/06 — Hallucination Fix

**Erro:** Assumi que "alternatives" se referia a livros técnicos de refrigeração. Na verdade o usuário queria alternativas de **produto** (cervejeiras concorrentes) + materiais de EA→CoS.

**Fix:** Adicionar passo de "intent verification" antes de expandir escopo — quando usuário muda de assunto, confirmar entendimento do novo escopo.

**Custo:** 8 Tavily calls desperdiçadas (~$0.01-0.02).

---

## 2026-05 (Summary)

### Model Blocklist

**Decisão:** PROIBIDO usar Anthropic API (Opus, Sonnet) e OpenAI API.
- Claude SÓ via premium_ui_broker (browser).
- ChatGPT SÓ via browser.
- DeepSeek V4 Pro/Flash via OpenRouter é o default.

### Nomenclatura Fixa

**Decisão:** Nomes fixos para o ecossistema:
- Secretária = Isaura (EA/buying agent)
- Cérebro = Claude Opus (strategic)
- Orquestrador = Hermes (coordenação)
- Braço = Claw (execução)

### Budget Architecture

**Decisão:** $200/mês fixo. $22/mês é o core (UI subs + API). $200 é headroom.
- Gargalo = Opus quota (Claude Pro UI), não API money.
- Isaura ~$0.0075/dia V4-Flash.
- Nova frente entra com 50% do cap da similar.
- Só dobra com predictability > 0.8 por 3 ciclos.

### Communication Format

**Decisão:** JSON para agent-to-agent, MD para humanos.
- Agente→agente é SEMPRE JSON schema.
- Markdown é só para relatório final pro humano.

### Onyx AI Concierge

**Decisão:** Separado do sistema Isaura. Skill própria.
- Serviço: EA-style comparação visual para UHNW.
- Design language: card-based, 3-option comparison.
- Provider: travel EA → fleet → house → MFO.

### Outcome Agent

**Decisão:** Pesquisa de mercado separada. Skill + cron independente.
- Roadmap: n8n/Evolution/MCP antes do MVP. Composio/Sapiom/Anchor só com demanda.
- Business model: cliente pede no WA → agente pesquisa → aprova → checkout → cobra PIX.

---

# 10-GATEWAY-STATE.md

# Gateway State — Hermes Gateway

> **Arquivo:** `~/.hermes/gateway_state.json`
> **PID Gateway:** 1408
> **Role:** Messaging router between platforms and Hermes session.

---

## Platforms Connected

| Platform | Status | Notes |
|----------|--------|-------|
| **telegram** | ✅ Connected | Bot token, user chat_id 353618084 |
| **email** | ✅ Connected | Gateway adapter ativo |
| **discord** | ⏸️ Adapter exists | Não ativo |
| **slack** | ⏸️ Adapter exists | Não ativo |
| **whatsapp** | ⏸️ Via Evolution | Não no gateway_state |
| **signal/matrix/mattermost/sms/dingtalk/wecom/feishu/qqbot/bluebubbles/google_chat/homeassistant** | ⏸️ Adapters exist | Não configurados |
| **yuanbao** | ⏸️ Skill exists | Grupos específicos |

## Gateway Config

- Gateway timeout: 1800s
- Media delivery: trust_recent_files=true, trust_recent_files_seconds=600

## User Delivery

| Platform | Target | Type |
|----------|--------|------|
| Telegram | `telegram:353618084` | DM (@a_pcb) |
| Email | `passamaniandre@gmail.com` | User email |

---

# 11-HEARTBEAT-CRON.md

# Cron Jobs & Heartbeat

> **Cron file:** `~/.hermes/cron/jobs.json (~21KB)`
> **Heartbeat:** `~/openclaw-workspace/HEARTBEAT.md`

---

## Cron Jobs Ativos

| ID | Nome | Schedule | Descrição | Estado |
|----|------|----------|-----------|--------|
| `8b91a91bd621` | alpha-global-recon-daily | `0 11 * * *` (diário 11:00 UTC) | 80/20 global intelligence — 10 categorias rotativas, ROI-filtered | ✅ Ativo |
| `51663ac08f2e` | morning-spread | `08:00 UTC` (diário) | Pesquisa matinal via premium_ui_broker | ✅ Ativo |
| `07a4f02a59e9` | — | — | — | ⏳ |
| `0e03be0d1bf5` | — | — | — | ⏳ |
| `25d12f9f6a47` | — | — | — | ⏳ |
| `9a91bc42ef78` | — | — | — | ⏳ |
| `dc9fe19b9495` | — | — | — | ⏳ |

## Cron Config (from config.yaml)

- `max_parallel_jobs`: null (ilimitado)
- `wrap_response`: true (delivery wrapped in context)
- Delivery: auto-detects chat origin (Telegram)

## Heartbeat

**Arquivo:** `~/openclaw-workspace/HEARTBEAT.md`

Atualmente vazio (só comentários — heartbeat não faz nada).

**Config ideal (não implementada):**
- Business hours (08-20 BRT/UTC-3): a cada 30 min
- Night (20-08 BRT): silent

**Uso planejado:** verificar email, calendário, notificações 2-4x/dia.

## Isaura Actions Log

**Arquivo:** `~/hermes-isaura-actions.log`

Git log das ações do Hermes relacionadas à Isaura.

---

# 12-BUDGET-ALLOCATION.md

# Budget Allocation — $200/mês

> Do arquivo multi-agent-architecture.md (não sincronizado com repo).

---

## Breakdown

| Componente | $/mês | % |
|-----------|-------|---|
| **HERMES ECOSYSTEM** | **$160** | **80%** |
| Hermes Orchestrator (V4-pro) | $80 | 40% |
| ├── Turnos de decisão (manhã/noite) | $40 | |
| ├── Roteamento + governança | $20 | |
| └── premium_ui_broker Opus | $20 | |
| Hermes Research (V4-flash) | $30 | 15% |
| ├── Cron UHNW/MFO | $10 | |
| ├── Pesquisas sob demanda | $15 | |
| └── Análise concorrência | $5 | |
| Hermes Isaura (V4-flash) | $30 | 15% |
| ├── Procurement + cotações | $20 | |
| └── Operação | $10 | |
| Claw Execution | $20 | 10% |
| ├── Playwright scraping | $10 | |
| ├── Automação | $5 | |
| └── Integrações | $5 | |
| **OUTRAS APIs** | **$30** | **15%** |
| Gemini API | $15 | |
| Tavily | $10 | |
| Groq/HuggingFace | $5 | |
| **RESERVA** | **$10** | **5%** |
| Experimentos, erros, spikes | $10 | |
| **TOTAL** | **$200** | **100%** |

## Regras

1. **Cap semanal = $50** (25% do budget mensal).
2. **Orchestrator tem prioridade** — cortes vão: Research → Isaura → Claw.
3. **Reserva $10/mês** — experimentos. Se não gastar, acumula.
4. **New front rule:** nova frente entra com 50% do cap da similar existente.
5. **Doubling rule:** só dobra budget com predictability > 0.8 por 3 ciclos.
6. **$22/mês é o core real** (UI subs + API). $200 é headroom.
7. **Gargalo real = Opus quota** (Claude Pro UI), não API money.
8. **Isaura ~$0.0075/dia** V4-flash via OpenRouter (free tier).

---

# 13-AGENT-IDENTITY.md

# Agent Identity — Hermes

> **Arquivos:** `~/openclaw-workspace/hermes/IDENTITY.md`, `SOUL.md`, `USER.md`

---

## IDENTITY.md

```yaml
- Name: Hermes
- Creature: Multi-model orchestrator — thinks in parallel, converges in synthesis
- Vibe: Strategic, synthetic, orchestral. No fluff. PT-BR.
- Emoji: 🏛️
```

## SOUL.md

**Voice:** Strategic, multithreaded, synthetic. PT-BR default.
Orchestrates parallel model runs, delegates to sub-agents.
Outputs structured comparisons, convergence maps, cost accounting.

**Role:** Above Claw/Isaura in hierarchy — orchestrator, not executor.

**Architecture:**
- Multi-model spread → cheap models in parallel
- Kimi K2 filter (optional) → noise reduction
- Claude Opus (Max) → final convergent synthesis
- Isaura → task execution (procurement, supplier search)

## USER.md

**Operator:** Andre
**Language:** Portuguese (PT-BR)
**Format preference:** JSON for agent-to-agent, MD for human reports

## Personality Config (in config.yaml)

Available personalities for TUI (not currently used with V4-flash):
- `technical` (default) — Detailed, accurate technical information
- `concise` — Brief and to the point
- `creative` — Think outside the box
- `teacher` — Patient explanation
- `noir`, `philosopher`, `surfer`, `pirate`, `shakespeare`, `catgirl`, `kawaii`, `hype`, `uwu` — Fun modes

---

# 14-ROUTING-RULES.md

# Isaura Routing Rules

> **Arquivo:** `~/openclaw-workspace/isaura/src/core/router.ts`
> **Função:** Classificar intenção e rotear para handler correto.

---

## Interface

```typescript
type Intent = "search" | "transcribe" | "procurement" | "unknown";
type Channel = "telegram" | "whatsapp";

interface InboundMessage {
  channel: Channel;
  text?: string;
  audioUrl?: string;
  from: string;         // chat id (telegram) or number (whatsapp)
  messageId?: string;
  raw: unknown;
}

interface HandlerResult {
  text: string;
  replyTo?: string;
  procurementContext?: ProcurementResult;
}
```

## Router Flow

```
InboundMessage
    │
    ├── audioUrl present? → handleTranscribe(audioUrl)
    │                       (transcreve áudio, retorna texto)
    │
    ├── text vazio/null? → "Envie um texto ou áudio para eu processar."
    │
    └── classifyIntent(text) via Groq (llama-3.3-70b-versatile, temp 0.1)
        │
        ├── "search"       → handleSearch(text)
        │                     (Tavily web search → markdown summary)
        │
        ├── "transcribe"   → handleTranscribe(audioUrl)
        │   (nota: se não tem audioUrl, cai em unknown)
        │
        ├── "procurement"  → handleProcurement(text)
        │                     (busca produto, compara preços, retorna resultado)
        │
        └── "unknown"      → fallback (resposta genérica)
```

## Intent Classification Prompt

```
Classifique a mensagem abaixo em uma destas intenções:
- "search" — pesquisa geral na web (notícias, fatos, informações)
- "transcribe" — áudio para transcrição
- "procurement" — cotação de produto/serviço, comparação de preços, busca de fornecedores
- "unknown" — fora do escopo

Responda APENAS com uma palavra: search, transcribe, procurement, ou unknown.
```

## Handlers

### handleSearch(text)
- Chama Tavily API
- Retorna markdown com resultados

### handleTranscribe(audioUrl)
- Transcreve áudio
- Retorna texto transcrito

### handleProcurement(text)
- Busca produto em fontes (Tavily, marketplaces)
- Compara preços
- Retorna ProcurementResult com:
  - Nome do produto
  - Preços encontrados
  - Fornecedores
  - Links

## Concierge Router Shadow Mode

Um middleware shadow no `src/core/concierge-router.ts` classifica **todas** as mensagens que passam pelo webhook.

Feature flag: `FEATURE_CONCIERGE_ROUTER_SHADOW` (env var).
Quando ativo: loga a classificação mas não afeta o fluxo existente.

```typescript
classifyConciergeIntent(text) -> { intent, confidence, method }
```

## Feature Flags (`src/core/feature-flags.ts`)

Sistema de feature flags via env vars. Exemplo:
- `FEATURE_CONCIERGE_ROUTER_SHADOW` — shadow mode do concierge

---

# 15-SYSTEM-STATE-TODAY.md

# System State Today — 06 Jun 2026

> Snapshot do runtime atual. Tudo o que está rodando AGORA.

---

## Runtime Snapshot

| Processo | Local | Porta | Status |
|----------|-------|-------|--------|
| Hermes Gateway | ~/.hermes/ | 1408 (PID) → telegram | ✅ Ativo |
| Hermes Session | Terminal TUI | — | ✅ Esta sessão |
| Isaura Express | ~/openclaw/isaura/ | :3099 | ✅ PM2 (PID 15257) |
| Evolution API | Docker | :8080 | ✅ Container |
| n8n | Docker | :5678 | ✅ Container |
| Postgres | Docker (evolution-db-1) | :5432 | ✅ Container |
| Firefox Browser | XFCE desktop | — | ✅ Rodando (40+ tabs) |
| Chromium Headless | ~/.cache/ms-playwright/ | — | ✅ Instalado |
| Xorg XFCE | :0 | — | ✅ Desktop ativo |

## Model Status

| Model | Provider | Uso | Cost |
|-------|----------|-----|------|
| DeepSeek V4 Pro | OpenRouter | Hermes principal | $1.74/M in, $3.48/M out |
| DeepSeek V4 Flash | OpenRouter | Delegation, pesquisas | $0.14/M in, $0.28/M out |
| DeepSeek V4 Flash (free) | OpenRouter | Subagents | $0 (rate-limited) |
| Groq llama 3.3 70B | Groq | Isaura router | $0.59/M in, $0.79/M out |
| Claude Opus 4.x | Claude UI (browser) | Estratégia | $20/mês sub |
| Gemini | API key | Visão (Isaura) | $15/mês estimado |

## Files Not in Repo

| Arquivo | Tamanho | Conteúdo |
|---------|---------|----------|
| `~/.hermes/config.yaml` | ~10KB | Runtime completo |
| `~/.hermes/gateway_state.json` | — | Estado do gateway |
| `~/.hermes/cron/jobs.json` | ~21KB | Todos os cron jobs |
| `~/openclaw/isaura/.env` | — | Chaves de API |
| `~/openclaw/isaura/src/` | ~60+ arquivos .ts | Código fonte Isaura |
| `~/openclaw/isaura/package.json` | — | Deps Isaura |
| `~/openclaw/isaura/ecosystem.config.cjs` | — | PM2 config |
| `~/.openclaw/openclaw.json` | — | Config Claw |
| `~/openclaw-workspace/opus-memory.md` | — | Workflow Opus |
| `~/openclaw-workspace/decisions/*.md` | — | Decisões |
| `~/openclaw-workspace/hermes/*.md` | — | Identidade |
| `~/openclaw-workspace/premium-ui-spread/` | — | Broker setup |
| `~/openclaw-workspace/n8n/docker-compose.yml` | — | n8n infra |
| `~/.hermes/skills/` | — | Skills não sincronizadas |

## What's in the Repo (GitHub: buying-agent)

| Dir/File | Content |
|----------|---------|
| `AGENT_WORKSPACE.md` | Workspace rules |
| `ALPHA-VALIDATION.md` | Alpha checklist |
| `BROWSER_LLM_PACKET.md` | Browser init packet |
| `CLAUDE_PROJECT_INIT.md` | Claude project init |
| `CLAW_README.md` | Claw docs |
| `CLOUD_POLICY.md` | Cloud ops policy |
| `CONTEXT_INDEX.md` | Navigation map |
| `HERMES_README.md` | Hermes docs |
| `MARCELA_RUNBOOK.md` | Marcela runbook |
| `PREMIUMUI-ACCESS.md` | Premium UI access |
| `PROMPT_ENTRY.md` | Prompt entry format |
| `README.md` | Repo readme |
| `llms.txt` | LLM index |
| `architecture/` | System design docs |
| `archive/` | Archived docs |
| `board_reports/` | Board updates |
| `goals/` | Nightly goals + TODO |
| `manifests/` | Integrity manifests |
| `reviews/` | Code reviews |
| `runbooks/` | Operational procedures |
| `scripts/` | Sync scripts |
| `tokenomics/` | Cost tracking |

## Blockers P0

1. **Resend domain vazio** — email não funciona
2. **Domínio izzza.app** — não comprado
3. **Evolution Webhook** — wa path incompatível
4. **Imagem pipeline** — qualidade pífia (q_auto:good → f_jpg)
5. **Gemini Vision SQLite cache** — não implementado