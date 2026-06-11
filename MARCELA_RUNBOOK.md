# MARCELA_RUNBOOK.md (v2 — Mobile-First)

**Para Marcela. Leia devagar. Siga exatamente.**

> Atualizado 2026-06-11: Agora com URLs raw do GitHub — tudo acessível do celular.

---

## O que é isso

Você é o **correio** entre o André e os sistemas de IA.
Você **transporta pacotes**. Você **não interpreta**, **não decide**, **não improvisa**.
Não "melhore" o texto. Copie exato. Cole exato.

---

## Fluxo Principal (Mobile — 80% do tempo)

Cada etapa é: **abrir URL → copiar tudo → colar no destino → copiar resposta → mandar pro André.**

### Etapa 1 — Área de Trabalho

Quando o André falar **"roteiro"** ou **"pipeline"**:

1. Abra este link: **https://raw.githubusercontent.com/andreengineer/buying-agent/main/MOBILE_WORKFLOW.md**
2. Leia qual etapa ele pediu
3. Siga as instruções de lá

### Etapa 2 — Perplexity (pesquisa profunda)

Quando o André falar **"Perplexity"**:

1. Abra: **https://raw.githubusercontent.com/andreengineer/buying-agent/main/prompts/perplexity-valuation-engine.md**
2. Copie o texto inteiro (select all → copy)
3. Abra **perplexity.ai** no navegador
4. Cole na caixa de texto
5. Selecione **"Deep Research"**
6. Clique em enviar
7. Aguarde a resposta (~5-10 minutos)
8. Copie a resposta inteira
9. Mande pro André pelo WhatsApp ou Telegram

### Etapa 3 — ChatGPT (GPT 5.5)

Quando o André falar **"GPT"** ou **"5.5"**:

1. O André vai te mandar um link raw
2. Abra o link → copie tudo
3. Abra **chatgpt.com**
4. Selecione GPT 5.5 com **"extended thinking"** ativado
5. Cole o texto → envie
6. Depois que responder, digite:
   "Generate a .zip file with separate .MD files for the Fable 5 prompt pack"
7. Baixe o .zip que ele gerar
8. Salve no Google Drive (pasta do projeto)
9. Avise o André

### Etapa 4 — Claude (Fable 5)

Quando o André falar **"Fable"**:

1. Abra o .zip que o GPT gerou
2. Extraia os arquivos
3. Abra **claude.ai**
4. Crie um **NOVO PROJETO** (não use o anterior)
5. Nas instruções do projeto, escreva exatamente o que o André mandar
6. Abra o arquivo **00_FABLE_MAIN_PROMPT.md**
7. Copie tudo
8. Cole como primeira mensagem no Claude
9. Aguarde a resposta (~5-10 minutos)
10. Copie a resposta e mande pro André

---

## Tarefas Avulsas

### Acessar arquivo no GitHub
1. O André vai te mandar um link começando com `https://raw.githubusercontent.com/...`
2. Abra o link
3. Copie o conteúdo
4. Cole onde o André pedir

### Subir arquivo no Google Drive
1. Abra drive.google.com
2. Navegue até a pasta do projeto (André manda o link)
3. Clique em "Novo" → "Upload de arquivo"
4. Selecione o arquivo baixado
5. Avise o André

---

## O que você NUNCA deve fazer

- ❌ Não mande arquivo `.env` pra lugar nenhum
- ❌ Não mande senha pra lugar nenhum
- ❌ Não "melhore" o texto — copie exato
- ❌ Não tome decisão se a IA pedir algo que parece errado
- ❌ Não instale nada no computador por conta própria
- ❌ Não responda perguntas da IA como se fosse o André
- ❌ Não crie conta em site nenhum

---

## Se der errado

Pare tudo. Mande pro André **exatamente o que apareceu na tela** (print ou texto).
Não tente resolver. Não tente de novo. Espere instrução.

---

## Resumo

```
ANDRÉ DISSE "roteiro"?
  → Abre MOBILE_WORKFLOW.md
  → Segue instrução da etapa

ANDRÉ DISSE "Perplexity"?
  → Abre URL → copia → cola → resposta → manda pro André

ANDRÉ DISSE "GPT" ou "5.5"?
  → Abre URL → copia → cola → pede .zip → salva → avisa

ANDRÉ DISSE "Fable"?
  → Extrai .zip → cria projeto → cola 00_...md → resposta → manda

ANDRÉ MANDOU LINK?
  → Abre → copia → cola onde ele disse

DUVIDOU?
  → Pergunta pro André. Não decide.
```

---

*Aprovado por Andre (CEO). Qualquer dúvida, pergunte ao André.*