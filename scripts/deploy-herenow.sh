#!/usr/bin/env bash
# Deploy the static site to here.now (in-place update of an existing slug).
#
#   HERENOW_TOKEN   required  API bearer token
#   HERENOW_SLUG    optional  target slug (default: sturdy-acorn-j7ch)
#
# Deploys every file listed in FILES (paths relative to repo root).
set -euo pipefail

: "${HERENOW_TOKEN:?Set HERENOW_TOKEN}"
SLUG="${HERENOW_SLUG:-sturdy-acorn-j7ch}"
API="https://here.now/api/v1/publish/${SLUG}"
FILES=("index.html")

cd "$(dirname "$0")/.."

# 1. Build the file manifest.
manifest=$(for f in "${FILES[@]}"; do
  jq -n --arg p "$f" \
        --argjson s "$(wc -c < "$f")" \
        --arg c "text/html; charset=utf-8" \
        '{path:$p, size:$s, contentType:$c}'
done | jq -s '{files: .}')

# 2. Create a new version (PUT = update existing slug in place).
resp=$(curl -fsS -X PUT "$API" \
  -H "Authorization: Bearer ${HERENOW_TOKEN}" \
  -H "content-type: application/json" \
  -d "$manifest")

version_id=$(jq -r '.upload.versionId' <<<"$resp")
finalize_url=$(jq -r '.upload.finalizeUrl' <<<"$resp")
site_url=$(jq -r '.siteUrl' <<<"$resp")

# 3. Upload each file to its presigned URL.
while IFS=$'\t' read -r path url ctype; do
  curl -fsS -X PUT "$url" -H "Content-Type: ${ctype}" --upload-file "$path" >/dev/null
  echo "uploaded ${path}"
done < <(jq -r '.upload.uploads[] | [.path, .url, .headers["Content-Type"]] | @tsv' <<<"$resp")

# 4. Finalize.
curl -fsS -X POST "$finalize_url" \
  -H "Authorization: Bearer ${HERENOW_TOKEN}" \
  -H "content-type: application/json" \
  -d "$(jq -n --arg v "$version_id" '{versionId:$v}')" >/dev/null

echo "deployed: ${site_url}"
