#!/usr/bin/env python3
import copy
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
from urllib.request import Request, urlopen

from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

app = FastAPI(title="Bhajan Content Backend", version="1.0.0")

PILLARS = {
    "bhajans": {"path": DATA / "bhajans.json", "shape": "list"},
    "shlokas": {"path": DATA / "shlokas.json", "shape": "list"},
    "prayers": {"path": DATA / "prayers.json", "shape": "dict_list", "key": "prayers"},
    "gita": {"path": DATA / "gita.json", "shape": "dict_nested", "key": "chapters"},
    "upanishads": {"path": DATA / "upanishads.json", "shape": "list"},
    "wisdom": {"path": DATA / "wisdom.json", "shape": "dict_list", "key": "topics"},
}


class IngestRequest(BaseModel):
    pillar: str = Field(..., description="One of: bhajans, shlokas, prayers, gita, upanishads, wisdom")
    item: Dict[str, Any]
    replace_by_slug: bool = True



def read_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def get_slug(item: Dict[str, Any]) -> str:
    return str(item.get("slug", "")).strip()


def get_title(item: Dict[str, Any]) -> str:
    for k in ("title_hindi", "title_english", "name_hindi", "name_english", "slug"):
        if item.get(k):
            return str(item[k])
    return ""


def get_target_list(pillar: str, data: Any) -> List[Dict[str, Any]]:
    cfg = PILLARS[pillar]
    shape = cfg["shape"]
    if shape == "list":
        if not isinstance(data, list):
            raise HTTPException(status_code=500, detail=f"Invalid JSON shape for {pillar}")
        return data
    if shape == "dict_list":
        key = cfg["key"]
        arr = data.get(key, [])
        if not isinstance(arr, list):
            raise HTTPException(status_code=500, detail=f"Invalid JSON shape for {pillar}")
        return arr
    if shape == "dict_nested":
        # Gita structure is chapter-based; item should be a chapter object.
        key = cfg["key"]
        arr = data.get(key, [])
        if not isinstance(arr, list):
            raise HTTPException(status_code=500, detail=f"Invalid JSON shape for {pillar}")
        return arr
    raise HTTPException(status_code=500, detail=f"Unsupported shape for {pillar}")


def upsert_by_slug(items: List[Dict[str, Any]], item: Dict[str, Any], replace_by_slug: bool) -> str:
    slug = get_slug(item)
    if replace_by_slug and slug:
        for i, row in enumerate(items):
            if str(row.get("slug", "")).strip() == slug:
                items[i] = item
                return "replace"
    items.append(item)
    return "insert"


def webhook_for_pillar(pillar: str) -> str:
    return os.getenv(f"GSHEET_WEBHOOK_{pillar.upper()}", "").strip()


def sync_google_sheet(pillar: str, action: str, item: Dict[str, Any]) -> None:
    url = webhook_for_pillar(pillar)
    if not url:
        return
    payload = {
        "pillar": pillar,
        "action": action,
        "slug": get_slug(item),
        "title": get_title(item),
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "raw_item": item,
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(req, timeout=20) as resp:
        _ = resp.read()


def run_publish_pipeline() -> None:
    subprocess.run(["bash", str(ROOT / "scripts" / "publish_content.sh")], cwd=str(ROOT), check=True)


@app.get("/api/health")
def health() -> Dict[str, Any]:
    return {"status": "ok", "service": "bhajan-content-backend"}


@app.get("/api/content/counts")
def counts() -> Dict[str, Any]:
    out = {}
    for pillar, cfg in PILLARS.items():
        data = read_json(cfg["path"])
        arr = get_target_list(pillar, data)
        out[pillar] = len(arr)
    return {"status": "ok", "counts": out}


@app.post("/api/content/ingest")
def ingest(req: IngestRequest, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    pillar = req.pillar.strip().lower()
    if pillar not in PILLARS:
        raise HTTPException(status_code=400, detail="Invalid pillar")

    item = copy.deepcopy(req.item)
    cfg = PILLARS[pillar]
    data = read_json(cfg["path"])
    items = get_target_list(pillar, data)

    action = upsert_by_slug(items, item, req.replace_by_slug)
    write_json(cfg["path"], data)

    background_tasks.add_task(run_publish_pipeline)
    background_tasks.add_task(sync_google_sheet, pillar, action, item)

    return {
        "status": "ok",
        "pillar": pillar,
        "action": action,
        "slug": get_slug(item),
        "message": "JSON updated; publish + sheet sync queued in background",
    }
