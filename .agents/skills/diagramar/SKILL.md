---
name: diagramar
description: Use no discovery para desenhar a arquitetura de ALTO NÍVEL em Mermaid — diagrama de contexto (C4 L1), containers (C4 L2) e o mapa de bounded contexts (DDD). Lê vision, context-map, design e assessment, e gera/atualiza docs/architecture/diagrams.md. Mantém alto nível, sem detalhe de implementação. Acione com /diagramar.
---

# Skill: Diagramar arquitetura (Mermaid, alto nível)

Gera os diagramas de arquitetura em **Mermaid** (renderizam no GitHub e no Claude Code) a partir
dos artefatos de discovery. Mantenha **alto nível**: atores, sistemas, containers e contextos —
nunca classes, tabelas ou detalhe de implementação (isso é escopo do `design.md` da feature).

## Insumos (puxe só o que existir e cite a origem)
- `docs/product/vision.md` — atores/personas e propósito do sistema.
- `docs/architecture/context-map.md` — bounded contexts e relações (DDD).
- `specs/*/design.md` — containers, serviços e integrações.
- `docs/architecture/assessment.md` — as-is, no brownfield.
- **Lacunas** → pergunte (`AskUserQuestion`): atores externos, sistemas vizinhos, principais
  containers (UI/serviços/dados/filas) e a jornada crítica a ilustrar.

## Diagramas (alto nível, alinhado a C4 + DDD)
1. **Contexto do sistema (C4 L1):** o sistema no centro + personas + sistemas externos.
2. **Containers (C4 L2):** apps/serviços, dados, filas e como conversam.
3. **Mapa de bounded contexts (DDD):** contextos e padrões de relação (ACL, Customer/Supplier,
   Conformist, Shared Kernel).
4. *(opcional)* **Fluxo-chave:** uma jornada crítica em `sequenceDiagram`.

> Use `flowchart` (renderiza em todo lugar) ou os diagramas C4 nativos do Mermaid (`C4Context`,
> `C4Container`) se o renderizador suportar. Rótulos na **linguagem ubíqua** do `glossary.md`.

## Saída
- Escreva/atualize `docs/architecture/diagrams.md` (já existe como placeholder; mantenha o
  frontmatter `alwaysApply: false`). Cada diagrama num bloco ` ```mermaid `, com título e 1 linha
  de contexto.
- Garanta o link de volta em `context-map.md`. **Regenere quando a arquitetura mudar** — diagrama
  desatualizado engana mais que ajuda.

## Regras
- **Alto nível only.** Pediram detalhe de classe/tabela? Diga que é escopo do `design.md`.
- **Valide a sintaxe antes de entregar** — rode o gate determinístico (não confie só no olho):
  ```
  node scripts/validate-mermaid.mjs .
  ```
  Pega bloco vazio, tipo de diagrama ausente/desconhecido e aspas/delimitadores desbalanceados.
  Corrija os erros antes de salvar; é o mesmo gate que roda na CI (`esteira.yml`).
- Não invente componentes que não estão nos insumos — pergunte (ver verificação de conhecimento no `CLAUDE.md`).
