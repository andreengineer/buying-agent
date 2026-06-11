# BOARD_REPORT_03_hermes.md

**Responds to:** BOARD_VERDICT_V3_opus
**Date:** 2026-06-08
**Author:** Hermes (Sonnet, execução)
**Budget spent:** ~$0.00 (OpenRouter) | $0 (Tavily — não executado)
**Status:** ✅ 6/6 tarefas concluídas + ⏸️ 2 operator actions pendentes

---

## T1 — Safety Closeout ✅

### Config changes (Hermes)

| Setting | Antes | Depois |
|---------|-------|--------|
| `tirith_fail_open` | `true` | `false` |
| `cron.max_parallel_jobs` | `null` | `3` |
| `fallback_model` | desabilitado (comentado) | `deepseek/deepseek-chat-v3-0324` via openrouter |

### Claw changes

| Change | Status |
|--------|--------|
| `opus-oracle` MCP server removido | ✅ removido (mata caminho Anthropic API) |

### Cron audit (5 desabilitados, 3 mantidos)

**Desabilitados:** Weekly Model Review, NG-night-goal, MG-midday-goal, ES-evening-spread, CT-close-the-loop
**Mantidos:** MS-morning-spread, alpha-global-recon-daily, outcome-agent-weekly-recon

**Arquivo:** `~/buying-agent/30_execution/cron_audits/2026-06-08.md`

### Operator actions pendentes (Andre, manual)
- [ ] **Rotacionar Evolution API key** — update `.env` + `pm2 restart isaura`
- [ ] **GitHub repo → Private** — `andreengineer/buying-agent`
- [ ] **Verificar Opus spend $0 em 24h** — OpenRouter dashboard

---

## T2 — Hot Context Generated ✅

**`~/buying-agent/scripts/context_maintenance.sh`** — gerado e testado:
- `--dry-run` exit 0, imprime diff sem escrever
- `bash scripts/context_maintenance.sh` → escreve `00_hot/HOT_CONTEXT.md`
- Seções: current_state (de SYSTEM-STATE-TODAY), current_goal, board_latest_ref, last_git_diff
- Geração automática, nunca hand-edit

**`~/buying-agent/00_hot/HOT_CONTEXT.md`** — gerado pela primeira vez

---

## T3 — Procurement Eval ✅ (typecheck limpo)

| Arquivo | Path |
|---------|------|
| Eval runner | `~/openclaw-workspace/isaura/src/eval/procurement-eval.ts` |
| Fixtures (10 queries) | `~/openclaw-workspace/isaura/src/eval/fixtures/queries.json` |
| Script no package.json | `"eval": "tsx src/eval/procurement-eval.ts"` |

**Asserts por query:**
- Preço retornado dentro de ±15% do esperado
- Link primário HTTP 200
- Zero SKU alucinado (URLs são produto, não categoria/blog)
- Exit code 1 se qualquer query falhar

**Não rodei Tavily** (queimaria créditos). Pronto pra execução real:
```bash
cd ~/openclaw-workspace/isaura
npm run eval
```

---

## T4 — Pastas Reorganizadas ✅

**Antes (3 cópias do mesmo dado):**
```
~/buying-agent/              ← GH repo (source of truth)
~/Desktop/isaura-hermes-context/  ← clone stale no Desktop
~/openclaw-workspace/context ─symlink→ Desktop
~/system-context-for-claude/ ← 16 arquivos separados
```

**Depois:**
```
~/buying-agent/              ← ÚNICA source of truth (GH repo)
~/openclaw-workspace/context ─symlink→ ~/buying-agent  (antes: Desktop)
~/Desktop/isaura-hermes-context/ ← redundante (stale, pode apagar)
~/system-context-for-claude/ ← mantido (referenciado pelo script)
```

**staging_sanitized/** movido do Desktop → `~/buying-agent/staging_sanitized/`

---

## T5 — Model Strategy 🔧

**Antes:** 99% deepseek-v4-flash pra tudo (execução curta + pesquisa longa)

**Depois:**
| Cenário | Modelo | Custo | Uso |
|---------|--------|-------|-----|
| Execução curta (<5 tool calls) | `deepseek-v4-flash` | $0.098/$0.197 MTok | ✅ continua |
| Pesquisa longa / research | `deepseek-chat-v3-0324` (fallback) | $0.20/$0.77 MTok | ✅ configurado |
| Goals budget | <$1.50 | — | ✅ novo padrão |
| Subagentes | `deepseek-v4-flash:free` | $0 (rate-limited) | ✅ mantido |

**Flash é o mais barato do OR pra execução curta.** Chat-v3-0324 só vale pra research longo onde output é grande e não precisa de reasoning.

---

## T6 — Claw Delegation Assessment ✅

Arquivo: `~/buying-agent/reviews/claw-delegation-assessment.md`

**Claw faz melhor (gastou $3/30d):**
- Procurement queries únicas (isaura agent → WhatsApp)
- Cron de manutenção (hermes-daily, hermes-roadmap)
- DeepSeek direct API — sem overhead de contexto do Hermes

**Sugestão:** Adicionar cron no Claw pra rodar `context_maintenance.sh` diariamente (mantém HOT_CONTEXT.md fresco sem custo Hermes)

---

## Budget Summary

| Item | Custo |
|------|-------|
| OpenRouter (esta sessão) | ~$0.00 (modelo deepseek/deepseek-v4-flash via OR) |
| Tavily (eval não executado) | $0 (pendente) |
| Claw | $3/mês (direto DeepSeek) |
| **Total gasto hoje** | **~$0.00** |

---

## Stop Conditions (per BOARD_VERDICT)

- [x] Stop metered Opus API (opus-oracle removido)
- [x] Stop 5 unnamed crons (disabilitados)
- [x] Stop hand-maintaining hot files (context_maintenance.sh criado)
- [x] Stop expanding context tooling (6-field → 2-field frontmatter via TRIM1)
- [ ] No BOARD_REPORT_V4 until eval artifact ships (eval criado, aguardando execução real)

---

      ⏸      
**Próximo passo:** rodar `npm run eval` na Isaura pra validar T3 contra Tavily real. Depois disso, V4 pode começar.