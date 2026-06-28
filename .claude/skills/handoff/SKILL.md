---
name: handoff
description: Use ao PAUSAR/encerrar uma sessão de trabalho (grava o estado atual em docs/STATE.md para retomar depois) ou ao RETOMAR (lê docs/STATE.md e a spec ativa e recompõe o contexto, propondo o próximo passo). Mantém a continuidade entre sessões de humanos e agentes. Acione com /handoff.
---

# Skill: Handoff de sessão (pause / resume)

Mantém a continuidade do projeto via `docs/STATE.md` — a memória de trabalho volátil
(diferente do ADR, que é decisão durável). Detecte a intenção pelo pedido ou pergunte.

## Modo PAUSE (pausar / encerrar)
Atualize `docs/STATE.md` com o estado real desta sessão:
1. **Em andamento / próximo passo** — a feature/spec ativa e a **próxima ação concreta**
   (específica: "implementar AC-3 no adapter X", não "continuar a feature").
2. **Decisões recentes** — o que foi decidido. Se for difícil de reverter, **crie/atualize o ADR**
   e linke; o STATE só resume.
3. **Bloqueios** — o que trava e quem/como destrava.
4. **Ideias adiadas / todos** — o que ficou de fora de propósito, com o gatilho para reconsiderar.
5. Marque a data e o autor. Se houver `SPEC_DEVIATION` aberto, registre como bloqueio.
6. Ofereça um commit (`docs: handoff — atualiza STATE`) se for repositório git.

> Seja conciso e acionável. O STATE é para alguém (ou um agente) retomar frio amanhã.

## Modo RESUME (retomar)
1. Leia `docs/STATE.md` e a `spec.md`/`tasks.md` da feature ativa citada nele.
2. Se houver MCP conectado e relevante (Jira/Confluence), e a trava de conta estiver validada,
   atualize o contexto com o que mudou lá fora.
3. **Resuma onde paramos** em poucas linhas: feature ativa, último passo, bloqueios abertos.
4. **Proponha o próximo passo** (o "Em andamento / próximo passo" do STATE) e confirme com o
   usuário antes de executar.

## Regras
- STATE.md é **volátil**; ADR é **durável**. Não escreva decisão estrutural só no STATE.
- Não invente progresso: relate fielmente o que foi feito, o que falta e o que está bloqueado.
