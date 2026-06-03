# RUNBOOK_browser_spread.md — Browser LLM Spread Protocol

**Type:** Human-relay (Marcela executes) + Opus chairman convergence
**Source migrated from:** `/home/a/openclaw-workspace/premium-ui-spread/`

---

## What this is

The browser spread is the **UI-only** orchestration path — for models that have no public API
(Manus, GPT-5 UI, Perplexity Pro) or when API quota is exhausted.

It is NOT agent code. It is a **Marcela protocol** + Opus chairman synthesis.

---

## Two spread modes

### Mode A — Parallel (use when: fast cross-validation, independent domains)

```
Claude starts → all models work simultaneously → Opus receives all outputs → convergence

Slot    Model           Role
─────   ─────────────   ────────────────────────────────
1       Manus           Execution & Deploy Pipeline
2       Gemini 2.0      Image HD + Vision Description
3       GPT-5 UI        Architecture + Data Lake
4       Perplexity Pro  Market + Competition Research
Opus    Chairman        Reads all 4 → final_alpha_launch.md
```

**When to use:** Decision needs breadth. Each slot gets a different domain.
Each model receives the same `context.json` + role-specific prompt.

### Mode B — Linear chain (use when: complex topic, low hallucination required)

```
Potent model → suggest → next model critiques → compresses → next model concludes

Step    Model           Input                       Output
────    ─────────────   ─────────────────────────   ────────────────────────
1       Claude Opus     bare topic                  structured suggestion vector
2       GPT-5 UI        step 1 output               critique + additions
3       DeepSeek R1     step 1+2 compressed         reasoning chain + conclusion
4       Opus            compressed chain             final synthesis (chairman)
```

**When to use:** Architecture decisions, strategy debates, anything where hallucination compounds.
Each step receives the COMPRESSED output of all prior steps, not raw.

---

## Marcela Instructions (PT-BR)

### Parallel spread — Passo a passo

**Passo 1:** Abra 4 abas no navegador.

**Passo 2:** Em cada aba, abra o site e cole o prompt que o André mandar:
- Aba 1: manus.ai → cole `inputs/manus.md` + `context.json`
- Aba 2: gemini.google.com → cole `inputs/gemini.md` + `context.json`
- Aba 3: chatgpt.com → cole `inputs/gpt.md` + `context.json`
- Aba 4: perplexity.ai → cole `inputs/perplexity.md` + `context.json`

**Passo 3:** Quando cada IA terminar, copie a resposta inteira.
Salve em:
- Aba 1 → `outputs/manus-output.md`
- Aba 2 → `outputs/gemini-output.md`
- Aba 3 → `outputs/gpt-output.md`
- Aba 4 → `outputs/perplexity-output.md`

**Passo 4:** Abra claude.ai (Claude Pro). Cole:
1. O template `templates/final_alpha_launch.md`
2. Os 4 arquivos de output, um por um

**Passo 5:** Copie a resposta do Claude e mande pro André.

### Linear chain — Passo a passo

**Passo 1:** Abra claude.ai. Cole o prompt que o André mandar. Copie a resposta.

**Passo 2:** Abra chatgpt.com. Cole: resposta do Passo 1 + instrução de crítica do André. Copie a resposta.

**Passo 3:** Abra o terminal. Cole o comando que o André mandar (passa o output pro DeepSeek via API).

**Passo 4:** Volte pro Claude. Cole tudo comprimido. Essa é a resposta final.

Marcela: você não decide o que é "comprimido". André ou Hermes comprimem. Você transporta.

---

## Context files location

```
/home/a/openclaw-workspace/premium-ui-spread/
├── inputs/context.json          ← shared context for all models
├── inputs/manus.md              ← Manus role prompt
├── inputs/gemini.md             ← Gemini role prompt
├── inputs/gpt.md                ← GPT role prompt
├── inputs/perplexity.md         ← Perplexity role prompt
├── templates/final_alpha_launch.md  ← Opus chairman template
└── outputs/                     ← paste results here
```

---

## API vs Browser model registry

See: `manifests/spread_registry.json`

Quick reference:

| Model | API available | Browser UI | Cost/spread |
|---|---|---|---|
| DeepSeek V3.2 | ✅ hermes-cortex | — | $~0.50 |
| DeepSeek R1 | ✅ hermes-cortex | — | $~1.00 |
| Kimi K2 | ✅ hermes-cortex (filter) | — | $~0.50 |
| Qwen 2.5 72B | ✅ hermes-cortex | — | $~0.40 |
| Gemini 2.5 Pro | ✅ hermes-cortex | gemini.google.com | $~1.25 |
| Claude Opus | ❌ no API budget | claude.ai (Pro) | $0 (sunk) |
| GPT-5 | ❌ | chatgpt.com | $0 (sunk) |
| Manus | ❌ | manus.ai | $0 (sunk) |
| Perplexity Pro | ❌ | perplexity.ai | $0 (sunk) |

**Rule:** API-capable models → hermes-cortex `--mode parallel` or `--mode linear`.
Browser-only models → this runbook.

---

## Chairman synthesis

Opus always runs last — never in parallel with subordinate models.
Opus receives compressed outputs and produces the final decision document.
Opus resolves conflicts between model outputs. No vote — chairman decides.

---

_Runbook owner: Andre. Relay operator: Marcela. Agent enforcer: Hermes._
