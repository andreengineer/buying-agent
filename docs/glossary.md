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
| Claw | Instância do Hermes para cron jobs e automação de rotina | Isaura, Hermes | Infrastructure |
| CodeSpar | Catálogo de 110+ MCP servers para agentes comerciarem (pagamentos, fiscal, logística) | Stripe | Integrations |
| Especificação (Spec) | Fonte da verdade — critérios de aceite (Given/When/Then) que contratam a implementação | Documentação técnica | SDD |
| Hermes Agent | Plataforma de agentes autônomos — gateway, ferramentas, TUI, MCP | Isaura, Claw, Agente de Compras | Platform |
| Isaura | Agente de compras e pesquisa (Express + React + PostgreSQL) | Hermes, Claw | Domain |
| MCP (Model Context Protocol) | Protocolo para agentes LLM consumirem ferramentas/serviços externos | API REST | Infrastructure |
| SPEC_DEVIATION | Divergência entre spec e código — ou corrige o código (spec vence) ou atualiza a spec com ADR | Bug, erro | SDD |
| SDD (Spec-Driven Development) | Metodologia onde a spec é o contrato que dirige implementação e testes | TDD, BDD | SDD |

<!-- Mantenha em ordem alfabética. Cada linha deve ter um dono mental claro. -->
