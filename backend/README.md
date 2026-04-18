# Bhajan Content Backend

This backend gives you one API to insert content into any pillar. When content is inserted:
1. JSON is updated in `/data`
2. Publish pipeline runs (`scripts/publish_content.sh`)
3. Google Sheets webhook is called automatically (if configured)

## Run

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 127.0.0.1 --port 8090 --reload
```

## API

### `POST /api/content/ingest`

Request body:
```json
{
  "pillar": "bhajans",
  "item": {"slug": "example-slug", "title_hindi": "..."},
  "replace_by_slug": true
}
```

### `GET /api/content/counts`
Returns counts from all six pillars.

## Google Sheets Auto Sync (6 Sheets)
Set these env vars before running backend:

- `GSHEET_WEBHOOK_BHAJANS`
- `GSHEET_WEBHOOK_SHLOKAS`
- `GSHEET_WEBHOOK_PRAYERS`
- `GSHEET_WEBHOOK_GITA`
- `GSHEET_WEBHOOK_UPANISHADS`
- `GSHEET_WEBHOOK_WISDOM`

Each webhook should accept JSON POST.

Payload sent:
- `pillar`
- `action` (`insert` or `replace`)
- `slug`
- `title`
- `updated_at`
- `raw_item`
