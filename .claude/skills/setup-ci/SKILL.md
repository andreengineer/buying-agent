---
name: setup-ci
description: Use para criar ou ajustar a pipeline de CI/CD que materializa os gates SDD — lint, análise estática (type-check/complexidade/SAST), testes (unidade/integração/aceite) e cobertura a partir de docs/engineering/TESTING.md, com cobertura e análise estática publicadas como artefatos, mais a regra "falha PR sem spec aprovada". Detecta GitHub Actions / GitLab CI / outro. Gera o arquivo só com aprovação. Acione com /setup-ci.
---

# Skill: Setup de CI/CD (gates SDD na pipeline)

Materializa os gates SDD na esteira automática — é onde "documento que o time tenta seguir" vira
"regra que o sistema garante". **Idempotente**: re-rodar ajusta a pipeline existente.

## Descubra o alvo
- Detecte o provedor (GitHub Actions / GitLab CI / Bitbucket / outro) pelo repo e por `integrations.md`.
- Leia `docs/engineering/TESTING.md` (comandos de gate) e o quality gate do `CLAUDE.md` (cobertura mínima).

## Proponha a pipeline (confirme antes de gerar)
Estágios em ordem; falhar **bloqueia o merge**:
1. **Lint/format** → 2. **Análise estática** (type-check + complexidade + SAST) → 3. **Unidade** →
   4. **Integração** → 5. **Aceite** (um por `AC-N`) → 6. **Cobertura** (mín. do `CLAUDE.md`).
7. **Regra SDD:** PR que altera código **sem spec aprovada** em `specs/` → falha (job que checa a
   presença/status da spec correspondente à mudança).

**Evidência rastreável:** publique **cobertura e análise estática como artefatos** do run (e, se o
provedor permitir, como check/comentário no PR). O resultado de qualidade fica anexado à mudança e
alimenta a tendência do `/metricas`.

## Gere
- O arquivo da pipeline (`.github/workflows/*.yml` / `.gitlab-ci.yml`) usando os comandos de
  `docs/engineering/TESTING.md` — não invente comandos; reuse os de lá.
- ⚠️ **Sem segredos no arquivo** — use os secrets do provedor. Confirme antes de escrever.
- Registre a escolha de pipeline como **ADR** se for estrutural; aponte em `docs/engineering/agentic-layer.md`.

## Próximo passo
Combine com `/revisar-pr` (gate humano/agente). Juntos cobrem **review + automação**: a CI garante
os testes/cobertura/spec; o `/revisar-pr` garante a conformidade de processo no PR/MR.
