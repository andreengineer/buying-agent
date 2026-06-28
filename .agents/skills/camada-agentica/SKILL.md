---
name: camada-agentica
description: Use para propor e gerar a camada agêntica do projeto — rules (CLAUDE.md, settings.json), subagents (.claude/agents), skills (.claude/skills) e workflows/CI — afinados ao stack, ferramentas, processo e domínio. Propõe com justificativa e gera só o aprovado. É chamada pelo /kickoff e também roda sozinha ao evoluir o projeto ou ao chegar novas ferramentas. Acione com /camada-agentica.
---

# Skill: Camada agêntica do projeto

Afina a camada que faz humanos e agentes **operarem a esteira**. Princípio: **proponha com
justificativa (qual insumo motiva cada item), gere só o aprovado.** Referência: `docs/engineering/agentic-layer.md`.

## Reúna o contexto
Stack e quality gates (`CLAUDE.md`, ADRs), ferramentas (`integrations.md`), processo (Scrum/Kanban)
e domínio (`context-map.md`, `glossary.md`). É isso que decide quais artefatos fazem sentido.

## Proponha (não gere sem OK)
- **Rules:** ajustes no `CLAUDE.md` por stack; `.claude/settings.json` com allowlist dos comandos
  comuns do stack e hooks. ⚠️ Permissões/hooks são sensíveis — confirme **cada um**.
- **Agents (subagentes)** em `.claude/agents/<nome>.md` (use `docs/engineering/_templates/subagent.template.md`):
  ex. `spec-reviewer` (gate DoR), `domain-modeler`, `adr-writer`, `<stack>-tester`.
- **Skills** em `.claude/skills/<nome>/` (use `docs/engineering/_templates/skill.template.md`): conforme as
  ferramentas, `/spec-to-jira`, `/publicar-confluence` (tools-aware).
- **Workflows:** hooks no `settings.json` (lint/teste no `Stop`). Para a **CI/CD** (gates na
  pipeline) delegue à skill `/setup-ci`; para o **gate de PR/MR**, à `/revisar-pr`.

## Regras
- Cada proposta cita o **insumo** que a motiva (ex.: stack Python → `pytest-tester` + allowlist).
- Itens não aprovados viram **itens de roadmap de adoção** (sugira `/roadmap`).
- Mapeie cada artefato em `docs/engineering/agentic-layer.md`.
