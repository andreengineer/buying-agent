---
name: tasks
description: Decomposição e gates da feature. Puxe ao implementar.
alwaysApply: false
---

# Tasks — Cota de uso por organização

## Plano
| #  | Task                                                        | Cobre AC | Depende de | Status |
|----|-------------------------------------------------------------|----------|------------|--------|
| 1  | Value objects `Quota`, `Window`, `UsageCount` + invariantes | AC-1,2   | —          | todo   |
| 2  | Agregado `OrganizationUsage` + eventos `QuotaExceeded`/`WindowReset` | AC-2,3 | 1 | todo |
| 3  | Porta `UsageCounter` (domínio) + caso de uso `CheckQuota`   | AC-1,2,3 | 2          | todo   |
| 4  | `RedisUsageCounter` implementando a porta (INCR/EXPIRE)     | AC-3,4   | 3          | todo   |
| 5  | Middleware na borda + headers 429 / `Retry-After`           | AC-1,2   | 3          | todo   |
| 6  | Fail-open + alerta quando contador indisponível             | AC-4     | 4,5        | todo   |
| 7  | Feature flag + modo shadow                                  | —        | 5          | todo   |
| 8  | ADR-0002 (janela fixa vs deslizante)                        | —        | —          | todo   |

## Plano de teste
- Unidade: invariantes de `Quota`/`UsageCount`; transição de estado `Exceeded`.
- Integração: `RedisUsageCounter` com Redis real (testcontainer); reset por TTL.
- Aceite: um teste por AC (AC-1 a AC-4), incluindo fail-open simulando Redis fora.

## Checklist de Definition of Done
- [ ] AC-1 a AC-4 verdes
- [ ] ADR-0002 registrado
- [ ] Glossário atualizado (Quota, Window, Usage, Exceeded)
- [ ] Context-map atualizado (novo contexto Usage Metering)
- [ ] Spec reflete o que foi construído
