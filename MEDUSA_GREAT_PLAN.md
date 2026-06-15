# 🐙 MEDUSA: The Great Plan

> Extrair *typing data* de ACB cruzando todas as plataformas.
> 4 fases: Extract → Structure → Analyze → Visualize.
> Output final: um mapa vivo de personalidade, comportamento, interesses, estilo de expressão.

---

## ⚙️ Fase 0 — Mapa de Tentáculos (fontes disponíveis)

### Big Tech Accounts (acesso real ou exportável)

| Fonte | Tipo de dado | Volume estimado | Status |
|-------|-------------|-----------------|--------|
| **Firefox** (histórico local) | URLs, buscas, bookmarks, frequência | 5.8K visits ✅ | Extraído |
| **Chrome** (histórico local) | URLs, buscas, bookmarks | ~? | Parcial |
| **ChatGPT** (export OpenAI) | Conversas, prompts, temas recorrentes | Export pendente | 🔴 Pendente |
| **Google Takeout** | Buscas, YouTube, Maps, My Activity | Export pendente | 🔴 Pendente |
| **Telegram** (export Desktop) | Mensagens, grupos, contatos, frequência | Export pendente | 🔴 Pendente |
| **Instagram** (export Meta) | Stories, DMs, likes, saved | Export pendente | 🔴 Pendente |
| **WhatsApp** (export por chat) | Conversas-chave | Export pendente | 🔴 Pendente |
| **GitHub** (API pública) | Commits, issues, stars, linguagens | Acessível via API | 🔴 Não iniciado |
| **Twitter/X** (arquivo) | Tweets, likes, retweets, DMs | Request pendente | 🔴 Pendente |
| **LinkedIn** (export) | Conexões, posts, search history | Request pendente | 🔴 Pendente |
| **OpenRouter/DeepSeek** | Usage log, modelos favoritos, custos | Ledger manual | 🔴 Não iniciado |
| **YouTube** (history via Takeout) | Watch history, subscriptions, searches | Dentro do Takeout | 🔴 Pendente |
| **Spotify** | Streaming history, playlists, gêneros | Request pendente | 🔴 Pendente |

### Fontes self-reported / manuais
- Obsidian vault (projetos, people, questions)
- Medium articles (escritos próprios)
- Fable 5 artifacts
- Hermes cron outputs

---

## 🔬 Fase 1 — Extract (cada tentáculo)

### 1.1 Firefox (✅ já extraído)
```bash
# ~/personal-obsidian-life/02_PARSED/firefox_history.csv
# Colunas: visited_at, url, title, visit_count, typed
```
**O que extrair**: domínios, padrões temporais (manhã/tarde/noite), buscas repetidas, pular entre sites.

### 1.2 Chrome (parcial)
```sql
# Chrome History DB → JSON já extraído
# Mesma análise que Firefox, comparar padrões
```

### 1.3 Google Takeout (🔴 pendente)
1. Ir em https://takeout.google.com
2. Selecionar APENAS: My Activity, Search, YouTube, Maps/ Timeline, Calendar
3. Formato JSON, frequência única
4. Baixar, salvar em `~/personal-obsidian-life/01_EXPORTS/google/takeout_archive/`
5. Rodar script de parse

### 1.4 ChatGPT Export (🔴 pendente)
1. Ir em https://chat.openai.com → Settings → Data Controls → Export Data
2. Aguardar email (até 24h)
3. Baixar ZIP → salvar em `~/personal-obsidian-life/01_EXPORTS/chatgpt/`
4. Parse: extrair prompts, temas, decisões, estilo de interação

### 1.5 Telegram Export (🔴 pendente)
1. Telegram Desktop → Settings → Advanced → Export Telegram data
2. Formato JSON, pessoais + grupos, sem mídia (primeira rodada)
3. Salvar em `~/personal-obsidian-life/01_EXPORTS/telegram/`
4. Analisar: vocabulário, tom, horários, tópicos recorrentes

### 1.6 Instagram (🔴 pendente)
1. Meta Accounts Center → Download your information
2. JSON, All time, media Low
3. Extrair: DMs, likes, saved posts, search history

### 1.7 WhatsApp (🔴 pendente)
- Chat → More → Export chat → Without media
- Salvar `.txt` em `~/personal-obsidian-life/01_EXPORTS/whatsapp/`
- Foco nos contatos de alta frequência

### 1.8 GitHub (via API — sem export)
```bash
gh repo list --limit 100 --json name,language,updatedAt
gh api user/repos --paginate
gh api user/events --paginate
```
Extrair: linguagens, horários de commit, issues abertas, stars em repositórios (sinal de interesse).

### 1.9 Twitter/X Archive (🔴 pendente)
- Settings → Your account → Download an archive of your data
- JSON, leva ~24h
- Extrair: tweets próprios (voz, tom), likes (interesses), DMs, search history

