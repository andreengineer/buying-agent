# Claw Task Delegation — BOARD_VERDICT_V3 Assessment

## Current Claw State
- **Price (direct DeepSeek):** flash $0.14/$0.28 per 1M | via OpenRouter (Hermes): $0.098/$0.197
- **Total spend 30d:** ~$3
- **Models:** DeepSeek V4 flash (direct)
- **Active crons (4):** llm-leaderboard-weekly, hermes-daily, hermes-roadmap, hermes-implement
- **Agents:** isaura (default), hermes
- **Channels:** Telegram + WhatsApp (Evolution API)

## What Claw Does Better Than Hermes

| Task Type | Winner | Why |
|-----------|--------|-----|
| **Procurement query (single)** | Claw (isaura) | Já integrado ao WhatsApp/Evolution, sem overhead de agente |
| **Daily health check** | Claw (hermes-daily) | Já configurado, $0.05/dia |
| **Cron leve (<10 tool calls)** | Claw | Sem contexto do Hermes, começa limpo |
| **Pesquisa web + síntese** | Claw | Perplexity configurado, custo fixo baixo |
| **WhatsApp delivery** | Claw (Evolution) | Já tem canal aberto |

## What Hermes Does Better Than Claw

| Task Type | Winner | Why |
|-----------|--------|-----|
| **Board review / decisão** | Hermes | Skills, memória, ferramentas de terminal/arquivo |
| **Code review + debug** | Hermes | Acesso ao sistema de arquivos completo, git |
| **Config changes** | Hermes | `hermes config set`, acesso ao config.yaml |
| **Eval runs** | Hermes | Precisa executar TypeScript, npm test |
| **Multi-step reasoning** | Hermes | 90 turns, delegation, subagentes |
| **Criação de skills** | Hermes | skill_manage tool |

## Recommended Delegation

1. **Context maintenance cron** → Claw (add cron pra rodar `context_maintenance.sh` diariamente)
2. **Procurement queries via WhatsApp** → Claw (já funciona, isaura agent)
3. **Long research scans** → Claw (sem OpenRouter markup, DeepSeek direct)
4. **Code/Config tasks** → Hermes (precisa de ferramentas específicas)

## Claw $ Advantage
Claw gasta ~$0.10/dia em operação normal. A vantagem NÃO é preço por token (OpenRouter é mais barato pra flash via desconto OR), mas sim:
- **Menos tokens por call** (contexto não carrega skills/memórias do Hermes)
- **Sem overhead de subagentes**
- **DeepSeek direct = sem risco de rate-limit do OR free tier**