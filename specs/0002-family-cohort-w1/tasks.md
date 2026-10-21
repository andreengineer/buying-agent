---
name: tasks
description: Task split for 0002 between Claude Code (orchestrator) and Codex gpt-6.1-sol (implementer) — exclusive paths, branches, gates. Pull when dispatching or implementing.
alwaysApply: false
---

# Tasks — Family cohort #1

> One task = one branch `t/0002-<n>-<slug>` cut from `feat/0002-family-cohort-w1` + one git worktree + one owner.
> Paths are exclusive: no two open tasks write the same path. Contracts (T0) merge before any `[P]` task starts.
> Paths are relative to the implementation repo. Default: this repo's `src/`. If CC finds the live bot in
> another repo, use that one and record it in `docs/STATE.md`.

## Plan
| # | Task | Covers AC | Owner | Depends | Exclusive paths | Gate | Status |
|---|---|---|---|---|---|---|---|
| T0 | Contracts → typed models + fixture validator | AC-1, AC-3, AC-6, AC-7 | Codex | — | `src/domain/contracts/` | fixtures validate against `contracts/*.schema.json` | todo |
| T1 | Intake normalizer + ≤ 2 clarifying questions | AC-1 | Codex | T0 | `src/application/intake/` | test `AC-1`: 10 fixtures (text, audio transcript, photo caption) | todo |
| T2 | Single poller + idempotent replies | AC-2 | CC | — | `src/interfaces/telegram/` | test `AC-2`: 20-message replay → 20 replies, 0 dupes | todo |
| T3 | Sourcing adapters (≥ 3 sources) + landed cost `[P]` | AC-3 | Codex | T0, H8 | `src/infrastructure/sources/` | test `AC-3` on recorded fixtures (no live calls in CI) | todo |
| T4 | Assurance checks + scorer + weight profiles `[P]` | AC-3 | Codex | T0 | `src/domain/scoring/` | golden test `AC-3`: design §4 table (A 8.4, B 7.9, D 7.6, C 7.0, X excluded) | todo |
| T5 | Renderers: L1 PNG 1080×1920, L2 text, L3 PDF/web `[P]` | AC-4, AC-5 | Codex | T0 | `src/interfaces/render/` | tests `AC-4`, `AC-5`: snapshot + PDF opens + PNG size | todo |
| T6 | Flow wiring: steps, buttons, timers | AC-4, AC-6 | CC | T1, T2, T5 | `src/application/flow/` | dry run on recorded offers: request → L2 ≤ 10 min | todo |
| T7 | A1 checkout runner, 1 marketplace (pick from H8) | AC-6, AC-8 | CC | T6, H8 | `src/infrastructure/checkout/` | dry run to payment step on a ≤ R$ 50 item; asserts no submit | todo |
| T8 | Ledger + rating prompt | AC-7 | Codex | T0 | `src/application/ledger/` | test `AC-7` fixtures | todo |
| T9 | Money guard: A2 disabled, ceiling, logging | AC-8 | CC | T7 | `src/domain/policy/` | test `AC-8`: the 5 decision-matrix rows | todo |
| T10 | WEEK1 metrics script | AC-9 | Codex | T8 | `scripts/cohort-week-metrics/` | runs on `~/isaura-data/cohort/`, writes `WEEK1.md` | todo |

H8 = research card in `goals/2026-10-21_nightly_goal.md` (marketplace integration paths).

## Pairing protocol (CC + Codex gpt-6.1-sol)
1. CC writes the card for each Codex task: task row above + links to spec, design §, contract files. Nothing else.
2. Codex runs headless in its worktree with stdin closed (`< /dev/null`; a run with stdin open hung for 69 min before).
   Model `gpt-6.1-sol`, effort `low` for every card. `medium` only after the task's gate fails twice, via `escalate:` in the card.
   CC checks exact flags with `codex exec --help` first. Time estimates and calendar blocks: `../0004-focus-guardrails/week-2026-10-21.blocks.yaml`.
3. Codex commits on its task branch only. It never merges and never edits paths outside its row.
4. CC runs the gate, reviews the diff, merges into `feat/0002-family-cohort-w1`, updates Status.
5. CC-owned tasks get a read-only review from Codex (`REVIEW.md` in the worktree, not committed).
6. No output for 30 min → CC kills the run, logs it in `~/isaura-data/ops/dispatch.md`, re-dispatches once with a smaller scope.
7. Contract change needed mid-week → stop the affected tasks, change the schema in its own commit, then resume. Never fork a schema inside a task.

## Test plan
- Unit: scorer math (golden table), assurance thresholds, ladder policy.
- Integration: sourcing adapters on recorded fixtures; renderer outputs.
- Acceptance: one test per AC (AC-1 to AC-9), named with the AC id.

## Deviations (SPEC_DEVIATION)
- [ ] none yet

## Definition of Done checklist
- [ ] AC-1 to AC-9 green by gate, not inspection
- [ ] ADR-0002 (autonomy ladder) recorded
- [ ] Glossary updated (done in this PR)
- [ ] `docs/STATE.md` updated at end of each session