### 1.10 LinkedIn (🔴 pendente)
- Settings & Privacy → Data Privacy → Get a copy of your data
- Sections: Profile, Connections, Posts, Search history, Messages

### 1.11 Spotify
- https://www.spotify.com/us/account/privacy/ → Request my data
- Streaming history, playlists, search queries

---

## 🧠 Fase 2 — Structure (schema unificado)

Cada fonte é parseada para um schema comum de **typing signals**:

### Schema Universal: `typing_signal.json`
```json
{
  "source": "firefox | chatgpt | telegram | google | ...",
  "timestamp": "ISO8601",
  "signal_type": "search | message | read | write | click | location | listen | watch",
  "content": {
    "raw": "text original",
    "domain": "domínio (se URL)",
    "language": "pt | en | mix",
    "topic": "categoria extraída",
    "entities": ["pessoa", "empresa", "conceito"]
  },
  "context": {
    "time_of_day": "morning | afternoon | evening | night",
    "day_of_week": "mon|tue|...",
    "device": "mobile | desktop | unknown",
    "session_length_sec": 0,
    "preceding_url": "(se browser)",
    "following_url": "(se browser)"
  },
  "personality_signals": {
    "sentiment": "positive|negative|neutral|analytical",
    "certainty": 0.0-1.0,
    "curiosity_score": 0.0-1.0,
    "formality": 0.0-1.0,
    "urgency": 0.0-1.0,
    "exploration_vs_exploitation": "explore|exploit"
  }
}
```

### Scripts de Parse por Fonte
Cada script em `~/personal-obsidian-life/04_SCRIPTS/`:
- `parse_firefox.py` → typing_signals.json
- `parse_chatgpt.py` → typing_signals.json
- `parse_google.py` → typing_signals.json
- `parse_telegram.py` → typing_signals.json
- `parse_instagram.py` → typing_signals.json
- `parse_github.py` → typing_signals.json

Output consolidado: `~/personal-obsidian-life/02_PARSED/medusa_signals.jsonl`

---

## 🔍 Fase 3 — Analyze (extrair padrões do humano)

### Dimensões de Análise

#### 3.1 Personalidade & Estilo Cognitivo
- **Dominância sensorial**: visual? textual? auditivo? (vide Spotify/YouTube vs leitura)
- **Estilo de decisão**: analítico vs intuitivo (ChatGPT prompts, search queries)
- **Tolerância a ambiguidade**: busca por respostas definitivas vs exploratórias
- **Impulsividade**: gap entre search e purchase/action
- **Ceticismo**: frequência de fact-checking, cross-referencing

#### 3.2 Interesses & Curiosidade
- **Tópicos recorrentes**: clusters de domínios, entidades, conceitos
- **Curiosity decay**: quanto tempo um interesse novo sobrevive
- **Deep vs shallow**: profundidade de leitura (tempo na página) vs bouncing
- **Seasonal patterns**: ciclos semanais, mensais, anuais de interesse

#### 3.3 Comportamento Temporal & Ritmos
- **Cronotipo**: horários de pico de atividade cognitiva
- **Session patterns**: deep work vs micro-sessions vs doom-scrolling
- **Transitions**: gatilhos que mudam de contexto (ex: busca → YouTube)
- **Procrastination signals**: páginas de escape durante horário produtivo

#### 3.4 Estilo de Expressão
- **Vocabulário**: palavras mais frequentes, jargões, muletas
- **Tom**: formal vs casual, imperativo vs consultivo, otimista vs pessimista
- **Comprimento**: frases curtas vs prolixas (por plataforma)
- **Code-switching**: quando troca pt ↔ en, e por quê
- **Metáforas preferidas**: guerra? construção? viagem? biologia?

#### 3.5 Relacionamentos & Tribos
- **Quem são os top-N contatos** (frequência, reciprocidade, tom)
- **Grupos**: quais comunidades online frequenta
- **Influência**: quem/quais fontes cita, compartilha, responde
- **Gatekeepers**: quem intermedia informação pra você

#### 3.6 Padrões de Consumo
- **Information diet**: proporção notícia/entretenimento/trabalho/estudo
- **Recommendation response**: clica em recomendações? busca organicamente?
- **Novelty seeking**: conteúdo novo vs conforto (repetições de domínio/tópico)
- **Attention span**: tracking de bounce rate por tipo de conteúdo

---

## 🎨 Fase 4 — Visualize & Map (tornar legível)

