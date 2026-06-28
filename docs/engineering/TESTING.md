---
name: TESTING
description: Comandos de gate e convenções de teste. Puxe ao codar, validar ou montar CI.
alwaysApply: false
---

# TESTING — Como verificar o projeto

> **Fonte única dos comandos de gate** e das convenções de teste. É o que o **DoD**, a **CI** e os
> **subagentes** consomem para provar que uma task/feature está pronta — sem inspeção visual.
> Preenchido no kickoff (eixo Qualidade) e mantido vivo.

## Como rodar
| Nível         | Comando                   | Quando |
|---------------|---------------------------|--------|
| Unidade       | `<comando>`               | sempre, rápido |
| Integração    | `<comando>`               | adapters / repos / contratos |
| Aceite (UAT)  | `<comando>`               | um teste por `AC-N` da spec |
| Lint / format    | `<comando>`               | pré-commit / CI |
| Análise estática | `<comando>` (type-check, complexidade, SAST) | CI — sem findings bloqueantes |
| Cobertura        | `<comando>` (mín. `<X>%`, gera relatório) | CI — relatório anexado ao PR |

## Convenções
- Pirâmide: muitos testes de unidade, menos de integração, poucos de aceite.
- **Cada `AC-N` da spec tem um teste de aceite que é o seu gate.** Nomeie o teste com o ID
  (`test_AC_1_*` / `AC-1: ...`) para rastreabilidade spec → teste.
- Domínio não sobe infra; integração usa `<testcontainer / mock de borda>`.
- **Análise estática** (escolha por stack): type-check (`<mypy/tsc/…>`), complexidade/smells e
  **SAST/segurança** (`<sonar/codeql/semgrep/…>`). Define o que é **bloqueante** (barra o merge)
  vs **aviso** (entra como tendência em `metrics.md`, não bloqueia).

## Gates (Definition of Done executável)
- Uma **task** só vira `done` quando o **Gate (comando)** dela em `tasks.md` passa.
- Uma **feature** só faz merge quando todos os AC estão verdes + lint + **análise estática limpa**
  (sem findings bloqueantes) + cobertura mínima.
- A **CI roda exatamente estes comandos** — falhar bloqueia o merge.

## O que a CI executa
<Pipeline em ordem: lint → análise estática → unidade → integração → aceite → cobertura (relatório).
Mais a regra SDD: falhar PR que altera código sem spec aprovada.
**Cobertura e análise estática são publicadas como artefatos do PR** — evidência rastreável do
resultado de qualidade, que o `/metricas` consome para a tendência.>
