#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

ROMAN_BEEJ_RE = re.compile(
    r"\b(hreem|shreem|kleem|phat|hroum|kshroum|ayeim)\b",
    flags=re.IGNORECASE,
)
DEVANAGARI_BEEJ_RE = re.compile(r"(ह्रीं|श्रीं|क्लीं|ऐं|फट्|फट)")


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def flat_text(node):
    if isinstance(node, dict):
        for v in node.values():
            yield from flat_text(v)
    elif isinstance(node, list):
        for v in node:
            yield from flat_text(v)
    elif isinstance(node, str):
        yield node


def check_beej(data, file_name):
    findings = []
    for txt in flat_text(data):
        m1 = ROMAN_BEEJ_RE.search(txt)
        if m1:
            findings.append(f"{file_name}: contains restricted token '{m1.group(1)}'")
            continue
        m2 = DEVANAGARI_BEEJ_RE.search(txt)
        if m2:
            findings.append(f"{file_name}: contains restricted token '{m2.group(1)}'")
    return findings


def required_checks():
    checks = []

    bhajans = load(DATA / "bhajans.json")
    checks.append(("bhajans.json list", isinstance(bhajans, list)))
    checks.append(("bhajans has items", len(bhajans) > 0))

    shlokas = load(DATA / "shlokas.json")
    checks.append(("shlokas.json list", isinstance(shlokas, list)))

    prayers = load(DATA / "prayers.json")
    checks.append(("prayers.json has prayers[]", isinstance(prayers, dict) and isinstance(prayers.get("prayers"), list)))

    gita = load(DATA / "gita.json")
    checks.append(("gita.json has chapters[]", isinstance(gita, dict) and isinstance(gita.get("chapters"), list)))

    upanishads = load(DATA / "upanishads.json")
    checks.append(("upanishads.json list", isinstance(upanishads, list)))

    wisdom = load(DATA / "wisdom.json")
    checks.append(("wisdom.json has topics[]", isinstance(wisdom, dict) and isinstance(wisdom.get("topics"), list)))

    return checks, [
        *check_beej(bhajans, "bhajans.json"),
        *check_beej(shlokas, "shlokas.json"),
        *check_beej(prayers, "prayers.json"),
        *check_beej(gita, "gita.json"),
        *check_beej(upanishads, "upanishads.json"),
        *check_beej(wisdom, "wisdom.json"),
    ]


def main():
    checks, beej_issues = required_checks()
    failed = [name for name, ok in checks if not ok]

    print("JSON structure checks:")
    for name, ok in checks:
        print(f"- {'PASS' if ok else 'FAIL'}: {name}")

    if beej_issues:
        print("\nRestricted mantra findings:")
        for line in beej_issues[:100]:
            print("-", line)

    if failed or beej_issues:
        raise SystemExit(1)

    print("\nAll validations passed.")


if __name__ == "__main__":
    main()
