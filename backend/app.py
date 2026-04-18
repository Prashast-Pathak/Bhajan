#!/usr/bin/env python3
import copy
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple
from urllib.request import Request, urlopen

from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
AUDIT_LOG = ROOT / "docs" / "INGEST_AUDIT_LOG.ndjson"

app = FastAPI(title="Bhajan Content Backend", version="1.1.0")

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


class BatchIngestRequest(BaseModel):
    pillar: str = Field(..., description="One of: bhajans, shlokas, prayers, gita, upanishads, wisdom")
    items: List[Dict[str, Any]]
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
    for key in ("title_hindi", "title_english", "name_hindi", "name_english", "slug"):
        if item.get(key):
            return str(item[key])
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
        key = cfg["key"]
        arr = data.get(key, [])
        if not isinstance(arr, list):
            raise HTTPException(status_code=500, detail=f"Invalid JSON shape for {pillar}")
        return arr
    raise HTTPException(status_code=500, detail=f"Unsupported shape for {pillar}")


def upsert_by_slug(items: List[Dict[str, Any]], item: Dict[str, Any], replace_by_slug: bool) -> str:
    slug = get_slug(item)
    if replace_by_slug and slug:
        for index, row in enumerate(items):
            if str(row.get("slug", "")).strip() == slug:
                items[index] = item
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


def sync_google_sheet_safe(pillar: str, action: str, item: Dict[str, Any]) -> Tuple[bool, str]:
    try:
        sync_google_sheet(pillar, action, item)
        return True, "ok"
    except Exception as err:  # noqa: BLE001
        return False, str(err)


def run_publish_pipeline() -> None:
    subprocess.run(["bash", str(ROOT / "scripts" / "publish_content.sh")], cwd=str(ROOT), check=True)


def run_publish_pipeline_safe() -> Tuple[bool, str]:
    try:
        run_publish_pipeline()
        return True, "ok"
    except Exception as err:  # noqa: BLE001
        return False, str(err)


def write_audit_log(payload: Dict[str, Any]) -> None:
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def apply_ingest(pillar: str, item: Dict[str, Any], replace_by_slug: bool) -> str:
    cfg = PILLARS[pillar]
    data = read_json(cfg["path"])
    items = get_target_list(pillar, data)
    action = upsert_by_slug(items, item, replace_by_slug)
    write_json(cfg["path"], data)
    return action


def run_full_automation_for_item(pillar: str, action: str, item: Dict[str, Any]) -> Dict[str, Any]:
    publish_ok, publish_msg = run_publish_pipeline_safe()
    sheet_ok, sheet_msg = sync_google_sheet_safe(pillar, action, item)
    audit = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pillar": pillar,
        "action": action,
        "slug": get_slug(item),
        "title": get_title(item),
        "publish_ok": publish_ok,
        "publish_msg": publish_msg,
        "sheet_ok": sheet_ok,
        "sheet_msg": sheet_msg,
    }
    write_audit_log(audit)
    return audit


def run_full_automation_for_batch(pillar: str, changes: List[Dict[str, Any]]) -> Dict[str, Any]:
    publish_ok, publish_msg = run_publish_pipeline_safe()
    sheet_results = []
    for change in changes:
        ok, msg = sync_google_sheet_safe(pillar, change["action"], change["item"])
        rec = {
            "slug": get_slug(change["item"]),
            "title": get_title(change["item"]),
            "action": change["action"],
            "sheet_ok": ok,
            "sheet_msg": msg,
        }
        sheet_results.append(rec)
        write_audit_log(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "pillar": pillar,
                "action": change["action"],
                "slug": rec["slug"],
                "title": rec["title"],
                "publish_ok": publish_ok,
                "publish_msg": publish_msg,
                "sheet_ok": ok,
                "sheet_msg": msg,
            }
        )
    return {
        "publish_ok": publish_ok,
        "publish_msg": publish_msg,
        "sheet_results": sheet_results,
    }


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


@app.get("/api/content/audit-log")
def audit_log(limit: int = 50) -> Dict[str, Any]:
    if not AUDIT_LOG.exists():
        return {"status": "ok", "entries": []}
    limit = max(1, min(500, int(limit)))
    lines = AUDIT_LOG.read_text(encoding="utf-8").splitlines()
    entries = []
    for line in lines[-limit:]:
        try:
            entries.append(json.loads(line))
        except Exception:  # noqa: BLE001
            continue
    return {"status": "ok", "entries": entries}


@app.post("/api/content/ingest")
def ingest(req: IngestRequest, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    pillar = req.pillar.strip().lower()
    if pillar not in PILLARS:
        raise HTTPException(status_code=400, detail="Invalid pillar")

    item = copy.deepcopy(req.item)
    action = apply_ingest(pillar, item, req.replace_by_slug)
    background_tasks.add_task(run_full_automation_for_item, pillar, action, item)
    return {
        "status": "ok",
        "pillar": pillar,
        "action": action,
        "slug": get_slug(item),
        "message": "JSON updated; publish + SEO + sheet sync queued in background",
    }


@app.post("/api/content/batch-ingest")
def batch_ingest(req: BatchIngestRequest) -> Dict[str, Any]:
    pillar = req.pillar.strip().lower()
    if pillar not in PILLARS:
        raise HTTPException(status_code=400, detail="Invalid pillar")
    if not req.items:
        raise HTTPException(status_code=400, detail="Items list is empty")

    changes = []
    for raw in req.items:
        item = copy.deepcopy(raw)
        action = apply_ingest(pillar, item, req.replace_by_slug)
        changes.append({"item": item, "action": action})

    automation = run_full_automation_for_batch(pillar, changes)
    return {
        "status": "ok",
        "pillar": pillar,
        "total_items": len(changes),
        "changes": [
            {"slug": get_slug(ch["item"]), "action": ch["action"], "title": get_title(ch["item"])}
            for ch in changes
        ],
        "publish_ok": automation["publish_ok"],
        "publish_msg": automation["publish_msg"],
        "sheet_results": automation["sheet_results"],
    }
