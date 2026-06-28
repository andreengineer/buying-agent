---
name: spec
description: Contrato da feature (critérios de aceite). Base enquanto a feature está ativa.
alwaysApply: true
---

# Spec — Cota de uso por organização

> **Fonte da verdade.** Status: aprovado.

## Resumo
Cada organização tem uma cota de requisições por janela de tempo. Ao estourar, a API
responde 429 com headers de cota até a janela reiniciar.

## Critérios de aceite

### AC-1: requisição dentro da cota é aceita
- **Dado** uma org com cota de 1000/min e uso atual de 999
- **Quando** ela faz 1 requisição
- **Então** a requisição é encaminhada para inferência
- **E** a resposta inclui `X-Quota-Remaining: 0`

### AC-2: requisição acima da cota é recusada
- **Dado** uma org com cota de 1000/min e uso atual de 1000
- **Quando** ela faz 1 requisição
- **Então** a API responde `429 Too Many Requests`
- **E** inclui `Retry-After` com os segundos até o reset da janela
- **E** emite o evento `QuotaExceeded`

### AC-3: janela reinicia a contagem
- **Dado** uma org que estourou a cota na janela anterior
- **Quando** uma nova janela começa
- **Então** o uso volta a 0 e novas requisições são aceitas

### AC-4: indisponibilidade do contador faz fail-open
- **Dado** que o contador de uso (Redis) está indisponível
- **Quando** uma org faz uma requisição
- **Então** a requisição é aceita (fail-open)
- **E** um alerta de degradação é emitido

## Matriz de decisão
> Como a checagem combina flag + modo + estado do contador, a tabela-verdade resolve a
> combinatória sem prosa. Cada linha é um caso de teste; AC-3 (reinício da janela) é temporal
> e fica nos critérios acima.

| `usage_quota_enabled` | Modo | Uso vs cota | Contador (Redis) | Resultado | AC |
|---|---|---|---|---|---|
| `false` | — | — | — | Aceita; checagem pulada | borda |
| `true` | shadow | estourou | ok | Aceita + emite métrica; **não** bloqueia | borda |
| `true` | normal | dentro | ok | Aceita + `X-Quota-Remaining` | AC-1 |
| `true` | normal | estourou | ok | `429` + `Retry-After` + evento `QuotaExceeded` | AC-2 |
| `true` | normal | — | indisponível | Aceita (fail-open) + alerta de degradação | AC-4 |

## Casos de borda e erros
- Cota configurada como 0 ou negativa → rejeitada na validação do domínio (config inválida).
- Demais combinações de flag/modo/contador: ver a **matriz de decisão** acima.

## Fora de escopo
- Cobrança por excedente.
- Cota por usuário individual.

## Rastreabilidade
- Product: `./product.md` · Design: `./design.md` · Domínio: `./domain.md`
- ADR a criar: ADR-0002 (janela fixa vs deslizante)
