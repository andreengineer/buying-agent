---
name: validar
description: Use APÓS implementar uma feature para validá-la (UAT) — roda os gates de docs/engineering/TESTING.md, mapeia cada AC-N ao seu teste e aponta ACs sem cobertura, resolve SPEC_DEVIATION pendente, checa o Definition of Done e atualiza docs/STATE.md. Acione com /validar.
---

# Skill: Validar feature (UAT)

Fecha o loop SDD: prova que a implementação cumpre a **spec**, pelo **gate executável** — não por
inspeção. Rode depois de implementar (pode ser em outra sessão).

## Processo
1. **Identifique a feature** (`specs/NNNN-<nome>/`) e leia `spec.md` + `tasks.md`.
2. **Rode os gates** de `docs/engineering/TESTING.md` (e os comandos da coluna Gate do `tasks.md`). O `/verify`
   embutido do Claude Code ajuda a validar comportamento real.
3. **Mapeie `AC-N → teste`** e mostre a tabela; **aponte qualquer AC sem cobertura** ou falhando.
   Se a spec tem **Matriz de decisão**, cada linha é um caso de teste: confira que **toda linha**
   tem teste correspondente (combinações são onde mais escapa bug).
4. **SPEC_DEVIATION:** resolva os pendentes — ou corrige o código (a spec vence) ou atualiza a
   spec conscientemente (e registra ADR se for difícil de reverter). Se a decisão "corrigir vs
   atualizar" tiver ramificações (afeta outros AC, fronteiras, ADRs), rode **`/clarificar`** para
   fechar a árvore antes de escolher.
5. **Definition of Done** (ver `README.md` / `CLAUDE.md`): AC verdes pelo gate, sem deviation
   aberto, ADRs registrados, glossário/context-map atualizados, spec fiel.
6. **Atualize `docs/STATE.md`** (próximo passo / decisões) — ou rode `/handoff` para encerrar.

## Saída
Veredito claro: **pronto para merge** ou a lista do que falta (AC sem cobertura, deviation aberto,
item de DoD pendente). Se há MCP de escrita validado, ofereça atualizar a issue/página da feature.
