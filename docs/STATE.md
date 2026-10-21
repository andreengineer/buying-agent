---
name: STATE
description: Memória de trabalho volátil — onde paramos, próximo passo, bloqueios.
alwaysApply: true
---

# STATE — Memória viva do projeto

> Memória de trabalho **entre sessões** (humanos e agentes). É **volátil**: atualizada o tempo
> todo. Diferente do **ADR** (decisão durável e imutável). Decisão estrutural → ADR; estado do
> trabalho → aqui. Atualize ao **pausar/encerrar**; leia ao **retomar**. Use a skill `/handoff`.

**Última atualização:** 2026-10-21 por Claude (PR `feat/0002-family-cohort-w1`)

## Em andamento / próximo passo
- **Feature ativa: `specs/0002-family-cohort-w1/`** — coorte familiar #1 (2026-10-21 → 10-27).
  Comece por `specs/0002-family-cohort-w1/plan.md` §4 (kickoff do CC). Design aprovado = merge do PR.
- **Hermes:** rodada de pesquisa de 10h em `goals/2026-10-21_nightly_goal.md` (apontar o arquivo
  explicitamente — o seletor `ls goals/ | sort | tail -1` devolve `README.md`).
- **Self-org lane:** `specs/0003-pv-since-last-open/` (PalantirView, Codex no lat).
- Dados da coorte e logs de ops ficam em `~/isaura-data/` — **nunca** neste repo (público).

## Decisões recentes
- 2026-10-21 (proposta, vale com o merge): escada de autonomia A0→A3; semana 1 = A0 para todos, A1 só André, agente nunca paga
- 2026-10-21 (proposta): vertical padrão da semana 1 = bens duráveis R$ 200–5k; farmácia/mercado só como dado de pesquisa
- 2026-10-21 (proposta): esforço padrão do Codex = `high`; `max` só com `escalate:` (fecha D1)
- 2026-07-02: Adotado SDD (@igoruehara/spec-driven v0.1.10) como governance model
- 2026-07-02: MCP CodeSpar configurado no Hermes (setup mode, sem API key ainda)
- 2026-07-02: CI gate esteira configurado em `.github/workflows/esteira.yml`

## Documentos pendentes (kickoff incompleto)
- [ ] `docs/product/vision.md` — definir visão do buying-agent
- [ ] `docs/product/features.md` — features priorizadas
- [ ] `docs/product/roadmap.md` — Now/Next/Later
- [ ] `docs/product/stakeholders.md` — quem é impactado
- [ ] `docs/product/journeys.md` — jornadas do usuário
- [ ] `docs/product/mvp-canvas.md` — hipótese + critério de sucesso
- [ ] `docs/architecture/overview.md` — preencher 5 eixos
- [ ] `docs/glossary.md` — popular termos do domínio
- [ ] `docs/architecture/context-map.md` — bounded contexts
- [ ] ADRs para decisões estruturais

## Bloqueios
- Inputs do André para a coorte (vertical, CEP, coorte, autonomia, teto Pix, canal) — defaults valem qui 2026-10-22 12:00
- CODESPAR_API_KEY não configurada → MCP CodeSpar em setup mode (só `codespar_get_started`)
- Cron jobs usando `deepseek/deepseek-v4-flash` → modelo não é mais válido (user trocou para DeepSeek v4 como default)

## Ideias adiadas / backlog técnico
- CodeSpar Asaas MCP para Pix — precisa de ASAAS_API_KEY
- Evolution API via CodeSpar (já temos Evolution API, redundância?)
