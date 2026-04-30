import json

ERRORS = []

def check(file_name, data, required_fields):
    if not isinstance(data, list):
        print(f"Error parsing {file_name}: not a list")
        return
    for item in data:
        slug = item.get('slug', '?')
        for field in required_fields:
            if not item.get(field):
                ERRORS.append(f"[{file_name}] {slug} missing: {field}")
        if 'seo' in required_fields:
            seo = item.get('seo', {})
            if not seo:
                ERRORS.append(f"[{file_name}] {slug} missing: seo block")
            else:
                for sf in ['meta_title', 'meta_description', 'keywords']:
                    if not seo.get(sf):
                        ERRORS.append(f"[{file_name}] {slug} missing: seo.{sf}")

print("Checking SHLOKAS...")
with open('data/shlokas.json') as f:
    raw = json.load(f)
    shlokas = raw.get('shlokas', raw) if isinstance(raw, dict) else raw
    check('shlokas.json', shlokas, ['slug', 'title_english', 'meaning_english', 'sanskrit', 'seo'])

print("Checking PRAYERS...")
with open('data/prayers.json') as f:
    raw = json.load(f)
    prayers = raw.get('prayers', raw) if isinstance(raw, dict) else raw
    check('prayers.json', prayers, ['slug', 'title_english', 'intro_english', 'seo'])

print("Checking WISDOM...")
with open('data/wisdom.json') as f:
    raw = json.load(f)
    wisdom = raw.get('topics', raw) if isinstance(raw, dict) else raw
    check('wisdom.json', wisdom, ['slug', 'title_english', 'intro_english', 'seo'])

print("Checking UPANISHADS...")
with open('data/upanishads.json') as f:
    upanishads = json.load(f)
    check('upanishads.json', upanishads, ['slug', 'name_english', 'theme_english', 'seo'])

print("Checking GITA...")
with open('data/gita.json') as f:
    raw = json.load(f)
    gita = raw.get('chapters', raw) if isinstance(raw, dict) else raw
    check('gita.json', gita, ['chapter', 'title_english', 'summary_english', 'seo'])

if ERRORS:
    print(f"\n❌ FOUND {len(ERRORS)} MISSING FIELDS:")
    for e in ERRORS[:50]:
        print(e)
    if len(ERRORS) > 50:
        print(f"... and {len(ERRORS)-50} more")
else:
    print("\n✅ All 6 pillars have complete SEO and metadata!")

