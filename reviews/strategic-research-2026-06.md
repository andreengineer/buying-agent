# Strategic Research — June 2026

## 1. Meta Business Agent: The Elephant in the Room

**Launched:** June 3, 2026 (Conversations London)
**Channel:** WhatsApp, Messenger, Instagram
**Capabilities:** FAQ, catalog recommendations, lead qual, appointment booking, close sales
**Pricing:** Free tier NOW, paid subscription coming
**Reach:** 3B users via WhatsApp

### Isaura's Moat vs Meta

| Dimension | Meta Business Agent | Isaura |
|-----------|-------------------|--------|
| Catalog | Single store catalog | Dynamic search across ALL stores |
| Price comparison | ❌ Not possible | ✅ Cross-store, ±15% tolerance |
| Wine expertise | ❌ Generic | ✅ Ratings, freight, images |
| Search depth | Shallow (FAQ) | Deep (Tavily → decay iterations) |
| Freight | ❌ Not calculated | ✅ Correios estimate |
| Premium report | ❌ | ✅ PDF + image comparison |
| Custom LLM pipeline | ❌ Fixed | ✅ Adaptive (fast/deep modes) |

**Key insight:** Meta's agent turns WhatsApp into a business operating layer. Isaura should NOT compete on basic customer service — Meta wins on distribution. Instead, Isaura competes on **cross-store intelligence** that Meta cannot do (no API for competitor pricing).

## 2. Agentic Commerce Landscape (2026)

**Market size (McKinsey):** $5T global agentic commerce by 2030
**US B2C (Morgan Stanley):** $190-385B through agents by 2030
**Funding:** YC funding 20+ AI assistant startups in current batch

**Key competitors:**
- Sierra (enterprise, outcome-based pricing, multi-model)
- Decagon (customer service agents)
- Nuvemshop Nuvechat (WhatsApp commerce BR)
- Noem.ai (AI concierge)
- Meta Business Agent (mass market)

**Isaura's niche:** "Cross-store procurement concierge" — NOT customer support, NOT single-store catalog. The user delegates "find me the best price on X" and Isaura searches across 10+ sources.

## 3. Posicionamento CORRETO (ICP clearing)

**Isaura NÃO é Buscapé/Zoom com agentes.** A comparação de preço é feature, não produto.

**Produto:** Concierge UHNW — "esse produto vale o que custa?"
**Dor real:** Rico gastador não quer economizar R$30. Quer:
- Saber se o Taylor's Tawny 10 anos vale os R$250 vs um Graham's de R$180
- Leitura de avaliação textual de sommelier, não tabela de preço
- Confiança de bom gosto — curadoria, não commodity
- Tempo — não passar 2h lendo review no Google

**Métrica de sucesso:** Não é "preço mais baixo encontrado". É "recomendação de qualidade que o usuário confia".
**Eval correto:** Comparação textual entre opções premium avaliando custo-benefício, não ±15% de preço.

## 4. Monetization

| Model | Example | Works for Isaura? |
|-------|---------|-------------------|
| Outcome-based ($/resolved) | Sierra | ✅ Best fit — charge per successful purchase |
| Subscription ($/mo) | Intercom Fin | ⚠️ Requires active user base |
| Transaction fee (%) | Traditional affiliate | ⚠️ Low margin on cheap items |
| Usage-based (token) | OpenAI | ✅ Second option per-query |
| Lead gen ($/qualified lead) | Meta BA | ❌ Isaura doesn't generate leads |

**Recommendation:** Outcome-based + usage hybrid. Freemium tier (3 queries/mo free), then $0.50/query or $19/mo unlimited.

## 4. Technical Opportunities (Immediate)

1. **Add Mercado Livre API integration** — MELI has a public API for search/pricing. Faster and cheaper than Tavily scraping.
2. **Product image caching** — SQLite cache for Gemini Vision (already in backlog). Reduces latency + cost.
3. **N8n automation** — Already running at :5678. Could wire: WhatsApp → Isaura → n8n → email/SMS notifications for price drops.
4. **Context_maintenance.sh on Claw cron** — Keep HOT_CONTEXT.md fresh daily without Hermes overhead.
5. **WhatsApp catalog-sync** — Shopify/MELI/Nuvemshop to Isaura's format for faster matching.

## 5. Proposed Roadmap (Next 30 Days)

```
Week 1: T3 eval real (npm run eval → pass/fail table)
Week 1: Mercado Livre API integration (faster procurement)
Week 2: First friendly user (find 1 person to test via WA)
Week 2: Pricing page (static HTML, $0.50/query or $19/mo)
Week 3: n8n price-drop alert workflow
Week 4: Premium report PDF to WA (already have pdf-renderer.ts)
```

**Cost:** ~$0.50/week OpenRouter + Tavily credits (existing lane)
**Revenue target:** 1 user at $19/mo = break even in month 2