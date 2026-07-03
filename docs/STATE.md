---
name: STATE
description: Memória de trabalho volátil — onde paramos, próximo passo, bloqueios.
alwaysApply: true
---

# STATE — Memória viva do projeto

> Memória de trabalho **entre sessões** (humanos e agentes). É **volátil**: atualizada o tempo
> todo. Diferente do **ADR** (decisão durável e imutável). Decisão estrutural → ADR; estado do
> trabalho → aqui. Atualize ao **pausar/encerrar**; leia ao **retomar**. Use a skill `/handoff`.

**Última atualização:** 2026-07-02 por Hermes (SDD kickoff parcial)

## Em andamento / próximo passo
- **SDD scaffold completo** (commit c732518, v0.1.10) — estrutura, skills, templates, CI gate prontos
- Próximo passo: **rodar `/kickoff` completo** (preencher product docs, architecture, glossary) OU
  começar a primeira feature real via `/nova-feature`

## Decisões recentes
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
- CODESPAR_API_KEY não configurada → MCP CodeSpar em setup mode (só `codespar_get_started`)
- Cron jobs usando `deepseek/deepseek-v4-flash` → modelo não é mais válido (user trocou para DeepSeek v4 como default)

## Ideias adiadas / backlog técnico
- CodeSpar Asaas MCP para Pix — precisa de ASAAS_API_KEY
- Evolution API via CodeSpar (já temos Evolution API, redundância?)
