---
name: kickoff
description: Use ao iniciar OU dar continuidade a um projeto com o boilerplate SDD. Primeiro descobre o modo — greenfield (começando do zero) ou brownfield (já rodando) — e roteia. Greenfield conduz uma entrevista Lean Inception (visão, personas, MVP). Brownfield mapeia o estado atual (as-is), identifica gaps vs o padrão SDD e captura decisões históricas. Os dois caminhos passam pelo kickoff técnico nos 5 eixos (tech stack, arquitetura, infra, qualidade, observabilidade), propõem a camada agêntica do projeto (rules, subagents, skills, workflows/CI) e convergem num roadmap incremental, gerando a "constituição" do projeto. As integrações com ferramentas do time (Jira, Confluence, MCPs) são uma skill separada (/integracoes) — rode antes para insumos read-first, ou depois. Acione com /kickoff.
---

# Skill: Kickoff de projeto (Lean Inception + SDD)

Você vai **entrevistar, mapear, propor e gerar um roadmap**. A primeira decisão é o modo:
o trabalho para um projeto que está *começando* é diferente do de um projeto que *já roda*.

## Princípios de condução
- **Pergunte em lotes curtos** com `AskUserQuestion` (máx. 4 perguntas, 2-4 opções cada).
  Ofereça sempre um default "(Recomendado)" como primeira opção; aceite "Other" livre.
  Quando um eixo abrir uma **decisão ramificada** (escolhas que dependem umas das outras — ex.:
  arquitetura → bounded contexts → infra), troque o lote por uma **sabatina**: rode **`/clarificar`**.
- **Não invente decisões de arquitetura.** Você propõe opções com trade-offs; quem decide é o usuário.
- **Não levante nem proponha ferramentas aqui** — isso é a skill `/integracoes`. O kickoff só faz a
  **oferta neutra** (Fase 0.5) de conectar. Se a `/integracoes` já rodou, aproveite os insumos puxados;
  senão, siga sem e deixe `/integracoes` como item do roadmap.
- Confirme um resumo antes de gerar arquivos. Gere tudo de uma vez no fim.
- O objetivo final dos dois caminhos é o mesmo: **a constituição do projeto + um roadmap
  acionável para rodar com o time.**

## Fase 0 — Detectar o modo
1. Inspecione o diretório: manifests (`package.json`, `pyproject.toml`, `go.mod`…), `src/`
   com código real, histórico git, docs já preenchidos.
   - Só o boilerplate / repo vazio → provável **greenfield**.
   - Código de produto existente → provável **brownfield**.
2. Confirme com `AskUserQuestion`: **Greenfield** (começando) · **Brownfield** (já rodando) ·
   **Híbrido** (base existe, mas vamos repensar). Roteie conforme a resposta.
3. Leia `README.md` e `CLAUDE.md` para alinhar com a esteira SDD.

## Fase 0.5 — Oferta de integração (neutra)
Conectar MCPs é **ortogonal** ao kickoff e é trabalho da skill `/integracoes`. Aqui você faz só
**uma oferta neutra** — **não liste nem proponha ferramentas** (quem levanta o ferramental é a
`/integracoes`; deixe o usuário dizer o que usa de fato lá).

Pergunte com `AskUserQuestion` (uma pergunta, **sem citar nomes de ferramenta**):
> *"Quer conectar suas ferramentas via MCP agora? Conectar antes deixa os artefatos com dado real
> (read-first)."* — opções: **Conectar agora (recomendado)** · **Seguir e conectar depois** · **Já conectei**.

- **Conectar agora →** rode **`/integracoes`** e retome o kickoff com os insumos puxados (cite a origem nas fases).
- **Conectar depois →** siga só com a entrevista; `/integracoes` vira item do roadmap de adoção (Fase 5).
- **Já conectei →** **use os insumos puxados** (cite a origem) nas fases abaixo.

> A `/integracoes` é **re-executável**. Mais adiante, se uma ferramenta passar a ajudar (puxar épico,
> ler PR), **reofereça-a** no ponto em que o valor aparece — não precisa ser só aqui.

---

## Fase 1A — [GREENFIELD] Descoberta (Lean Inception)
Conduza as atividades da inception em lotes de `AskUserQuestion` e **gere um artefato por pilar**
(não enfie tudo num doc só — cada pilar tem seu lar):

1. **Visão & escopo** → `vision.md`: problema e para quem; categoria + diferencial; North Star;
   2-3 coisas que o produto explicitamente **NÃO é / NÃO faz**.
2. **Stakeholders** → `stakeholders.md`: quem influencia/é impactado (interesse × influência) e
   como engajar cada um.
3. **Jornadas** → `journeys.md`: as 1-3 jornadas ponta a ponta — etapas, dores e oportunidades.
4. **Funcionalidades** → `features.md`: brainstorm a partir das **jornadas**, classificadas por
   esforço/valor/confiança/UX e **sequenciadas em ondas** (Onda 1 = MVP).
5. **MVP** → `mvp-canvas.md`: a Onda 1 + a hipótese principal e o critério de sucesso.

