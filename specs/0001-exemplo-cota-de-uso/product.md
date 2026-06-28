---
name: product
description: PRD-lite da feature (por quê e para quem). Puxe ao abrir feature arquitetural.
alwaysApply: false
---

# Product — Cota de uso por organização

> **Tier:** arquitetural · **Status:** aprovado · **Dono:** Igor
> *(Exemplo didático preenchido. Substitua por features reais.)*

## Problema
Algumas organizações consomem volume desproporcional da API de inferência, degradando
latência para todas as outras. Hoje não há limite por organização — picos de uma conta
viram incidente de plataforma. Evidência: 3 incidentes P2 no último trimestre originados
por uma única org.

## Para quem
Todas as orgs do plano pago (~120 contas). Afeta diretamente as ~8 contas de alto volume
e indiretamente todas que dividem a infraestrutura.

## Resultado esperado / métrica de sucesso
- Métrica: p95 de latência da API durante picos de uma org.
- Baseline: até 4s sob pico → Alvo: ≤ 1,2s (isolamento por cota).
- Métrica secundária: zero incidentes P2 por "org barulhenta".

## Goals
- Limitar requisições por org a uma cota configurável por janela de tempo.
- Resposta clara (429 + headers) quando a cota estoura.

## Non-goals
- Billing/cobrança por excedente (feature separada).
- Cotas por usuário individual dentro da org.
- Rate limiting por IP (camada de borda já cobre).

## Riscos / premissas
- Premissa: cota por org (não por usuário) é granularidade suficiente. Se falsa,
  o modelo de domínio muda.
