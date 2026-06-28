---
name: nova-feature
description: Use para abrir uma nova feature no padrão SDD. Decide o tier (trivial/pequeno/arquitetural), cria specs/NNNN-<nome>/ com os templates certos, conduz o preenchimento de cima pra baixo pelos gates (product → design → domain → spec → tasks) e, quando há MCP conectado, importa a story do Jira no início e cria as issues na quebra de tasks. Acione com /nova-feature.
---

# Skill: Nova feature (loop SDD)

Abre e conduz uma feature pela esteira do `README.md`. A **spec é o contrato**; preencha na
ordem dos gates e pare em cada um para review. Siga as convenções do `CLAUDE.md`.

## Princípios
- **Pergunte em lotes curtos** com `AskUserQuestion`; ofereça defaults "(Recomendado)". Mas quando a
  ambiguidade for **profunda e ramificada** (uma decisão depende da outra), troque o lote por uma
  **sabatina** — rode **`/clarificar`** (uma pergunta por vez, caminhando a árvore) e volte com o
  entendimento fechado. Especialmente útil nos gates de **design** e **spec**.
- **Não delegue a `spec.md`** — os critérios de aceite são o contrato; o usuário valida.
- Ações outward-facing (criar issue, publicar) → **confirme antes**.
- *Tools-aware:* só use um MCP se ele estiver disponível na sessão (`mcp__<servidor>__*`);
  caso contrário, siga sem ele e registre como pendência.
- **Trava de conexão:** MCP já ativo não autoriza uso. Confirme **qual conta/workspace** a
  conexão aponta antes de ler a story, e reconfirme antes de **criar issues** (escrever na conta
  errada — ex.: Jira pessoal vs do projeto — vaza dado). Use a conexão validada no `/kickoff` se houver.

## Fase 1 — Identidade da feature
1. Calcule o próximo número: maior `NNNN` em `specs/` + 1, com 4 dígitos (ex.: `0002`).
2. Pergunte um nome curto em kebab-case → pasta `specs/NNNN-<nome>/`.
3. **(tools-aware) Importar contexto:** se Jira/Linear estiver conectado, pergunte se a feature
   tem uma story/épico. Se sim, leia a issue e use para semear `product.md`; guarde a chave na
   frontmatter (`jira: PROJ-123`). Se Confluence/Notion estiver conectado, puxe páginas relacionadas.
   **Se nada de gestão/doc estiver conectado** e o usuário quiser puxar insumo, **ofereça rodar
   `/integracoes` agora** (neutro — deixe-o dizer o que usa); se recusar, siga sem e registre a pendência.

## Fase 2 — Decidir o tier
Pergunte (gate): **"isso introduz decisão difícil de reverter ou nova fronteira de domínio?"**

| Resposta | Tier | Artefatos a criar |
|----------|------|-------------------|
| Não, é trivial (≤3 arquivos) | **Trivial** | só o PR — ou `specs/quick/NNN-slug/` (TASK.md + SUMMARY.md) p/ deixar rastro. |
| Não, mas é uma feature isolada | **Pequeno** | `spec.md` + `tasks.md` |
| Sim | **Arquitetural** | `product.md` + `design.md` + `domain.md` + `spec.md` + `tasks.md` |

Na dúvida, promova de tier (é barato). Copie os templates de `specs/_templates/` para a pasta.

## Fase 3 — Preencher de cima pra baixo (pelos gates)
Para cada artefato do tier, rascunhe a partir do template e **pare no gate para review**:

1. **`product.md`** (arquitetural) — problema, para quem, métrica, goals/non-goals.
2. **`design.md`** (arquitetural) — solução + os 5 eixos (stack, arquitetura, infra, qualidade,
   observabilidade) + alternativas/trade-offs/riscos. Decisão difícil de reverter → vira ADR.
   Trade-offs entrelaçados? Rode **`/clarificar`** para sabatinar os ramos antes de fixar a decisão.
   Se existir o subagente `domain-modeler`/`spec-reviewer`, ofereça delegar a eles.
3. **`domain.md`** (arquitetural) — bounded context, linguagem ubíqua, agregados, eventos.
   Atualize `docs/glossary.md` e `docs/architecture/context-map.md` se surgirem termos/fronteiras.
4. **`spec.md`** (sempre) — critérios de aceite em Given/When/Then, casos de borda, fora de escopo.
   Gate **Definition of Ready**: cada AC é testável e não-ambíguo? **Algum AC ainda vago ou um "como
   deveria se comportar quando…" em aberto? Rode `/clarificar`** para fechar a árvore antes de gravar.
   Se houver `spec-reviewer`, use-o.
   **Regra que combina vários fatores** (flags, estados, modos)? Use a **Matriz de decisão** do
   template — tabela-verdade é mais densa e barata em tokens que prosa, e cada linha vira teste.
5. **`tasks.md`** (sempre) — decomponha em tasks, cada uma mapeando para um ou mais AC + plano de teste.

## Fase 4 — Quebra de tasks e tracking
1. Preencha a tabela de `tasks.md` (task → cobre AC → depende de → status).
2. **(tools-aware) Criar issues:** se Jira/Linear estiver conectado, ofereça criar uma issue/subtask
   por task (confirme antes). Escrita é **uma via** (repo → ferramenta); grave o mapeamento
   `task # ↔ issue key` no `tasks.md`. **Se não houver MCP de gestão**, ofereça rodar `/integracoes`
   para conectar agora; se o usuário recusar, deixe a coluna para preencher à mão.

## Fase 5 — Pronto para implementar
- Cheque o **Definition of Ready** (ver `README.md`): AC testáveis, non-goals, termos no glossário,
  e — no tier arquitetural — `design.md` aprovado.
- Resuma com links clicáveis e aponte: implementar respeitando a regra de camadas (`src/README.md`),
  um teste por AC. Lembre o **Definition of Done** para o merge (AC verdes, ADRs, docs vivas, spec fiel).
- Se for repositório git e o usuário quiser, ofereça um commit dos artefatos da spec.

## Fase 6 — Validação (UAT)
Após a implementação (pode ser em outra sessão), rode a skill **`/validar`**: ela roda os gates de
`docs/engineering/TESTING.md`, mapeia `AC-N → teste`, resolve `SPEC_DEVIATION`, checa o Definition of Done e
atualiza `docs/STATE.md`. Encerre com `/handoff` se for pausar.
