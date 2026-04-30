import json, os, re

ERRORS = []
WARNINGS = []

def check(condition, msg, category="ERROR"):
    if not condition:
        if category == "ERROR":
            ERRORS.append(msg)
        else:
            WARNINGS.append(msg)

# ─────────────────────────────────────────────────────────────
# 1. BHAJANS
# ─────────────────────────────────────────────────────────────
with open('data/bhajans.json','r') as f:
    bhajans = json.load(f)

print(f"\n{'='*60}")
print(f"BHAJANS — {len(bhajans)} entries")
print('='*60)
PLACEHOLDER_WORDS = ['lorem','ipsum','placeholder','todo','tbd','coming soon','sample text','example']

for b in bhajans:
    slug = b.get('slug','?')
    verses = b.get('verses',[])
    check(len(verses) >= 3, f"  [BHAJAN] '{slug}' has only {len(verses)} verses (need ≥3)")
    for i, v in enumerate(verses):
        for line in v.get('lines',[]):
            for field in ['hindi','roman','english']:
                val = line.get(field,'')
                check(bool(val), f"  [BHAJAN] '{slug}' verse {i+1} — '{field}' is EMPTY")
                for pw in PLACEHOLDER_WORDS:
                    check(pw not in val.lower(), f"  [BHAJAN] '{slug}' verse {i+1} — '{field}' has placeholder: '{pw}'")
    print(f"  ✅ {slug}: {len(verses)} verses")

# ─────────────────────────────────────────────────────────────
# 2. SHLOKAS
# ─────────────────────────────────────────────────────────────
with open('data/shlokas.json','r') as f:
    raw = json.load(f)
    shlokas = raw.get('shlokas', raw) if isinstance(raw, dict) else raw

print(f"\n{'='*60}")
print(f"SHLOKAS — {len(shlokas)} entries")
print('='*60)
for s in shlokas:
    slug = s.get('slug','?')
    check(bool(s.get('sanskrit')), f"  [SHLOKA] '{slug}' — 'sanskrit' is EMPTY")
    check(bool(s.get('meaning_english')), f"  [SHLOKA] '{slug}' — 'meaning_english' is EMPTY")
    check(bool(s.get('word_by_word')), f"  [SHLOKA] '{slug}' — 'word_by_word' is EMPTY")
    print(f"  ✅ {slug}: OK")

# ─────────────────────────────────────────────────────────────
# 3. PRAYERS
# ─────────────────────────────────────────────────────────────
with open('data/prayers.json','r') as f:
    prayers_data = json.load(f)
    prayers = prayers_data.get('prayers', prayers_data) if isinstance(prayers_data, dict) else prayers_data

print(f"\n{'='*60}")
print(f"PRAYERS — {len(prayers)} entries")
print('='*60)
for p in prayers:
    slug = p.get('slug','?')
    steps = p.get('steps',[])
    check(len(steps) >= 3, f"  [PRAYER] '{slug}' has only {len(steps)} steps (need ≥3)")
    print(f"  ✅ {slug}: {len(steps)} steps")

# ─────────────────────────────────────────────────────────────
# 4. WISDOM
# ─────────────────────────────────────────────────────────────
with open('data/wisdom.json','r') as f:
    wisdom_data = json.load(f)
    topics = wisdom_data.get('topics', wisdom_data) if isinstance(wisdom_data, dict) else wisdom_data

print(f"\n{'='*60}")
print(f"WISDOM TOPICS — {len(topics)} entries")
print('='*60)
for t in topics:
    slug = t.get('slug','?')
    quotes = t.get('quotes',[])
    check(len(quotes) >= 3, f"  [WISDOM] '{slug}' has only {len(quotes)} quotes (need ≥3)")
    print(f"  ✅ {slug}: {len(quotes)} quotes")

# ─────────────────────────────────────────────────────────────
# 5. UPANISHADS
# ─────────────────────────────────────────────────────────────
with open('data/upanishads.json','r') as f:
    upanishads = json.load(f)

