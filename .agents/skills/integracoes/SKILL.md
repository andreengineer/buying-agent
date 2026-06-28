---
name: integracoes
description: Use para levantar as ferramentas do time (Jira, Confluence, Notion, GitHub, cloud, observabilidade), conectar os MCPs com segurança, puxar insumos de leitura e definir os fluxos de escrita (repo → ferramenta). Gera docs/engineering/integrations.md e, se aprovado, .mcp.json, e registra os MCPs validados no roteamento (bloco "Ferramentas conectadas (MCP)" do CLAUDE.md + skills tools-aware). Rode ANTES do /kickoff para alimentar os artefatos com dado real (read-first), ou DEPOIS, quando o ferramental ficar conhecido. Re-executável. Acione com /integracoes.
---

# Skill: Integrações e MCPs do time

Esta skill é **ortogonal ao kickoff** — você nem sempre conhece o ferramental ao iniciar o
projeto. Rode quando souber. É **idempotente**: re-executar atualiza `docs/engineering/integrations.md`.

**Quando rodar:**
- **Antes do `/kickoff` (ideal):** os MCPs de leitura alimentam `vision`/`assessment`/`context-map`
  com dado real (read-first).
- **Depois, a qualquer momento:** quando o ferramental ficou conhecido, ou para configurar a escrita.
  Se o kickoff já rodou e você puxar insumos novos aqui, **ofereça enriquecer** os artefatos
  existentes (context-map, glossary, assessment), citando a origem.

## Princípios
- **Trava de conexão (MCP):** conexão já ativa **não** autoriza uso. Sempre confirme **qual
  conta/workspace** ela aponta antes de ler — e reconfirme antes de **qualquer escrita**. Usar a
  conta errada (ex.: Notion pessoal no lugar do business) lê contexto errado e, na escrita,
  **vaza dado do projeto** para fora do contexto de trabalho.
- Ações outward-facing (conectar, publicar, criar issue) → **confirme antes**.
- *Tools-aware:* só use um MCP disponível na sessão (`mcp__<servidor>__*`); senão, documente e siga.

## Fase 1 — Levantar as ferramentas do time
Lotes de `AskUserQuestion`:
- **Gestão e processo:** Jira / Trello / Linear / Azure DevOps (+ **Scrum / Kanban / Waterfall**).
- **Documentação:** Confluence / Notion / Evernote / Google Docs.
- **Código e CI:** GitHub / GitLab / Bitbucket. **Cloud:** AWS / GCP / Azure.
- **Observabilidade e comunicação:** Datadog / Sentry / Grafana; Slack / Teams.
- **Libs/APIs:** Context7 (lookup na verificação de conhecimento do `CLAUDE.md`).

## Fase 2 — Conexão de leitura (read-first) + trava de segurança
Para as ferramentas de leitura (Confluence, Jira, Notion, GitHub, cloud), verifique se o MCP
já está disponível na sessão (`mcp__<servidor>__*`):
- **Já conectado → ⚠️ trava de segurança, NÃO use direto.** Pode apontar para a conta errada.
  1. **Identifique a conta/workspace** (se o MCP expõe — ex.: buscar o workspace/usuário atual) e
     mostre ao usuário. Se não der pra verificar, trate como **não confirmado**.
  2. Pergunte (`AskUserQuestion`): **usar esta conexão** (workspace X) · **reconectar / trocar de
     conta** (pessoal → business) · **usar outra ferramenta** · **pular esta fonte**.
  3. Só prossiga após confirmação explícita. Registre a conta/workspace em `integrations.md`.
- **Não conectado** → pergunte se quer conectar. ⚠️ Adicionar um MCP novo (`.mcp.json` /
  `claude mcp add`) normalmente **só passa a valer após reconectar a sessão**. Ofereça:
  - **(a)** conectar agora → reabrir a sessão → rodar `/integracoes` (ou `/kickoff`) de novo; ou
  - **(b)** seguir sem conectar → vira item do roadmap de adoção. Documente em `integrations.md`.

**Puxe os insumos disponíveis** (só dos MCPs já conectados e validados) e cite a origem (link/ID):
- Confluence / Notion: decisões de negócio, visão, domínio, arquitetura.
- Jira / Linear: épicos, roadmap atual, stories abertas.
- GitHub / cloud: contexto de código e infra (as-is).

## Fase 3 — Plano de escrita (write-side)
1. **Mapeie cada ferramenta ao MCP server** (tabela em `docs/engineering/_templates/integrations.template.md`).
   Verifique nome/disponibilidade na doc oficial — não invente nomes de pacote.
2. **Defina os fluxos de escrita e quando disparam** — regra: **leia cedo, escreva no gate**:
   - Gate "aprovado" de vision/design/spec/roadmap → publica no Confluence/Notion.
   - Quebra de `tasks.md` → cria issues/subtasks no Jira/Linear.
   - ADR novo → comenta no PR do GitHub/GitLab. Evento (aprovou/subiu) → Slack/Teams.
   - Escrita é sempre **repo → ferramenta** (uma via); guarde a chave de volta (`jira:`, `confluence:`).
   - ⚠️ **Antes da primeira escrita**, reconfirme a conta/workspace de destino (mesma trava).
3. **Scaffolding (confirme antes).** Se aprovado, gere `.mcp.json` na raiz com placeholders,
   **sem segredos** (tokens via env / `claude mcp add`). Não commite credenciais.

## Fase 4 — Gerar/atualizar `docs/engineering/integrations.md`
A partir de `docs/engineering/_templates/integrations.template.md`: ferramentas, MCPs, conta/workspace validada,
fluxos read/write e status. Se o kickoff já rodou e você puxou insumos novos, ofereça enriquecer
`context-map.md` / `glossary.md` / `assessment.md` com o que encontrou (citando origem).

## Fase 5 — Registrar no roteamento (rules + skills)
Conexão validada **não basta**: o resto da esteira precisa **saber** que ela existe e quem a usa.
1. **CLAUDE.md (rules):** atualize o bloco **"Ferramentas conectadas (MCP)"** com os servidores
   validados — `mcp__<servidor>__*`, conta/workspace e quais skills consomem cada um. Como o
   `CLAUDE.md` é `alwaysApply: true`, toda sessão passa a carregar esse roteamento.
2. **Skills (roteamento):** confirme que as skills tools-aware apontam para os MCPs certos —
   `/nova-feature` (Jira/Linear/Confluence/Notion), `/revisar-pr` (GitHub/GitLab), `/publicar-*`
   (Confluence/Notion). Não duplique lógica: as skills checam `mcp__<servidor>__*` em runtime.
3. **Camada agêntica:** se as novas ferramentas pedem artefatos novos (skill `/spec-to-jira`,
   subagente, hook de publicação), **delegue à `/camada-agentica`** (propõe com justificativa, gera
   só o aprovado). Itens não aprovados viram roadmap de adoção.

## Fechamento
- Resuma com links clicáveis e liste os MCPs que entraram no roteamento (`CLAUDE.md`).
- Próximo passo: se o `/kickoff` ainda não rodou, sugira rodá-lo agora (com os MCPs de leitura já
  conectados, os artefatos saem com dado real). Senão, aponte `/nova-feature`. Se registrou
  ferramentas novas, considere `/camada-agentica` para afinar a esteira a elas.
