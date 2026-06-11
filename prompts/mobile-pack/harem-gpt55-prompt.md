# README.md — GPT 5.5 Extended Thinking

> **You are GPT 5.5 with extended thinking enabled.**
> Your goal is to generate a comprehensive Fable 5 prompt that architects the Harem Marketplace platform.

## Files in this directory

| File | Purpose |
|------|---------|
| `context.md` | Full business context — client, market, features |
| `data.json` | Structured data — pricing tiers, features, constraints, revenue model |
| `instructions.md` | Exact output format for the Fable 5 prompt |

## Instructions

1. Read `context.md` → understand the business completely
2. Read `data.json` → understand the structured constraints
3. Read `instructions.md` → understand what to generate
4. Think deeply with extended thinking
5. Output a **single .md file** that IS the Fable 5 prompt

## Output Requirement

Generate ONE Fable 5 prompt file that covers the complete platform architecture. No zip, no multiple files. A single comprehensive .md that can be pasted directly into Claude Fable 5 as the first message in a new project.
---
# CONTEXT
---

# Context — Harem Marketplace Platform (for GPT 5.5)

## The Client

**Elisangela Meira Andrade** — empresária do ES, 3 empresas no entretenimento adulto.

| Empresa | CNPJ | Desde |
|---------|------|-------|
| Pousada Ragazza LTDA | 30.312.740/0001-24 | Fev/2021 |
| Harem Cafe Entretenimento LTDA | 64.533.711/0001-04 | Jan/2026 |
| Aurora Producoes Privadas LTDA (Maison Privee) | 64.353.970/0001-53 | Jan/2026 |

## Current Operations

| Aspect | Detail |
|--------|--------|
| Physical venue | Harem Cafe, Vitória-ES |
| Ad spend | U$8k/month **exclusively** on competitor marketplaces (Ilha do Prazer primary) |
| Professional pricing | Min U$100/hour |
| Client profile | Buys luxury beverages, stays 24h+, budget U$1-4k per visit |

## The Platform

A marketplace connecting:
- **Supply:** Physical venues (casas) + Independent professionals (autônomas)
- **Demand:** High-spending clients (U$1-4k budget)
- **Revenue:** Recurring B2B + B2C ad packages (not commission-based)

### Key Design Constraints

1. **Segregated branding** — the platform brand is NOT Harem Cafe. Zero visible conflict.
2. **Both supply types** — physical venues AND independent professionals can advertise
3. **No conflict of interest** — professionals and venues in ES can coexist; platform is neutral
4. **Ad packages are the product** — venues and professionals pay monthly for visibility
5. **Agentified ad management** — AI handles ad optimization + media buying, 1 CMO oversees
6. **Gradual migration** — U$8k/mo ad spend shifts from competitor platforms to own platform

## Feature 1: High Priority

### Buy sexshop + beverages + luxury gifts before scheduling
- Catalog of products available for pre-order
- Client selects items to be delivered to venue during visit
- Or sends a "purpose package" (hour package + gift combo)

### Gamification for heavy spenders
- Spending tiers (Bronze/Silver/Gold/Platinum)
- Points per U$ spent → redeem for upgrades, gifts, exclusive content
- Badges: "Connoisseur", "Regular", "VIP"
- Exclusive combos unlock at each tier
- Visible status on profile (optional)

## Business Model Detail

```
Supply (casas + autônomas) → pagam pacote de anúncio mensal
  ↓
Plataforma → ads + discovery para clients
  ↓
Clients (U$1-4k) → booking + sexshop/gifts + gamificação
  ↓
Revenue → pacotes ads (recorrente) + comissão opcional em transações
```

## Ad Management (Agentified + SaaS)

1. AI automates: campaign creation, audience targeting, budget allocation, creative rotation
2. SaaS dashboard: CMO manages 1 dashboard for all campaigns
3. Cross-platform: ads run on Google, Meta, TikTok, plus partner marketplaces
4. Learning loop: AI learns which creatives convert, auto-optimizes

## Budget

| Item | Value |
|------|-------|
| Total project budget | U$40,000 |
| Current monthly ad spend (competitor platforms) | U$8,000 |
| Target: migrate to own platform | Gradual, phased |
| Initial build | Platform MVP + ad system
---
# DATA (structured constraints)
---

