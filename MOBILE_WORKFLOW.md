# MOBILE_WORKFLOW.md — Pipeline Harem Marketplace

> Projeto: Elisangela (U$40k) — Marketplace entretenimento adulto ES.
> Cada estágio = **1 URL** → copia tudo → cola no destino.

---

## Pipeline

```
Hermes → Perplexity → Hermes/DeepSeek → GPT 5.5 → Fable 5
```

---

## ① Perplexity Pro (deep research)

**URL pra copiar:** https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/mobile-pack/harem-marketplace-perplexity-prompt.md

**Fazer:** Abre URL → copia tudo → cola no Perplexity Pro → Deep Research → me manda output.

---

## ② Perplexity → Hermes

**Fazer:** Copia output → me manda no Telegram.
**Eu faço:** Processo com DeepSeek v4-pro → organizo `prompts/gpt55/` → te dou URL.

---

## ③ GPT 5.5 ext thinking

**URL:** `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/mobile-pack/harem-gpt55-prompt.md`

**Fazer:** Abre URL → copia tudo → cola no ChatGPT (GPT 5.5 + extended thinking) → envia.
Pede: "Output as single .md file, no zip."

---

## ④ Fable 5

**Fazer:** Copia output do GPT 5.5 → claude.ai → novo projeto → cola → aguarda.

---

## URLs fixas

| O quê | URL |
|-------|-----|
| Perplexity (Harem) | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/mobile-pack/harem-marketplace-perplexity-prompt.md` |
| Estado do sistema | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/00_hot/HOT_CONTEXT.md` |
| Este arquivo | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/MOBILE_WORKFLOW.md` |

---

## Feature 1 (alta prioridade): Compras + Gamificação

Quando chegar na etapa Fable 5, incluir no prompt:

1. **Sexshop/bebidas/gifts** — catálogo, compra pré-agendamento, entrega no local
2. **Pacote hora + presente** — combos preço fixo (ex: 4h + vinho + gift = U$500)
3. **Gamificação heavy-spender** — tiers, badges, pontos por gasto, combos exclusivos
4. **Para profissionais:** perfil com fotos, serviços, agenda, rating
5. **Para casas:** gestão de profissionais, comissões, analytics