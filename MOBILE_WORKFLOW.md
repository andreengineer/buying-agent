# MOBILE_WORKFLOW.md — Pipeline 1-Arquivo

> Cada estágio = **1 URL raw** → copia tudo → cola no destino.
> Zero zip, zero extração, zero múltiplos arquivos no Poco C65.

---

## Pipeline

```
Hermes → Perplexity → Hermes/DeepSeek → GPT 5.5 → Fable 5
 ①        ②             ③               ④          ⑤
```

---

## ① Hermes → Perplexity Pro (deep research)

**Já está no ar:** https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/perplexity-valuation-engine.md

**Fazer:** Abre URL → copia tudo → cola no Perplexity Pro → Deep Research → aguarda output → me manda o output.

---

## ② Perplexity → Hermes (DeepSeek v4-pro)

**Você faz:** Copia o output do Perplexity → me manda no Telegram.

**Eu faço:** Processo com DeepSeek v4-pro → estruturo → gero `prompts/gpt55-brief.md` → push no GitHub → te dou a URL.

---

## ③ Hermes → GPT 5.5 ext thinking

**URL (chega após etapa 2):** `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/gpt55-brief.md`

**Fazer:** Abre URL → copia tudo → cola no ChatGPT com GPT 5.5 + extended thinking → envia.

**O GPT 5.5 vai gerar UM arquivo .md. Peça:** "Output as a single .md file that I can copy-paste directly into Claude Fable 5. No zip, no multiple files."

---

## ④ GPT 5.5 → Fable 5

**Fazer:** Copia o output .md do GPT 5.5 → abre claude.ai → cria **novo projeto** → cola como primeira mensagem → aguarda.

---

## Regras

| Regra | Por quê |
|-------|---------|
| **1 URL = 1 estágio** | Sem procurar arquivo em diretório no Android |
| **Nunca .zip** | Poco C65 não extrai zip fácil |
| **Nunca múltiplos arquivos** | Confunde no Files app |
| **Copia tudo → cola** | Zero edição manual |
| **Output de um = input do próximo** | Pipeline linear, sem desvio |

---

*Atualizado: 2026-06-11*