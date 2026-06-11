# MOBILE_WORKFLOW.md — Pipeline de Prompts (copiar-colar do celular)

> **80% do tempo você está longe do PC.**
> Cada etapa abaixo tem uma URL raw do GitHub. Abre, copia tudo, cola no destino.
> Zero arquivos locais. Zero SSH. Zero IDE.

---

## Etapa 1 — Perplexity Pro Deep Research

**URL:** https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/perplexity-valuation-engine.md

**O que fazer:**
1. Abre o link acima no celular
2. Copia **tudo** (select all → copy)
3. Abre perplexity.ai → cola → seleciona **"Deep Research"** → envia
4. Perplexity pesquisa por ~5-10min
5. Copia o output completo → salva num Google Doc / Note / me envia no Telegram

**O que esperar:** Pesquisa profunda sobre valuation engine, mercado de vinhos brasileiro, concorrência UHNW, data sources.

---

## Etapa 2 — Hermes Processa Perplexity Output

**O que fazer:**
1. Me envia (Hermes) o output do Perplexity no Telegram
2. Eu processo com DeepSeek v4-pro: estruturo, verifico fontes, preparo brief técnico
3. Faço upload do resultado processado no GitHub → nova URL raw

**Aguardar confirmação minha antes de seguir.**

---

## Etapa 3 — GPT 5.5 Extended Thinking (gera .zip pro Fable 5)

**URL (chegará após Etapa 2):** `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/gpt55-valuation-brief.md`

**O que fazer:**
1. Abre o link → copia tudo
2. Abre chatgpt.com → seleciona GPT 5.5 com **extended thinking** ligado
3. Cola o prompt → envia
4. GPT 5.5 vai gerar um entendimento rico e pensar por ~3-5min
5. Pede: "Generate a .zip file with separate .MD files for the Fable 5 prompt pack, following this structure:
   - 00_FABLE_MAIN_PROMPT.md (main prompt, 30-50k chars)
   - 01_PROJECT_BRIEF.md
   - 02_CONTEXT.md
   - 03_IMPLEMENTATION.md
   - MANIFEST.json
   - README.md"
6. Baixa o .zip

---

## Etapa 4 — Fable 5 (execução)

**O que fazer:**
1. Extrai o .zip no celular (Files app / Google Drive)
2. Abre claude.ai → **CRIA NOVO PROJETO** (não reaproveita o anterior)
3. Project Instructions: `"Você é Fable 5. Projete o motor de valuation 'vale esse preço?' para Isaura. Contexto abaixo."`
4. Cola `00_FABLE_MAIN_PROMPT.md` como primeira mensagem
5. Deixa Fable 5 pensar por 5-10min
6. Refina: usa `05_FOLLOWUP_PROMPTS.md` se precisar direcionar
7. Copia output final

---

## Regras de Ouro (Mobile)

| Situação | Faça |
|----------|------|
| Link raw não funciona | Me avisa no Telegram — ajusto o path |
| Prompt muito grande pro celular | Uso split automático ou Google Drive como cache |
| Perplexity travou | Tenta de novo com consulta mais curta |
| GPT 5.5 não gerou .zip | Pede explicitamente: "Generate all files as a downloadable .zip" |
| Fable 5 não entendeu | Pede: "Read the file 00_FABLE_MAIN_PROMPT.md from the context" |
| Dúvida em qualquer etapa | Me manda print → respondo em segundos |

---

## URLs Rápidas (aponta pra sempre)

| Recurso | URL |
|---------|-----|
| Prompt Perplexity (Etapa 1) | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/perplexity-valuation-engine.md` |
| Scrapling analysis | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/scrapling-analysis.md` |
| Contexto atual do sistema | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/00_hot/HOT_CONTEXT.md` |
| AGENT_WORKSPACE.md | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/AGENT_WORKSPACE.md` |
| Este arquivo | `https://raw.githubusercontent.com/andreengineer/buying-agent/main/MOBILE_WORKFLOW.md` |

---

*Gerado por Hermes em 2026-06-11. Qualquer etapa que travar, me chama.*