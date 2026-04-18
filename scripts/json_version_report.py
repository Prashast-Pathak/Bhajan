#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "docs" / "JSON_VERSION_REPORT.md"


def read_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def count_items():
    bhajans = read_json(DATA / "bhajans.json")
    shlokas = read_json(DATA / "shlokas.json")
    prayers = read_json(DATA / "prayers.json").get("prayers", [])
    upanishads = read_json(DATA / "upanishads.json")
    wisdom_topics = read_json(DATA / "wisdom.json").get("topics", [])
    gita = read_json(DATA / "gita.json").get("chapters", [])

    gita_verses = 0
    for chapter in gita:
        gita_verses += len(chapter.get("verses", []))

    return {
        "bhajans": len(bhajans) if isinstance(bhajans, list) else 0,
        "shlokas": len(shlokas) if isinstance(shlokas, list) else 0,
        "prayers": len(prayers) if isinstance(prayers, list) else 0,
        "upanishads": len(upanishads) if isinstance(upanishads, list) else 0,
        "wisdom_topics": len(wisdom_topics) if isinstance(wisdom_topics, list) else 0,
        "gita_chapters": len(gita) if isinstance(gita, list) else 0,
        "gita_verses": gita_verses,
    }


def write_report(stats):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# JSON Version Report",
        "",
        f"Generated: {now}",
        "",
        "## Content Counts",
        "",
        f"- Bhajans: **{stats['bhajans']}**",
        f"- Shlokas: **{stats['shlokas']}**",
        f"- Prayers: **{stats['prayers']}**",
        f"- Upanishads: **{stats['upanishads']}**",
        f"- Wisdom Topics: **{stats['wisdom_topics']}**",
        f"- Gita Chapters: **{stats['gita_chapters']}**",
        f"- Gita Verses: **{stats['gita_verses']}**",
        "",
        "## Files Tracked",
        "",
        "- `/data/bhajans.json`",
        "- `/data/shlokas.json`",
        "- `/data/prayers.json`",
        "- `/data/gita.json`",
        "- `/data/upanishads.json`",
        "- `/data/wisdom.json`",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")


def main():
    stats = count_items()
    write_report(stats)
    print("JSON report written to docs/JSON_VERSION_REPORT.md")


if __name__ == "__main__":
    main()
