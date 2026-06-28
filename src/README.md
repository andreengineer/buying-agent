---
name: src
description: Regra de camadas DDD. Puxe ao estruturar ou implementar código.
alwaysApply: false
---

# src/ — Estrutura em camadas (DDD tático)

Agnóstico de linguagem. Crie subpastas/módulos equivalentes na sua stack, mas
**preserve a regra de dependência**: as setas apontam só para dentro.

```
interfaces ──► application ──► domain ◄── infrastructure
```

| Camada            | Responsabilidade                                   | Pode depender de         |
|-------------------|----------------------------------------------------|--------------------------|
| `domain/`         | Entidades, value objects, eventos, regras/invariantes | **nada** (sem framework/IO) |
| `application/`    | Casos de uso, orquestração, portas (interfaces)    | `domain/`                |
| `infrastructure/` | Repos, adapters, integrações (implementa as portas)| `domain/`, `application/`|
| `interfaces/`     | Borda: API, CLI, UI, controllers                   | `application/`           |

## Por que essa regra
- O domínio é a parte mais valiosa e mais estável — não pode depender de detalhes
  voláteis (banco, HTTP, SDKs). Detalhes dependem do domínio, nunca o contrário.
- Permite testar regras de negócio sem subir infraestrutura.
- Trocar banco/framework vira mudança só em `infrastructure/`.

> Inversão de dependência: a porta (interface) é declarada em `application/` ou `domain/`;
> a implementação concreta vive em `infrastructure/`.