{
  "_schema": "harem-marketplace-v1",
  "_desc": "Structured constraints and data for GPT 5.5 to generate the Fable 5 prompt",
  "project": {
    "name": "Harem Marketplace",
    "budget_usd": 40000,
    "timeline": "2026 Q3",
    "current_monthly_ad_spend": 8000
  },
  "supply_side": {
    "types": ["physical_venues", "independent_professionals"],
    "conflict_rule": "Platform is neutral. Branding segregated from Harem Cafe. No visible conflict."
  },
  "revenue_model": {
    "primary": "recurring_ad_packages_b2b_b2c",
    "description": "Venues and professionals pay monthly for ad visibility, featured listings, promoted profiles",
    "secondary": "optional_commission_on_transactions",
    "agentified_ads": {
      "ai_managed": true,
      "saas_dashboard": true,
      "cmo_count": 1,
      "channels": ["google", "meta", "tiktok", "partner_marketplaces"]
    }
  },
  "feature_1_gamification": {
    "priority": "high",
    "components": [
      "sexshop_catalog_pre_order",
      "beverages_pre_order",
      "luxury_gifts_catalog",
      "purpose_package_hours_plus_gift",
      "gamification_tiers",
      "points_per_dollar_spent",
      "badges_system",
      "exclusive_combos_per_tier"
    ],
    "tiers": ["Bronze", "Silver", "Gold", "Platinum"]
  },
  "platform_features": {
    "profiles": ["venues", "professionals", "clients"],
    "booking_scheduling": true,
    "payments": true,
    "messaging": true,
    "ratings_reviews": true,
    "sexshop_ecommerce": true,
    "gamification": true,
    "ad_management_saas": true
  },
  "growth_strategy": {
    "phase_1": "Platform MVP + first venues and professionals onboarded",
    "phase_2": "Gradual ad spend migration ($8k/mo from competitors)",
    "phase_3": "Scale B2B/B2C ad packages, expand ES",
    "agentified_ads_goals": "AI manages campaigns, auto-optimizes creative, budget allocation, targeting"
  },
  "constraints": {
    "branding_segregated": true,
    "no_conflict_of_interest": true,
    "mobile_first": true,
    "brazilian_market": true,
    "legal_adult_entertainment": true,
    "lgpd_compliance": true,
    "age_verification_required": true
  }
}
---
# INSTRUCTIONS
---

# Instructions — Generate the Fable 5 Prompt

## What to Generate

A single `.md` file that is the **Fable 5 prompt** — to be pasted directly into claude.ai as the first message in a new project.

## Prompt Structure

The Fable 5 prompt must cover:

### 1. Mission Statement
"You are Fable 5 (Mythos-class). Your job is to architect a complete adult entertainment marketplace platform for the Brazilian market (Espírito Santo). This is a buildable, shippable MVP. Not a strategy discussion."

### 2. Business Context
- Elisangela's existing operations (Harem Cafe, U$8k/mo ad spend, ICP U$1-4k)
- Platform serves BOTH physical venues AND independent professionals
- Revenue model: recurring B2B/B2C ad packages (NOT commission-based)
- Branding: segregated from Harem Cafe, no visible conflict of interest
- Budget: U$40k

### 3. Feature Set (High Priority)
Specify in detail:
- **Sexshop/beverages/gifts pre-order** — catalog, checkout, delivery to venue
- **Purpose packages** — bundle hours + gift, fixed price combos
- **Gamification** — tiers (Bronze/Silver/Gold/Platinum), points, badges, exclusive combos per tier, visible status
- **Professional profiles** — photos, videos, services, availability, rating
- **Venue profiles** — multiple professionals, analytics, ad management dashboard
- **Booking system** — calendar, availability, confirmation, reminders, check-in
- **Client profiles** — spending history, tier status, preferences
- **Ad management** — agentified AI campaigns, SaaS dashboard for CMO

### 4. Architecture Requirements
- Tech stack recommendation (Node/TypeScript since Isaura uses it, or Python)
- Database schema (users, venues, professionals, bookings, transactions, products, gamification)
- Payment integration (Pix, credit card, age verification)
- Mobile-first design (80% of clients on phone)
- LGPD compliance, age verification
- Content moderation

### 5. What NOT to Build (V1)
- Don't build full CRM
- Don't build payment gateway from scratch (use existing)
- Don't overbuild AI agent system — 1 CMO dashboard is enough
- Don't build native apps — PWA/mobile-first web is sufficient

### 6. Implementation Order
Phase 1 → Phase 2 → Phase 3 with clear milestones

### 7. Estimated Costs
Development hours, server costs, payment processing fees, ad spend per phase

## Output Format Rules

1. **Single .md file** — no zip, no multiple files
2. **35-50k characters** (optimal for Fable 5 context window)
3. **Self-contained** — Fable 5 should not need external context
4. **Buildable specs** — include code snippets for critical paths
5. **Risk section** — flag legal, compliance, payment processing risks

## Final Instruction to Include in the Prompt

"Do not spend output summarizing the brief back to me. Produce the build plan, architecture, data model, execution order, and risk analysis. If ambiguous, choose the simplest shippable version. Mark risky features for later."