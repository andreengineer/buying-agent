---
name: clarificar
description: Use para uma SABATINA — entrevista implacável que transforma intenção difusa em entendimento compartilhado antes de construir. Caminha pela árvore de decisão UMA pergunta por vez, resolvendo dependências entre escolhas, sempre com uma resposta recomendada; explora o codebase/docs em vez de perguntar quando a resposta já existe. Ideal no gate da spec (AC testáveis / Definition of Ready) e do design (decisão difícil de reverter). Produz um resumo de entendimento que alimenta product.md/design.md/spec.md. Chamada por /nova-feature, /kickoff, /roadmap e /validar, ou acione direto com /clarificar.
---

# Skill: Clarificar (sabatina de plano/spec)

Entrevista implacável para **afiar um plano, uma spec ou um design** antes de construir. O alvo é
**entendimento compartilhado**: nenhuma ambiguidade que vire retrabalho ou `SPEC_DEVIATION` depois.
Inspirada na técnica de *grilling* — adaptada ao vocabulário da esteira (AC testáveis, tier,
decisão difícil de reverter → ADR, linguagem ubíqua).

> **Quando usar isto e não "lotes curtos":** o resto da esteira pergunta em **lotes** (`AskUserQuestion`)
> para escolhas **independentes**. A sabatina é o oposto e o complemento: para uma **árvore de decisão
> com dependências**, onde a resposta 3 só faz sentido depois das respostas 1 e 2. Use quando a
> ambiguidade é **profunda e ramificada**, não quando são opções ortogonais.

## Princípios (o motor)
- **Uma pergunta por vez.** Faça a pergunta, **espere a resposta**, e só então a próxima. Várias
  perguntas de uma vez confundem e impedem que cada resposta refine a seguinte.
- **Caminhe pela árvore.** Cada resposta abre/fecha ramos. Resolva **dependências em ordem**: não
  pergunte o "como" antes do "se", nem o detalhe antes da fronteira.
- **Sempre proponha uma resposta recomendada.** Não interrogue no vácuo — para cada pergunta dê sua
  recomendação com o porquê (em `AskUserQuestion`, a primeira opção leva "(Recomendado)").
- **Explore antes de perguntar.** Se a resposta está no **codebase, nos docs (`specs/`, `docs/`,
  ADRs, glossário) ou num MCP de referência conectado**, descubra você mesmo — só pergunte o que
  exige decisão humana. (É a *Verificação de conhecimento* do `CLAUDE.md`.) Nunca invente: incerteza
  explícita > chute confiante.
- **Cave até o testável.** Uma resposta vaga ("rápido", "seguro", "vários") **não fecha o ramo** —
  refine até virar critério verificável (número, caso concreto, Given/When/Then).

## Processo
1. **Enquadre o alvo.** Diga em 1-2 linhas o que está sendo sabatinado (esta feature / este design /
   esta prioridade) e o que será considerado "entendido o bastante para seguir".
2. **Levante os ramos abertos.** A partir do material existente, liste mentalmente as decisões em
   aberto e as ambiguidades. Priorize as de **maior impacto / mais difíceis de reverter**.
3. **Sabatine, um ramo por vez.** Para cada ponto: explore primeiro; se restar decisão, pergunte
   **uma** coisa com a recomendação; integre a resposta; deixe-a abrir os próximos ramos. Repita.
4. **Pare quando a árvore fechar** — sem ramos abertos que mudem o que será construído. Não estenda
   por esporte; quando o usuário e você concordam no escopo, encerre.

## Saída — o entendimento vira artefato
A sabatina **não termina em chat**: consolide o resultado para alimentar a esteira.
- **Resumo de entendimento:** decisões fechadas, não-objetivos que surgiram, premissas e riscos.
- **Direcione ao destino certo** conforme o que foi clarificado:
  - virou **critério de aceite** → `spec.md` (Given/When/Then; regra multifatorial → Matriz de decisão);
  - virou **decisão difícil de reverter** → vira **ADR** (`docs/architecture/adr/`);
  - virou **termo de negócio** → `docs/glossary.md` / `domain.md`;
  - ficou **em aberto de propósito** → `docs/STATE.md` (com o gatilho para reconsiderar).
- Aponte o próximo passo de quem te chamou (preencher o gate, retomar `/nova-feature`, etc.).
