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