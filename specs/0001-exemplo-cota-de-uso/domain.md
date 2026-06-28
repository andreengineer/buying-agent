---
name: domain
description: Modelo DDD da feature. Puxe ao modelar agregados e linguagem.
alwaysApply: false
---

# Domain Model (DDD) — Cota de uso por organização

## Bounded Context
**Usage Metering** — subdomínio **supporting** (necessário para proteger a plataforma,
mas não é o diferencial competitivo do produto).

## Linguagem ubíqua
| Termo            | Definição                                                | NÃO confundir com |
|------------------|----------------------------------------------------------|-------------------|
| Quota            | Limite máximo de requisições de uma org por janela        | Rate limit (borda/IP) |
| Window (janela)  | Intervalo de tempo fixo em que o uso é contado e zerado   | Sessão            |
| Usage            | Contagem de requisições de uma org na janela atual        | Billing/cobrança  |
| Exceeded         | Estado em que `usage ≥ quota`                             | Erro de sistema   |

## Agregados, entidades e value objects
- **Agregado `OrganizationUsage`** (raiz: `OrganizationUsage`)
  - Identidade: `OrganizationId`
  - Value objects: `Quota`, `Window`, `UsageCount`
  - **Invariantes:**
    - `UsageCount ≥ 0`
    - `Quota > 0`
    - request é aceita ⇔ `UsageCount < Quota` no momento da checagem
  - Fronteira de consistência: a contagem de uma org muda atomicamente (INCR).

## Eventos de domínio
| Evento                 | Disparado quando        | Quem reage                          |
|------------------------|-------------------------|-------------------------------------|
| `QuotaExceeded`        | `usage` atinge `quota`  | observabilidade (métrica), notificação opcional |
| `WindowReset`          | janela expira           | reinicia `UsageCount` para a org    |

## Relações com outros contextos
- **Inference** (downstream): consome a decisão via `CheckQuota`. Padrão Customer/Supplier —
  Inference é cliente, Usage Metering é fornecedor do veredito.
- Nenhum acoplamento de modelo: a borda só recebe um booleano + metadados de cota.
