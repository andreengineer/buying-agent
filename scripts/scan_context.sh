#!/bin/bash
# scan_context.sh — Inventory local context files
# Scans isaura-goal-metaprompt/ and workspace/ for relevant files

SCAN_DIRS=(
  "/home/a/Desktop/isaura-goal-metaprompt"
  "/home/a/Desktop/workspace"
)
OUTPUT_FILE="/home/a/Desktop/isaura-hermes-context/staging_sanitized/SCAN_INVENTORY.txt"
EXTENSIONS="md|json|txt|yaml|yml|sh|py"

mkdir -p "$(dirname "$OUTPUT_FILE")"

echo "# CONTEXT SCAN INVENTORY" > "$OUTPUT_FILE"
echo "# Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$OUTPUT_FILE"
echo "# Scanned by: scan_context.sh" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
printf "%-60s %-8s %-10s %-20s %s\n" "PATH" "TYPE" "SIZE" "MODIFIED" "SENSITIVITY_GUESS" >> "$OUTPUT_FILE"
echo "$(printf '%.0s-' {1..120})" >> "$OUTPUT_FILE"

SENSITIVE_PATTERNS="(\.env|api.key|token|password|secret|cookie|oauth|credential|ssh|\.pem|\.key|\.p12|auth\.json|session)"

for dir in "${SCAN_DIRS[@]}"; do
  if [ ! -d "$dir" ]; then
    echo "WARN: $dir not found" >> "$OUTPUT_FILE"
    continue
  fi

  python3 -c "
import os, sys
base = sys.argv[1]
exts = {'.md','.json','.txt','.yaml','.yml','.sh','.py'}
skip_dirs = {'node_modules','.git','staging_sanitized','isaura-hermes-context','.npm','__pycache__','.venv','venv'}
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in skip_dirs and not d.startswith('.')]
    for f in sorted(files):
        p = os.path.join(root, f)
        ext = os.path.splitext(f)[1].lower()
        if ext in exts:
            print(p)
" "$dir" | while read -r fpath; do

    fname=$(basename "$fpath")
    ext="${fname##*.}"
    size=$(du -sh "$fpath" 2>/dev/null | cut -f1)
    mtime=$(stat -c "%Y" "$fpath" 2>/dev/null | xargs -I{} date -d @{} "+%Y-%m-%d %H:%M" 2>/dev/null)

    # Sensitivity heuristic
    sensitivity="CLOUD-SAFE"
    if echo "$fpath" | grep -iqE "$SENSITIVE_PATTERNS"; then
      sensitivity="LOCAL-ONLY"
    elif grep -lqiE "(api_key|api.key|token|password|secret|oauth|credential)" "$fpath" 2>/dev/null; then
      sensitivity="LOCAL-ONLY"
    elif echo "$fname" | grep -iqE "\.env$|secret|password|token|key"; then
      sensitivity="FORBIDDEN"
    fi

    printf "%-60s %-8s %-10s %-20s %s\n" \
      "${fpath:0:59}" "$ext" "$size" "$mtime" "$sensitivity" >> "$OUTPUT_FILE"
  done
done

echo "" >> "$OUTPUT_FILE"
echo "# SUMMARY" >> "$OUTPUT_FILE"
TOTAL=$(grep -v "^#\|^PATH\|^---" "$OUTPUT_FILE" | grep -c "." || true)
SAFE=$(grep -c "CLOUD-SAFE" "$OUTPUT_FILE" || true)
LOCAL=$(grep -c "LOCAL-ONLY" "$OUTPUT_FILE" || true)
FORBIDDEN=$(grep -c "FORBIDDEN" "$OUTPUT_FILE" || true)
echo "Total files: $TOTAL" >> "$OUTPUT_FILE"
echo "Cloud-safe:  $SAFE" >> "$OUTPUT_FILE"
echo "Local-only:  $LOCAL" >> "$OUTPUT_FILE"
echo "Forbidden:   $FORBIDDEN" >> "$OUTPUT_FILE"

echo "Scan complete. Results: $OUTPUT_FILE"
cat "$OUTPUT_FILE"
