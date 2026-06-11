# README.md — Perplexity Pro Deep Research: Adult Entertainment Marketplace Brasil

> **You are Perplexity Pro with Deep Research enabled.**
> Your goal is to research the Brazilian adult entertainment marketplace industry for a new platform being built with a U$40k budget.

## Files in this directory

| File | Purpose |
|------|---------|
| `context.md` | Background: the client, business model, existing competitors |
| `research_questions.md` | Research axes — answer ALL in depth |

## Instructions

1. Read `context.md` first — understand the business and the opportunity
2. Read `research_questions.md` — investigate each question thoroughly
3. Research in Portuguese AND English (Brazilian market focus)
4. Return structured markdown:
   - Executive Summary (top 5 insights)
   - Detailed findings per research question
   - Competitive analysis matrix
   - Feature recommendations
   - Pricing/compliance considerations
5. **Cite ALL sources with URLs**

## Output

Single structured markdown document. No zip, no multiple files.
---
# CONTEXT
---

# Context — Harem Marketplace Platform

## The Client

**Elisangela Meira Andrade** — empresária do setor de entretenimento adulto no Espírito Santo.

### Empresas

| Empresa | CNPJ | Fundação | Atividade |
|---------|------|----------|-----------|
| Pousada Ragazza LTDA (Ragazza) | 30.312.740/0001-24 | Fev/2021 | Pousada |
| Harem Cafe Entretenimento LTDA (Harem Cafe) | 64.533.711/0001-04 | Jan/2026 | Cafe/entretenimento adulto |
| Aurora Producoes Privadas LTDA (Maison Privee) | 64.353.970/0001-53 | Jan/2026 | Producao/conteudo privado |

### Current Operations (Harem Cafe)

| Aspect | Detail |
|--------|--------|
| Location | Vitória, ES |
| Ad spend | U$8k/month **exclusively on marketplaces** (Ilha do Prazer is primary) |
| Professional pricing | Min U$100/hour |
| ICP profile | Buys luxury beverages, stays 24h+, budget U$1-4k |
| Business model | Marketplace ads → brings clients to physical venue |

## The Opportunity

Elisangela wants to build her **own marketplace platform** serving multiple adult entertainment venues ("casas de entretenimento adulto").

**Why she can win:**
1. She already spends U$8k/mo on competitor marketplaces — knows the model intimately
2. She has her own CRM with professional contacts
3. She can replicate/improve the best assets from existing marketplaces
4. She understands the ICP (luxury buyer, U$1-4k budget)
5. U$40k budget to build

**Value prop for venues:** "Our platform brings you qualified leads"
**Value prop for professionals:** "Best place to acquire high-spending clients"

## Market Context

Marketplaces in this space handle:
- Professional profiles with photos/videos (assets)
- Scheduling/booking
- Ratings and reviews
- Location-based search
- Payment processing

## Competition

| Platform | Type | Notes |
|----------|------|-------|
| Ilha do Prazer | Adult marketplace | Main competitor — E.S. focused |
| Privacy | Content subscription (OnlyFans-style) | Different model (digital content) |
| Skooka | Adult marketplace | Competitor |
| Meu Patrocinio | Sugar dating | Adjacent market |
| OnlyFans | Content subscription | International, BR presence |

## Budget & Timeline

| Item | Value |
|------|-------|
| Total budget | U$40,000 |
| Monthly ad spend (current) | U$8,000 — could redirect to own platform |
| Development | Full platform (marketplace + booking + sexshop/gifts + gamification) |

## Tech Implications

- Platform needs: user profiles, venue profiles, professional profiles, scheduling, payments, messaging, reviews, e-commerce (sexshop/gifts), gamification system
- Could use: Node.js (existing Isaura stack), Playwright for scraping competitor assets
---
# RESEARCH QUESTIONS
---

# Research Questions — Harem Marketplace Platform

## 1. Competitor Analysis (Ilha do Prazer, Skooka, similares)

- How does Ilha do Prazer work? What features does it offer? (profiles, booking, payments, reviews, ads?)
- What is Ilha do Prazer's pricing model? (commission per booking? monthly fee? ad packages?)
- How do professionals/venues use the platform? What's the workflow?
- What features are missing or poorly executed that a new platform could improve?
- How does Skooka compare? Differentiators?
- What other adult entertainment marketplaces exist in Brazil? (regional players, niche platforms)
- What do user reviews say about these platforms? (pain points, complaints, desires)

## 2. Business Model & Pricing

- What commission structures do adult marketplace platforms use?
- What are the typical pricing tiers for professionals? (hourly rates by region/type)
- How do platforms handle payments? (gateways, chargebacks, age verification)
- What are the advertising/promotion options for venues within these platforms?
- What is the average customer LTV in this space?
- What premium features could justify higher margins?

## 3. Feature Benchmarking

Research the **exact features** of platforms in this space:

### Profiles & Discovery
- What information do professional profiles include? (photos, videos, stats, services, availability)
- How is search/filtering implemented? (location, price, services, ratings, availability)
- How are venues displayed vs individual professionals?

### Booking & Scheduling
- How does scheduling work across platforms? (real-time calendar, request-based, instant book?)
- What happens after booking? (confirmation, reminders, check-in process?)

### Payments & Commerce
- What payment methods are accepted? (Pix, credit card, crypto?)
- How are tips, deposits, and pre-payments handled?
- How does the platform handle the "sexshop/gift" add-on concept?
- What fraud prevention measures exist?

### Reviews & Trust
- How are reviews/ratings implemented? (verified only? anonymous?)
- What identity verification exists for both professionals and clients?

## 4. Gamification in Adult/Service Marketplaces

- What gamification mechanics exist in adult entertainment or dating platforms? (tiers, badges, points, leaderboards)
- Case studies of successful gamification: What made them work?
- How could a "loyalty program" work for high-spending users (U$1-4k)?
- "Package deals" — examples of bundling services + products in this industry
- How do platforms encourage repeat visits from heavy spenders?

## 5. Legal & Compliance Brazil

- What regulations apply to adult entertainment marketplaces in Brazil?
- Age verification requirements and best practices
- Data privacy (LGPD) considerations for professional and client data
- Payment processing restrictions for adult content/services
- Liability considerations: what happens if a booking goes wrong?
- Are there specific municipal/state regulations in Espírito Santo?

## 6. Technology & Platform Architecture

- What tech stacks do existing adult marketplaces use? (any public info)
- What are the critical technical challenges? (scalability, content moderation, fraud prevention, payment processing)
- What APIs exist for age verification, identity checks, payment gateways in Brazil?
- How to handle image/video content at scale? (CDN, moderation, DMCA)

## 7. Growth & Acquisition Strategy

- How do existing platforms acquire venues and professionals?
- What's the typical CAC for acquiring both supply (professionals) and demand (clients)?
- How did Ilha do Prazer grow? (initial strategy, funding, marketing)
- What role does SEO play in this space?
- Elisangela spends U$8k/mo on competitor ads — what's the migration strategy?

---

## Output Requirements

Return your research as structured markdown with:
1. **Executive Summary** — top 5 actionable insights
2. **Competitive Deep-Dive** — per-competitor analysis with features, pricing, gaps
3. **Feature Recommendations** — what to build, what to skip, priority order
4. **Gamification/Commerce Opportunities** — specific mechanics for heavy-spender retention
5. **Legal & Compliance Checklist** — must-haves before launch
6. **Implementation Notes** — technical considerations, risks, unknowns

**Cite ALL sources.** If insufficient data, say so.