→ Saídas: `vision.md` · `stakeholders.md` · `journeys.md` · `features.md` · `mvp-canvas.md`.
A **Onda 1** de `features.md` alimenta o `roadmap.md` (Fase 5).

## Fase 1B — [BROWNFIELD] Mapear o estado atual (as-is)
Execute a skill **`/mapear`** (mesma lógica): leia o código, entreviste as lacunas, faça o gap
analysis dos 5 eixos e capture decisões históricas como ADR retroativo.

→ Saídas: `docs/architecture/assessment.md` (as-is + gaps) e a lista de ADRs retroativos.
Esses gaps alimentam as Fases 2 e 5.

---

## Fase 2 — Kickoff técnico (os 5 eixos)
Um lote de `AskUserQuestion` por eixo. Proponha defaults sensatos.
- **Greenfield:** são decisões *a tomar*.
- **Brownfield:** são decisões *já tomadas* (capture como ADR retroativo) + as que o time
  quer *mudar* (capture como ADR novo que substitui, mais um item no roadmap).

1. **Tech stack** — linguagem, framework/runtime, gerência de pacotes, versão alvo.
2. **Arquitetura base** — estilo (monolito modular / serviços / serverless), camadas DDD
   (default do boilerplate), e os **bounded contexts** (do MVP no greenfield; validados no brownfield).
3. **Infra** — cloud, modelo de deploy, ambientes, CI/CD, IaC.
4. **Qualidade** — pirâmide de testes, cobertura mínima, lint/format, **análise estática** (type-check,
   complexidade, SAST/segurança — o que é bloqueante vs aviso), política de review, DoD.
5. **Observabilidade** — logs estruturados, métricas, tracing, alertas, SLO/SLI iniciais.

## Fase 3 — Confirmação
Mostre um resumo em tabela (decisão → escolha → vira ADR? novo ou retroativo?). Peça OK.

## Fase 4 — Geração dos documentos
Gere/atualize usando os templates do projeto:

| Arquivo | Modo | Template |
|---|---|---|
| `docs/product/vision.md` | greenfield | `docs/product/_templates/vision.template.md` |
| `docs/product/stakeholders.md` | greenfield | `docs/product/_templates/stakeholders.template.md` |
| `docs/product/journeys.md` | greenfield | `docs/product/_templates/journeys.template.md` |
| `docs/product/features.md` | greenfield | `docs/product/_templates/features.template.md` (classificadas + sequenciadas) |
| `docs/product/mvp-canvas.md` | greenfield | `docs/product/_templates/mvp-canvas.template.md` |
| `docs/architecture/assessment.md` | brownfield | `docs/architecture/_templates/assessment.template.md` |
| `docs/architecture/context-map.md` | ambos | existente (inicial no greenfield; reverse-engineered no brownfield) |
| `docs/architecture/overview.md` | ambos | existente — consolide os **5 eixos** + segurança + operacional, com links para ADRs/context-map/diagrams/TESTING |
| `docs/glossary.md` | ambos | existente (semeie os termos centrais) |
| `CLAUDE.md` | ambos | existente (preencha stack, comandos, quality gates, observabilidade) |
| `docs/architecture/adr/NNNN-*.md` | ambos | `docs/architecture/adr/_template.md` (um por decisão estrutural; retroativos no brownfield) |
| `docs/product/roadmap.md` | ambos | `docs/product/_templates/roadmap.template.md` |

> `docs/engineering/integrations.md` e `.mcp.json` são gerados pela skill `/integracoes`, não aqui.
> Após o `context-map`, ofereça rodar **`/diagramar`** para os diagramas de arquitetura (Mermaid).

Regras:
- **ADRs:** numere após o 0001. Greenfield: decisões novas. Brownfield: retroativos (status
  aceito, registrando o porquê histórico) + novos para mudanças propostas. Imutáveis.
- **CLAUDE.md:** preencha stack/comandos/camadas e adicione blocos "Quality gates" e
  "Observabilidade". Não remova as regras SDD existentes.
- **Roadmap:** quick wins de baixo risco primeiro. No brownfield, inclua a seção de **adoção
  incremental do SDD** (sem big-bang: começar pela próxima feature, backfill de ADRs depois).

## Fase 4.5 — Camada agêntica do projeto
Execute a skill **`/camada-agentica`** (mesma lógica): a partir de stack + ferramentas + processo
+ domínio, proponha rules, subagents, skills e workflows/CI afinados — **com justificativa** — e
gere só o aprovado. Itens não aprovados viram itens do roadmap (Fase 5). Ref.: `docs/engineering/agentic-layer.md`.

## Fase 5 — Roadmap e fechamento
- Execute a skill **`/roadmap`** (mesma lógica): construa `roadmap.md` em Now/Next/Later, com valor,
  esforço, dono e dependências, quick wins primeiro — para rodar e revisar **com o time**.
- Se for repositório git, ofereça `git add -A && git commit -m "docs: kickoff do projeto"`.
- Resuma com links clicáveis e aponte o próximo passo: criar a 1ª feature em `specs/NNNN-<nome>/`
  escolhendo o tier (ver `README.md`).