print(f"\n{'='*60}")
print(f"UPANISHADS — {len(upanishads)} entries")
print('='*60)
for u in upanishads:
    slug = u.get('slug','?')
    verses = u.get('verses',[])
    check(len(verses) >= 3, f"  [UPANISHAD] '{slug}' has only {len(verses)} verses (need ≥3)")
    print(f"  ✅ {slug}: {len(verses)} verses")

# ─────────────────────────────────────────────────────────────
# 6. GITA
# ─────────────────────────────────────────────────────────────
with open('data/gita.json','r') as f:
    gita_data = json.load(f)
    chapters = gita_data.get('chapters', gita_data) if isinstance(gita_data, dict) else gita_data

print(f"\n{'='*60}")
print(f"BHAGAVAD GITA — {len(chapters)} chapters")
print('='*60)
for ch in chapters:
    cnum = ch.get('chapter','?')
    verses = ch.get('verses',[])
    check(len(verses) >= 5, f"  [GITA] Chapter {cnum} has only {len(verses)} verses (need ≥5)")
    print(f"  ✅ Chapter {cnum}: {len(verses)} verses")

# ─────────────────────────────────────────────────────────────
# 7. BACK BUTTON AUDIT — all HTML templates
# ─────────────────────────────────────────────────────────────
TEMPLATES = [
    'index.html','bhajans.html','bhajan.html','bhagavad-gita.html',
    'shlokas.html','prayers.html','upanishads.html','wisdom.html',
    'about.html','contact.html','favorites.html'
]
print(f"\n{'='*60}")
print("BACK BUTTON AUDIT")
print('='*60)
for tmpl in TEMPLATES:
    if not os.path.exists(tmpl):
        WARNINGS.append(f"  [TEMPLATE] '{tmpl}' does not exist")
        continue
    with open(tmpl,'r') as f:
        content = f.read()
    # Bad pattern: old broken relative check
    has_broken = "endsWith('/')" in content or "endsWith('/index.html')" in content
    # Good pattern: strict absolute path check
    has_fixed = ("p === '/' " in content or "p === '/'" in content or 
                 "pathname === '/'" in content or "location.pathname ===" in content)
    if has_broken and not has_fixed:
        check(False, f"  [BACK BTN] '{tmpl}' — still uses BROKEN back button logic")
    else:
        print(f"  ✅ {tmpl}: back button OK")

# ─────────────────────────────────────────────────────────────
# 8. PLACEHOLDER scan in HTML templates
# ─────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("PLACEHOLDER SCAN IN TEMPLATES")
print('='*60)
HTML_PLACEHOLDERS = ['lorem ipsum', 'coming soon', 'TODO', 'FIXME', 'placeholder text', '[content here]', 'sample content']
for tmpl in TEMPLATES:
    if not os.path.exists(tmpl): continue
    with open(tmpl,'r') as f:
        content = f.read()
    found = [p for p in HTML_PLACEHOLDERS if p.lower() in content.lower()]
    if found:
        ERRORS.append(f"  [PLACEHOLDER] '{tmpl}' — found: {found}")
    else:
        print(f"  ✅ {tmpl}: no placeholders")

# ─────────────────────────────────────────────────────────────
# 9. SEO PAGES — check generated folders exist and have content
# ─────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("SEO PAGES FOLDER AUDIT")
print('='*60)
SEO_FOLDERS = ['bhajan','shloka','prayer','upanishad','wisdom','gita']
for folder in SEO_FOLDERS:
    if os.path.isdir(folder):
        count = sum(1 for _, dirs, files in os.walk(folder) for f in files if f.endswith('.html'))
        check(count > 0, f"  [SEO] '{folder}/' exists but has no HTML files!")
        print(f"  ✅ {folder}/  — {count} pages")
    else:
        check(False, f"  [SEO] Folder '{folder}/' does NOT exist!")

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("AUDIT SUMMARY")
print('='*60)
if ERRORS:
    print(f"\n❌ {len(ERRORS)} ERROR(S) FOUND:")
    for e in ERRORS:
        print(e)
else:
    print("\n✅ ZERO ERRORS — site is 100% clean!")

if WARNINGS:
    print(f"\n⚠️  {len(WARNINGS)} WARNING(S):")
    for w in WARNINGS:
        print(w)
else:
    print("✅ ZERO WARNINGS")

print()