### Output 1: Obsidian Graph (mapa vivo)
```
03_OBSIDIAN/
├── 00_Index.md              # Dashboard vivo
├── 01_Daily/               # [futuro: daily typing log]
├── 02_Search_History.md    # Padrões de busca
├── 03_Personality_Map.md   # ★ Output central
├── 04_Interest_Graph.md    # Clusters de interesse
├── 05_Behavior_Rhythms.md  # Padrões temporais
├── 06_Projects.md          # Projetos detectados
├── 07_People.md            # Mapa de contatos
├── 08_Expression_Style.md  # ★ Voz e estilo
├── 09_Questions_I_Ask.md   # Perguntas que voltam
└── 10_Behavior_Patterns.md # Macropadrões
```

### Output 2: Personality Map (03_Personality_Map.md)
```markdown
# 🧠 Personality Map — ACB

## Cognitive Profile
- **Thinking style**: [analytical | intuitive | mixed]
- **Risk posture**: [conservative | calculated | aggressive]
- **Decision speed**: [fast/impulsive | measured | slow/deliberate]
- **Learning style**: [read → do | do → read | watch → do | social]

## Behavioral Archetypes (by context)
| Context | Archetype | Signal |
|---------|-----------|--------|
| Work/Projects | [Builder | Strategist | Perfectionist | Ship-it] | 
| Learning | [Explorer | Deep-diver | Skimmer | Social learner] |
| Social | [Observer | Connector | Debater | Supporter] |
| Consumption | [Curator | Binger | Sampler | Completionist] |

## Recurring Patterns
- [padrão 1]
- [padrão 2]
- [padrão 3]

## Temporal Signature
- **Peak hours**: [HH:MM-HH:MM]
- **Deep work blocks**: [avg minutes]
- **Recharge activities**: [what, when]
- **Procrastination triggers**: [what contexts]

## Evolution over time
[Como os padrões acima MUDARAM nos últimos meses/anos]
```

### Output 3: Expression Style (08_Expression_Style.md)
```markdown
# 🗣 Expression Style — ACB

## Voice Profile
- **Register**: [formal | casual | technical | poetic]
- **Sentence length**: [short/long avg words]
- **Punctuation signature**: [... | ! | ? | em-dash -- | caps]
- **Lexical fingerprint**: [top 30 words, top emojis, top abbreviations]

## Platform Variation
| Platform | Tone | Length | Language mix |
|----------|------|--------|-------------|
| Telegram | | | |
| ChatGPT | | | |
| Twitter | | | |
| WhatsApp | | | |
| GitHub | | | |
| Instagram | | | |

## Code-Switching Map
- **When PT**: [contexts]
- **When EN**: [contexts]
- **Trigger words that flip language**: [...]

## Communication Goals (detected)
- [ ] Persuade
- [ ] Understand
- [ ] Archive/reference
- [ ] Connect socially
- [ ] Vent/process
- [ ] Decide/commit
```

### Output 4: Medusa Canvas (HTML/diagrama interativo)
Um canvas SVG/HTML mostrando:
- **Cluster de interesses** como bolhas (tamanho = intensidade, cor = categoria)
- **Fluxo temporal** como rio semanal
- **Rede de contatos** como grafo (grossura = frequência)
- **Evolução** como timeline (como ACB mudou em 6 meses)

---

## 📋 Pipeline Completo (Ordem de Execução)

```
SEMANA 1: Extrair tudo
  □ Firefox (✅ ok)
  □ Chrome (parse)
  □ Google Takeout (solicitar)
  □ ChatGPT Export (solicitar)
  □ Telegram Desktop (exportar)
  □ GitHub (API)
  □ WhatsApp (chats principais)

SEMANA 2: Parsear + Estruturar
  □ Rodar scripts de parse para cada fonte
  □ Consolidar em medusa_signals.jsonl
  □ Validar qualidade dos dados
  □ Preencher lacunas

SEMANA 3: Analisar
  □ Personality Map (draft)
  □ Expression Style (draft)
  □ Interest Graph (draft)
  □ Behavior Rhythms (draft)

SEMANA 4: Visualizar + Refinar
  □ Obsidian vault completo
  □ Canvas visual
  □ Feedback loop: o que falta?
  □ Cron jobs de manutenção
```

---

## ⚠️ Regras de Ouro

1. **RAW untouched** — nunca editar export original. Scripts são a única fonte de transformação.
2. **Parse scripts são repeatables** — se rodar de novo, mesmo output. Se mudar, versionar.
3. **Nunca upload raw p/ cloud** — tudo local. Só análises agregadas vão pra Fable/artifacts.
4. **Uma fonte por vez** — processar Firefox completamente antes de abrir ChatGPT.
5. **Cada análise responde "E daí?"** — sem fatos soltos. Todo insight vira ação ou pergunta.
6. **Dados stale viram noise** — Firefox de 3 meses atrás é contexto, não sinal ativo.
7. **Privacidade > Completeza** — pular o que não confortável exportar.

---

> Editado: 2026-06-15
> Próxima revisão: após extrair 3+ fontes
