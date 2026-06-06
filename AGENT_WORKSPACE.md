# AGENT WORKSPACE — LLM-to-LLM Data Layer

**Goal**: Any LLM agent (Claude, ChatGPT, Hermes, DeepSeek, etc.) can read and write structured data in this repo using only standard tools: file operations, JSON parsing, git.

No proprietary APIs, no MCP servers, no gateways. Just files.

---

## Conventions

### Data format
- **Machine ↔ Machine**: JSON (strict schema, typed fields, timestamps)
- **Machine → Human**: Markdown (reports, summaries, runbooks)
- Never mix. A JSON file contains zero prose; a MD file contains zero structured data.

### File structure
```
reviews/              ← structured critiques, audits, assessments
  isaura-pre-alpha-v1.json
  archive/            ← superseded versions
goals/                ← sprint/phase goals (MD for humans, JSON for agents)
manifests/            ← inventory of what exists
architecture/         ← system design docs
runbooks/             ← operational procedures
board_reports/        ← periodic status reports
```

### Naming
- `<entity>-<phase>-v<N>.json` — versioned, never overwrite in place
- Superseded files move to `archive/<entity>-<phase>-v<N>-superseded-<date>.json`
- V bump per sprint, pivot, or significant content change

### Schema requirements (every JSON file MUST have)
```json
{
  "_schema": "<name>-v<major>",
  "_desc": "Plain English purpose — what any LLM should know before reading this file",
  "version": <integer>,
  "created_at": "<ISO8601>",
  "updated_at": "<ISO8601>",
  "_archive": [],
  "_next": "placeholder for next version"
}
```

### Governance
- **Commits are the audit log**. `git log` shows who (which agent/user) wrote what, when.
- **PRs for approval gates**. Sensitive changes (pricing, contracts, prod configs) require human review.
- **No force-push to main**. Branch + PR for structural changes.
- **Any agent can propose edits**. Hermes, Claude, ChatGPT — same rules: commit + push or open a PR.

### Updating from an LLM
1. Read the file (`git pull` → `read_file`)
2. Modify the JSON (add/update items, bump `version`, update `updated_at`)
3. Commit with a message: `<agent-name>: <summary> [v<N+1>]`
4. Push, or open a PR if the change is sensitive

### Reading from an LLM
1. `git pull` to get latest
2. `read_file` the relevant JSON(s)
3. Filter by `version`, `updated_at`, or `created_at` to find the right revision
4. If you need superseded context, check `_archive` or `archive/` directory

---

## Why this works
| Property | Mechanism |
|----------|-----------|
| LLM-readable | Plain JSON, no auth, no API |
| LLM-writable | git + file edit, any CLI agent can do this |
| Redundant | Local + GitHub remote |
| Versioned | git history + semver in filename |
| Governed | git blame, PR review, no force-push |
| Private | GitHub private repo (or self-hosted) |
| Interoperable | No framework lock-in — the format IS the interface |

---

## Future (v2+)
- **Schema registry**: `_schemas/` directory with JSON Schema files for validation
- **Auto-index**: An `INDEX.json` in each directory that any LLM can use to discover files without `ls`
- **Signed commits**: GPG signing so agents can verify integrity
- **Cron-synced**: Hermes cron periodically pulls + reconciles

---

*Last updated: 2026-06-06*
*Maintainer: Cérebro (Claude Opus) — all workspace conventions align with Opus rulings.*
