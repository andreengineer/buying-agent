#!/usr/bin/env python3
"""
sanitize_context.py — Copy cloud-safe files to staging_sanitized/
Applies redaction rules. Generates SKIP_REPORT.txt.
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path("/home/a/Desktop/isaura-hermes-context")
STAGING = REPO_ROOT / "staging_sanitized"
STAGING.mkdir(exist_ok=True)

SOURCE_DIRS = [
    Path("/home/a/Desktop/isaura-goal-metaprompt"),
    Path("/home/a/Desktop/workspace"),
]

ALLOWED_EXTENSIONS = {".md", ".json", ".txt", ".yaml", ".yml"}

FORBIDDEN_FILENAME_PATTERNS = [
    r"\.env$", r"\.env\.", r"secret", r"password", r"token",
    r"credential", r"cookie", r"oauth", r"\.pem$", r"\.key$",
    r"\.p12$", r"\.pfx$", r"auth\.json", r"id_rsa", r"id_ed25519",
]

FORBIDDEN_CONTENT_PATTERNS = [
    r"(?i)(api_key|api\.key)\s*[:=]\s*\S+",
    r"(?i)token\s*[:=]\s*['\"]?\w{20,}",
    r"(?i)password\s*[:=]\s*['\"]?\S+",
    r"(?i)secret\s*[:=]\s*['\"]?\S+",
    r"(?i)bearer\s+[a-zA-Z0-9\-_\.]{20,}",
    r"(?i)basic\s+[a-zA-Z0-9+/=]{20,}",
    r"sk-[a-zA-Z0-9]{32,}",
    r"ghp_[a-zA-Z0-9]{36,}",
    r"ANTHROPIC_API_KEY",
    r"OPENAI_API_KEY",
    r"EVOLUTION.*KEY",
]

SKIP_DIRS = {
    "node_modules", ".git", ".npm", "__pycache__", "staging_sanitized",
    "isaura-hermes-context", ".venv", "venv", "isaura/.env",
}

skipped = []
copied = []

def is_forbidden_filename(name: str) -> bool:
    name_lower = name.lower()
    return any(re.search(p, name_lower) for p in FORBIDDEN_FILENAME_PATTERNS)

def has_sensitive_content(path: Path) -> tuple[bool, str]:
    try:
        text = path.read_text(errors="replace")
        for pattern in FORBIDDEN_CONTENT_PATTERNS:
            m = re.search(pattern, text)
            if m:
                return True, f"pattern match: {pattern[:40]!r} near char {m.start()}"
    except Exception as e:
        return True, f"unreadable: {e}"
    return False, ""

def safe_dest(src: Path) -> Path:
    # Flatten to staging_sanitized/<source_dir_name>/<relative_path>
    for base in SOURCE_DIRS:
        try:
            rel = src.relative_to(base)
            return STAGING / base.name / rel
        except ValueError:
            continue
    return STAGING / src.name

def process_file(src: Path):
    if src.suffix not in ALLOWED_EXTENSIONS:
        skipped.append((str(src), "extension not allowed"))
        return

    if is_forbidden_filename(src.name):
        skipped.append((str(src), "forbidden filename pattern"))
        return

    sensitive, reason = has_sensitive_content(src)
    if sensitive:
        skipped.append((str(src), f"sensitive content — {reason}"))
        return

    dest = safe_dest(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    copied.append((str(src), str(dest)))

def should_skip_dir(d: Path) -> bool:
    return d.name in SKIP_DIRS or d.name.startswith(".")

for source_dir in SOURCE_DIRS:
    if not source_dir.exists():
        print(f"WARN: {source_dir} not found, skipping")
        continue
    for root, dirs, files in os.walk(source_dir):
        root_path = Path(root)
        dirs[:] = [d for d in dirs if not should_skip_dir(root_path / d)]
        for fname in files:
            process_file(root_path / fname)

# Write skip report
skip_report = STAGING / "SKIP_REPORT.txt"
with skip_report.open("w") as f:
    f.write(f"# SANITIZER SKIP REPORT\n")
    f.write(f"# Generated: {datetime.now(timezone.utc).isoformat()}\n\n")
    f.write(f"Copied:  {len(copied)}\n")
    f.write(f"Skipped: {len(skipped)}\n\n")
    f.write("## COPIED\n")
    for src, dst in copied:
        f.write(f"  COPIED  {src}\n         -> {dst}\n")
    f.write("\n## SKIPPED\n")
    for src, reason in skipped:
        f.write(f"  SKIP    {src}\n  REASON: {reason}\n")

print(f"Sanitization complete.")
print(f"  Copied:  {len(copied)}")
print(f"  Skipped: {len(skipped)}")
print(f"  Report:  {skip_report}")
