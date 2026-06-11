# MOBILE_WORKFLOW.md — Pipeline

> Cada estágio = **1 URL** → copia tudo → cola no destino.
> Zero zip. Zero extração. Zero navegação em diretório.

---

## Pipeline

```
Hermes → Perplexity → Hermes/DeepSeek → GPT 5.5 → Fable 5
```

---

## ① Perplexity Pro (deep research)

**URL pra copiar:** https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/mobile-pack/perplexity-full-prompt.md

**Fazer:** Abre URL → copia tudo → cola no Perplexity Pro → Deep Research → me manda output.

---

## ② Perplexity → Hermes

**Fazer:** Copia output do Perplexity → me manda no Telegram.
**Eu faço:** Processo com DeepSeek v4-pro → organizo em `prompts/gpt55/` → te dou URL.

---

## ③ GPT 5.5 ext thinking

**URL (chega após etapa 2):** `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/mobile-pack/gpt55-full-prompt.md`

**Fazer:** Abre URL → copia tudo → cola no ChatGPT com GPT 5.5 + extended thinking → envia.
Pede: "Output as a single .md file, no zip."

---

## ④ Fable 5

**Fazer:** Copia output do GPT 5.5 → claude.ai → novo projeto → cola → aguarda.

---

## URLs fixas

| O quê | URL |
|-------|-----|
| Perplexity (mobile) | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/mobile-pack/perplexity-full-prompt.md` |
| Scrapling analysis | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/reference/scrapling-analysis.md` |
| Estado do sistema | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/00_hot/HOT_CONTEXT.md` |
| Workflow (este) | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/MOBILE_WORKFLOW.md` |