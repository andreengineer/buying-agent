---
name: glossary
description: Linguagem ubíqua. Puxe ao nomear, modelar domínio ou escrever specs.
alwaysApply: false
---

# Glossário — Linguagem Ubíqua

> A fonte única do vocabulário do sistema. O mesmo termo aparece aqui, na spec e no código.
> Termo novo introduzido por uma feature → adicione no mesmo PR. Sem sinônimos.

| Termo        | Definição                                      | NÃO confundir com | Contexto (bounded context) |
|--------------|------------------------------------------------|-------------------|----------------------------|
| Agente (Agent) | Sistema autônomo que executa tarefas em nome do usuário usando LLMs + ferramentas | Agente (humano) | Core |
| Agente de Compras (Buying Agent) | Instância do Hermes configurada para orquestrar compras | Isaura, Claw | Core |
| Autonomy level (A0–A3) | Quanto o agente faz na compra: A0 pesquisa + link; A1 checkout até o pagamento, humano paga; A2 agente paga ≤ PIX_CEIL de conta dedicada; A3 regras recorrentes | Budget governor | Core |
| Claw | Instância do Hermes para cron jobs e automação de rotina | Isaura, Hermes | Infrastructure |
| CodeSpar | Catálogo de 110+ MCP servers para agentes comerciarem (pagamentos, fiscal, logística) | Stripe | Integrations |
| Especificação (Spec) | Fonte da verdade — critérios de aceite (Given/When/Then) que contratam a implementação | Documentação técnica | SDD |
| Family cohort (Coorte familiar) | Grupo de parentes do André usando o agente de compras numa rodada de descoberta de 7 dias | Design partner (Beta, pagante) | Discovery |
| Focus block (Bloco de foco) | Evento no calendário com 1 task, estimativa em minutos e critério de pronto. `[V/S/M]` = bloco do André (ocupado); `[bot]` = run de agente (livre) | Reunião | Focus |
| Hermes Agent | Plataforma de agentes autônomos — gateway, ferramentas, TUI, MCP | Isaura, Claw, Agente de Compras | Platform |
| Isaura | Agente de compras e pesquisa (Express + React + PostgreSQL) | Hermes, Claw | Domain |
| Landed cost | Preço + frete até o CEP do pedido (+ taxas). Base de comparação entre ofertas | Preço de vitrine | Core |
| MCP (Model Context Protocol) | Protocolo para agentes LLM consumirem ferramentas/serviços externos | API REST | Infrastructure |
| Output layers (L1/L2/L3) | L1 imagem 9:16 com ≤ 6 opções; L2 tabela top-3 em texto no chat; L3 relatório completo (PDF/web) com scorecard | Autonomy level | Core |
| Parking lot | Lista de ideias capturadas com `/park` durante um bloco; triada (manter/matar) na revisão de domingo | Backlog | Focus |
| PIX_CEIL | Saldo máximo pré-carregado da conta dedicada de pagamento. O raio de dano = o saldo | Orçamento do pedido | Core |
| Scorecard | Avaliação ponderada das ofertas por perfil de categoria (qualidade, valor, confiança, popularidade, prazo, garantia) | Rating (nota 1–5 do solicitante) | Core |
| SPEC_DEVIATION | Divergência entre spec e código — ou corrige o código (spec vence) ou atualiza a spec com ADR | Bug, erro | SDD |
| SDD (Spec-Driven Development) | Metodologia onde a spec é o contrato que dirige implementação e testes | TDD, BDD | SDD |

<!-- Mantenha em ordem alfabética. Cada linha deve ter um dono mental claro. -->
