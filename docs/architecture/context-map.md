---
name: context-map
description: Bounded contexts e relações. Puxe ao modelar ou cruzar contextos.
alwaysApply: false
---

# Context Map

> Visão DDD estratégica: os bounded contexts do sistema e como se relacionam.
> Atualize quando uma feature cria/move fronteiras. Combine com diagramas C4 se útil.

## Bounded Contexts
| Contexto   | Subdomínio (core/supporting/generic) | Responsabilidade        | Dono |
|------------|--------------------------------------|-------------------------|------|
| <Contexto> | core                                 | <o que ele decide>      | <time>|

## Relações entre contextos
> Padrões de integração DDD: Customer/Supplier, Conformist, Anti-Corruption Layer (ACL),
> Shared Kernel, Open Host Service, Published Language.

```
[Contexto A] ──(ACL)──► [Contexto B]
     │
     └──(Customer/Supplier)──► [Contexto C]
```

| Upstream   | Downstream | Padrão              | Por quê |
|------------|------------|---------------------|---------|
| <A>        | <B>        | Anti-Corruption Layer | <protege o modelo de B> |

## Diagramas
Os diagramas de arquitetura de alto nível (contexto C4, containers, mapa de contextos) ficam em
[`diagrams.md`](./diagrams.md) — gere/atualize com a skill `/diagramar`.
