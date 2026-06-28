---
name: STATE
description: Memória de trabalho volátil — onde paramos, próximo passo, bloqueios.
alwaysApply: true
---

# STATE — Memória viva do projeto

> Memória de trabalho **entre sessões** (humanos e agentes). É **volátil**: atualizada o tempo
> todo. Diferente do **ADR** (decisão durável e imutável). Decisão estrutural → ADR; estado do
> trabalho → aqui. Atualize ao **pausar/encerrar**; leia ao **retomar**. Use a skill `/handoff`.

**Última atualização:** <YYYY-MM-DD> por <nome>

## Em andamento / próximo passo
> O que está aberto agora e a **próxima ação concreta** (não "continuar a feature" — diga o passo).
- Feature ativa: `specs/NNNN-<nome>/` — <fase atual>
- Próximo passo: <ação específica>

## Decisões recentes
> Resumo cronológico. Se for difícil de reverter, vire um ADR e linke aqui.
- <YYYY-MM-DD: decisão — [ADR-NNNN](adr/NNNN-*.md) se aplicável>

## Bloqueios
- [ ] <o que trava · quem/como destrava · desde quando>

## Ideias adiadas / backlog técnico
- <ideia → quando reconsiderar (qual gatilho)>

## Todos soltos
- [ ] <tarefa que não cabe ainda numa spec>
