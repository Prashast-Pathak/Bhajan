# Extreme Step-by-Step Guide: Add Content, Auto-Sync Sheets, Auto-SEO Pages

This is your single operating manual.

## 0. What is now automated
When you add content through backend API:
1. Correct JSON file updates automatically.
2. Validation runs automatically.
3. JSON Version Report regenerates automatically.
4. Programmatic SEO pages regenerate automatically.
5. `sitemap.xml`, `robots.txt`, `llms.txt`, `ai.txt` regenerate automatically.
6. Matching Google Sheet webhook receives the content payload automatically.
7. Ingest audit log is appended automatically to `docs/INGEST_AUDIT_LOG.ndjson`.

No manual sitemap editing needed.

## 1. One-time setup (local machine)

### 1.1 Start website preview server
```bash
cd /Users/prashastpathak/Bhajan
python3 -m http.server 8020
```
Open: `http://127.0.0.1:8020/`

### 1.2 Start backend
```bash
cd /Users/prashastpathak/Bhajan/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 127.0.0.1 --port 8090 --reload
```
Health check:
```bash
curl -s http://127.0.0.1:8090/api/health
```
Expected: `{"status":"ok",...}`

## 2. Configure 6 Google Sheets auto-update
Create 6 Google Sheets (one per pillar).
For each sheet, make a Google Apps Script Web App endpoint that appends JSON rows.
Then export env vars before backend start:

```bash
export GSHEET_WEBHOOK_BHAJANS="https://script.google.com/macros/s/.../exec"
export GSHEET_WEBHOOK_SHLOKAS="https://script.google.com/macros/s/.../exec"
export GSHEET_WEBHOOK_PRAYERS="https://script.google.com/macros/s/.../exec"
export GSHEET_WEBHOOK_GITA="https://script.google.com/macros/s/.../exec"
export GSHEET_WEBHOOK_UPANISHADS="https://script.google.com/macros/s/.../exec"
export GSHEET_WEBHOOK_WISDOM="https://script.google.com/macros/s/.../exec"
```

If any env var is missing, that pillar still updates JSON; only sheet sync is skipped.

## 3. Daily content workflow (the exact process)

### Step A: Generate content with Claude
Use:
- `prompts/claude/MASTER_CONTENT_SYSTEM_PROMPT.md`
- plus pillar prompt `prompts/claude/0X_...`
- plus schema file `templates/pillar-json/...`

Ask Claude: `Return only valid JSON`.

### Step B: Insert content via API
Example (Bhajans):
```bash
curl -s -X POST http://127.0.0.1:8090/api/content/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "pillar":"bhajans",
    "replace_by_slug":true,
    "item":{
      "id":999,
      "slug":"sample-bhajan",
      "title_hindi":"सैंपल भजन",
      "title_roman":"Sample Bhajan",
      "title_english":"Sample Bhajan",
      "deity":"Krishna",
      "deity_color":"#4F46E5",
      "language":"Hindi",
      "festival":[],
      "occasion":"Daily",
      "timing":"Morning",
      "raga":"",
      "composer":"Traditional",
      "duration_minutes":5,
      "tags":["sample"],
      "topics":["devotion"],
      "story":"Short story",
      "story_hindi":"छोटी कथा",
      "significance":"Traditional devotional significance",
      "significance_hindi":"पारंपरिक भक्ति महत्व",
      "benefits":["Traditionally recited for peace."],
      "when_to_sing":{"festival":[],"time":["Morning"],"occasion":["Daily"]},
      "featured":false,
      "priority":999,
      "verses":[],
      "related":[],
      "seo":{"meta_title":"Sample","meta_description":"Sample desc","keywords":["sample"]}
    }
  }'
```

Expected response:
- `status: ok`
- `message: JSON updated; publish + SEO + sheet sync queued in background`

### Step B2: Insert content in bulk (recommended for speed)
```bash
curl -s -X POST http://127.0.0.1:8090/api/content/batch-ingest \
  -H "Content-Type: application/json" \
  -d '{
    "pillar":"bhajans",
    "replace_by_slug":true,
    "items":[
      { "slug":"sample-bhajan-1", "title_hindi":"नमूना भजन 1" },
      { "slug":"sample-bhajan-2", "title_hindi":"नमूना भजन 2" }
    ]
  }'
```

### Step C: Verify auto outputs
Run:
```bash
cd /Users/prashastpathak/Bhajan
bash scripts/publish_content.sh
```
Expected logs:
- `[1/5] Validating JSON`
- `[2/5] Generating JSON version report`
- `[3/5] Generating programmatic SEO pages`
- `[4/5] Generating sitemap/robots/llm crawl files`
- `[5/5] Done`

### Step D: Check generated assets
- `docs/JSON_VERSION_REPORT.md`
- `programmatic/` pages
- `sitemap.xml`
- `robots.txt`
- `llms.txt`
- `ai.txt`
- `docs/INGEST_AUDIT_LOG.ndjson`

### Step E: Verify automatic sheet + publish status
```bash
curl -s "http://127.0.0.1:8090/api/content/audit-log?limit=20"
```

## 4. Deploy updates
```bash
cd /Users/prashastpathak/Bhajan
git add .
git commit -m "content update"
git push origin main
```
Cloudflare Pages auto-deploys from GitHub.

## 5. How canonical domain works
Edit one file only:
- `config/site.config.json` -> `base_url`
Then run:
```bash
bash scripts/publish_content.sh
```
This updates all crawl files to the new domain.

## 6. Safety controls built in
- JSON shape validation for all six pillars.
- Restricted mantra scanner.
- No manual sitemap editing.
- Non-destructive upsert-by-slug logic.

## 7. If something fails
- Check backend logs.
- Re-run `bash scripts/publish_content.sh`.
- Validate API health: `curl -s http://127.0.0.1:8090/api/health`.
