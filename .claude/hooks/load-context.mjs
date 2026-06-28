#!/usr/bin/env node
// Hook SessionStart — injeta o contexto base SDD (docs alwaysApply: true) no início da sessão.
// O stdout deste script é adicionado ao contexto do Claude Code.
// Roda a partir da raiz do projeto; lê só o que existe (no scaffold cru, só o STATE).

import { readFileSync, existsSync } from "node:fs";

// Docs "alwaysApply: true" — o contexto base de toda sessão.
const BASE = [
  "docs/STATE.md",
  "docs/product/vision.md",
  "docs/product/roadmap.md",
];

let out = "# Contexto base SDD (carregado no SessionStart)\n";
out += "> Estes são os docs `alwaysApply: true`. Os demais são sob demanda — puxe pelo `description`.\n";

let any = false;
for (const f of BASE) {
  if (existsSync(f)) {
    out += `\n===== ${f} =====\n${readFileSync(f, "utf8").trim()}\n`;
    any = true;
  }
}

// Dica sobre a spec ativa (o STATE aponta qual é; o agente a lê sob demanda).
out += "\n> Spec da feature ativa: veja \"Em andamento\" no STATE e leia `specs/NNNN-*/spec.md`.\n";

if (any) process.stdout.write(out);
