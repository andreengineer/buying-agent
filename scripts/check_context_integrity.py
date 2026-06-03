#!/usr/bin/env python3
"""
check_context_integrity.py — Generate manifests/context_manifest.json
sha256, mtime, sensitivity label, upload status for each file in staging_sanitized/
"""

import json
import hashlib
import os
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path("/home/a/Desktop/isaura-hermes-context")
STAGING = REPO_ROOT / "staging_sanitized"
MANIFEST_PATH = REPO_ROOT / "manifests" / "context_manifest.json"
MANIFEST_PATH.parent.mkdir(exist_ok=True)

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def sensitivity_label(path: Path) -> str:
    name = path.name.lower()
    sensitive_patterns = [".env", "secret", "password", "token", "key", "oauth", "cookie"]
    if any(p in name for p in sensitive_patterns):
        return "FORBIDDEN"
    # Check if it's in a sensitive-looking path
    path_str = str(path).lower()
    if "isaura/" in path_str or ".env" in path_str:
        return "LOCAL-ONLY"
    return "CLOUD-SAFE"

entries = []

if STAGING.exists():
    for root, dirs, files in os.walk(STAGING):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in sorted(files):
            if fname in ("SKIP_REPORT.txt", "SCAN_INVENTORY.txt", ".gitkeep"):
                continue
            fpath = Path(root) / fname
            try:
                stat = fpath.stat()
                sha = sha256_file(fpath)
                label = sensitivity_label(fpath)
                # Determine cloud path (relative to staging)
                rel = fpath.relative_to(STAGING)
                entries.append({
                    "source_path": str(fpath),
                    "sanitized_path": str(rel),
                    "sha256": sha,
                    "modified_time": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                    "size_bytes": stat.st_size,
                    "sensitivity_label": label,
                    "upload_status": "pending" if label == "CLOUD-SAFE" else "blocked",
                })
            except Exception as e:
                entries.append({
                    "source_path": str(fpath),
                    "error": str(e),
                    "sensitivity_label": "UNKNOWN",
                    "upload_status": "error",
                })

manifest = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "generated_by": "check_context_integrity.py",
    "repo_root": str(REPO_ROOT),
    "total_files": len(entries),
    "cloud_safe": sum(1 for e in entries if e.get("sensitivity_label") == "CLOUD-SAFE"),
    "blocked": sum(1 for e in entries if e.get("upload_status") == "blocked"),
    "files": entries,
}

with MANIFEST_PATH.open("w") as f:
    json.dump(manifest, f, indent=2)

print(f"Manifest written: {MANIFEST_PATH}")
print(f"  Total:       {manifest['total_files']}")
print(f"  Cloud-safe:  {manifest['cloud_safe']}")
print(f"  Blocked:     {manifest['blocked']}")
