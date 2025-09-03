#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
ARTIFACTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/artifacts"
mkdir -p "$ARTIFACTS_DIR"

# Package each service which contains an app.py into a zip
for svc in $(ls -1 .. | grep -E '^services$' || true); do
  : # placeholder
done

# Find service directories under services/
for dir in $(find "$ROOT_DIR/services" -maxdepth 2 -type f -name "app.py" -printf "%h\n" 2>/dev/null || true); do
  svc_name=$(basename "$dir")
  artifact="$ARTIFACTS_DIR/${svc_name}.zip"
  echo "Packaging $svc_name -> $artifact"
  (cd "$dir" && zip -r "$artifact" app.py > /dev/null)
done

echo "Artifacts created in $ARTIFACTS_DIR"
