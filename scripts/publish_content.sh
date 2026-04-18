#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo "[1/5] Validating JSON"
python3 scripts/validate_pillar_json.py

echo "[2/5] Generating JSON version report"
python3 scripts/json_version_report.py

echo "[3/5] Generating programmatic SEO pages"
python3 scripts/generate_programmatic_pages.py

echo "[4/5] Generating sitemap/robots/llm crawl files"
python3 scripts/generate_seo_assets.py

echo "[5/5] Done"
echo "Next: git add . && git commit -m 'content update' && deploy to Cloudflare Pages"
