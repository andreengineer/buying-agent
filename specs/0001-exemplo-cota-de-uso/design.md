---
name: design
description: Technical Design Doc — 5 eixos + tabelas de dependências, solução, riscos e roadmap, com links ao repo de artefatos do time. Puxe ao desenhar feature arquitetural.
alwaysApply: false
---

# Technical Design Doc — Cota de uso por organização

> **Tier:** arquitetural · **Status:** aprovado · **Autor:** Igor · **Data:** 2026-06-18

## Links e artefatos
| Artefato                 | Onde                | Link                                         |
|--------------------------|---------------------|----------------------------------------------|
| Página do design         | Confluence          | acme.atlassian.net/wiki/…/usage-quota        |
| Issue / épico            | Jira                | PLAT-481                                      |
| Repo de artefatos        | wiki do time        | wiki/platform/rate-limiting                   |
| Spec · Product · Domínio | repositório         | `./spec.md` · `./product.md` · `./domain.md`  |

## Contexto da funcionalidade
A API de inferência não tem isolamento por org — picos de uma conta degradam todas (3 incidentes
P2 no trimestre). Esta feature limita o uso por organização por janela de tempo. Ver `./product.md`.

## Goals / Non-goals
**Goals**
- Contagem de uso por org com janela configurável e limite por org.
- Decisão de aceitar/recusar em < 5ms (não pode virar gargalo).

**Non-goals**
- Persistência durável do contador (perda em restart é tolerável).
- Cobrança por excedente.

## Glossário (da funcionalidade)
| Termo      | Descrição                                              |
|------------|--------------------------------------------------------|
| Quota      | Limite máximo de requisições de uma org por janela     |
| Window     | Intervalo fixo em que o uso é contado e zerado         |
| Usage      | Contagem de requisições da org na janela atual         |
| Exceeded   | Estado em que `usage ≥ quota`                          |

## Design proposto
Novo bounded context **Usage Metering** (supporting). Um value object `Quota` e o agregado
`OrganizationUsage` mantêm a contagem por janela. Um middleware em `interfaces/` consulta o caso
de uso `CheckQuota` antes de encaminhar para inferência. Contador em **Redis** (INCR + EXPIRE por
janela) atrás de uma porta `UsageCounter` definida no domínio — o domínio não conhece Redis.

```
[API edge] → interfaces/middleware → application/CheckQuota
                                         → domain/OrganizationUsage (regra)
                                         → infrastructure/RedisUsageCounter (porta)
```

## Cobertura dos 5 eixos
### 1. Tech stack
Introduz **Redis** como datastore do contador. Sem outras libs novas.
### 2. Arquitetura base
Novo bounded context **Usage Metering** (supporting). Porta `UsageCounter` no domínio, adapter na
infra — segue a regra de camadas. Relação Customer/Supplier com o contexto Inference.
### 3. Infra
Redis gerenciado (INCR/EXPIRE). Feature flag `usage_quota_enabled` por org. **Rollout:** shadow
mode (conta, não bloqueia) → 5% → 100%. **Reversão:** desligar a flag (efeito imediato).
### 4. Qualidade
Unidade (invariantes de `Quota`/`UsageCount`); integração (`RedisUsageCounter` com testcontainer);
aceite (um teste por `AC-N`, incluindo fail-open). Gate de latência < 5ms.
### 5. Observabilidade
Métricas `quota_checks_total`, `quota_exceeded_total{org}`, histograma de latência do check.
Alerta quando o fail-open ativar. SLO: p95 do check < 5ms.

## Mapa de dependências
| Dependência         | Tipo                 | Descrição                              | Principais métodos / endpoints |
|---------------------|----------------------|----------------------------------------|--------------------------------|
| Redis               | datastore / cache    | contador de uso por org, TTL por janela| `INCR` · `EXPIRE` · `GET`      |
| API de Inferência   | serviço interno (downstream) | consome o veredito de `CheckQuota`     | recebe `allow: bool` + headers |

## Solução
| #  | Tarefa / bloco                          | Descrição                              | Status      |
|----|-----------------------------------------|----------------------------------------|-------------|
| 1  | Value objects `Quota`/`Window`/`UsageCount` | invariantes do domínio              | definido    |
| 2  | Agregado `OrganizationUsage` + eventos  | `QuotaExceeded` / `WindowReset`        | definido    |
| 3  | Porta `UsageCounter` + `RedisUsageCounter` | INCR/EXPIRE por janela              | definido    |
| 4  | Middleware na borda + `429`/`Retry-After` | gate antes da inferência             | definido    |
| 5  | Fail-open + alerta                      | comportamento quando o Redis cai       | definido    |
| 6  | Custo do Redis em alta escala           | dimensionar chaves/sharding            | indefinido  |

## Alternativas consideradas
| Alternativa               | Prós                        | Contras                       | Por que (não) escolhida |
|---------------------------|-----------------------------|-------------------------------|-------------------------|
| Redis (escolhida)         | rápido, TTL nativo, simples | dependência externa           | ✅ atende SLA de 5ms |
| Contador em memória local | zero dependência            | não funciona com N réplicas   | ❌ inconsistente |
| Postgres                  | durável                     | latência alta no hot path     | ❌ vira gargalo |

## Trade-offs e consequências
Aceitamos perder a contagem em restart do Redis (a janela reinicia) em troca de simplicidade e
latência. Para cotas de proteção, é aceitável.

## Riscos
| Risco                  | Descrição                       | Prob. × Impacto | Ações / mitigações                     |
|------------------------|---------------------------------|-----------------|----------------------------------------|
| Redis indisponível     | contador fora do ar             | baixa × alto    | fail-open (permite request) + alerta   |
| Janela mal configurada | cota 0/negativa                 | média × médio   | validação no domínio + default seguro  |
| Custo do Redis sob pico | muitas orgs × muitas chaves    | baixa × médio   | TTL curto; avaliar sharding (Onda 2)   |

## Roadmap da feature
| Fase / onda | Entrega                                  | Quando       | Depende de |
|-------------|------------------------------------------|--------------|------------|
| 1 (MVP)     | shadow mode (conta, não bloqueia) + `429`| sprint atual | —          |
| 2           | rollout 5% → 100% + alerta de fail-open  | próximo      | 1          |
| 3           | avaliar janela deslizante / sharding     | depois       | 2          |

## Questões em aberto
- [ ] Janela fixa ou deslizante no MVP? → **decidido: fixa** (registrar ADR-0002).
