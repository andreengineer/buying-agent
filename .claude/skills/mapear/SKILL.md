---
name: mapear
description: Use para mapear um codebase existente (brownfield) e produzir docs/architecture/assessment.md — stack, arquitetura, bounded contexts implícitos, maturidade nos 5 eixos, dívidas/riscos e decisões históricas a virar ADR retroativo. Re-execução atualiza o assessment. É chamada pelo /kickoff no modo brownfield, e também roda sozinha quando o codebase mudar ou para analisar um repo. Acione com /mapear.
---

# Skill: Mapear o estado atual (as-is)

Produz o retrato de um projeto **já em andamento**. Primeiro **leia o código**, depois pergunte
só o que o código não revela. É **idempotente**: re-rodar atualiza `docs/architecture/assessment.md`.

## Processo
1. **Mapeamento automático:** identifique stack, estrutura de pastas, estilo de arquitetura,
   acoplamentos, testes/CI, logs/métricas/tracing. Infira os **bounded contexts implícitos** a
   partir da organização do código. Em repos grandes, **delegue a varredura a um subagente** de
   exploração (ver `docs/engineering/_templates/subagent.template.md`) para manter o contexto enxuto.
2. **Insumos externos (se houver):** se `/integracoes` conectou GitHub/cloud/Confluence (conta
   validada), use para enriquecer o as-is. Cite a origem.
3. **Entrevista de lacunas** (`AskUserQuestion`): intenção de negócio e North Star atuais;
   maiores dores/riscos hoje; termos de domínio que confundem o time; o que NÃO pode quebrar;
   contexto e tamanho do time.
4. **Gap analysis:** compare o as-is com o padrão SDD nos 5 eixos (tech stack, arquitetura, infra,
   qualidade, observabilidade). Marque risco (baixo/médio/alto).
5. **Decisões históricas:** liste escolhas estruturais já feitas sem registro → viram **ADR
   retroativo** (status: aceito, registrando o porquê histórico).

## Saídas
- `docs/architecture/assessment.md` (use `docs/architecture/_templates/assessment.template.md`).
- Lista de ADRs retroativos a criar em `docs/architecture/adr/`.

## Próximo passo
- Dentro do `/kickoff`: devolva o assessment + gaps para alimentar os 5 eixos e o roadmap.
- Sozinha: sugira `/roadmap` (priorizar as dívidas mapeadas) ou `/camada-agentica`.
