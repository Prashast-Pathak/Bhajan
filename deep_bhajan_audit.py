import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

ERRORS = []
WARNINGS = []

# Expected minimum standards for each bhajan
REQUIRED_FIELDS = ['slug', 'title_hindi', 'title_roman', 'title_english', 'deity',
                   'composer', 'language', 'timing', 'occasion', 'story',
                   'story_hindi', 'significance', 'significance_hindi', 'benefits',
                   'raga', 'when_to_sing', 'tags', 'verses']

TRADITIONAL_VERSE_COUNT = {
    'hanuman-chalisa': 42,
    'jai-ganesh-deva': 5,
    'om-jai-jagdish-hare': 9,
    'shiv-tandav-stotram': 15,
    'achyutam-keshavam': 5,
    'ram-siya-ram': 10,
    'deva-shree-ganesha': 5,
    'jai-ambe-gauri': 10,
    'aarti-kunj-bihari-ki': 8,
    'om-jai-lakshmi-mata': 8,
    'raghupati-raghav-raja-ram': 5,
    'mere-ghar-ram-aayo': 3,
    'vaishnav-jan': 5,
    'shri-ramachandra-kripalu': 5,
    'madhurashtakam': 8,
}

print("=" * 70)
print("DEEP BHAJAN AUDIT — Every Field, Every Verse, Every Line")
print("=" * 70)

for b in data:
    slug = b.get('slug', '?')
    has_error = False
    verse_errors = []
    field_errors = []
    
    print(f"\n{'─'*60}")
    print(f"📿 {slug}")
    print(f"   Title: {b.get('title_hindi','')} | {b.get('title_roman','')}")
    print(f"   Deity: {b.get('deity','')} | Composer: {b.get('composer','')}")
    
    # 1. Check required fields
    for field in REQUIRED_FIELDS:
        val = b.get(field)
        if not val:
            field_errors.append(f"MISSING field: '{field}'")
            has_error = True
        elif isinstance(val, str) and len(val.strip()) < 5:
            field_errors.append(f"TOO SHORT field: '{field}' = '{val}'")
            has_error = True
    
    # 2. Check story length (should be substantial)
    story = b.get('story', '')
    if story and len(story) < 100:
        field_errors.append(f"Story too short: {len(story)} chars (need 100+)")
        has_error = True
        
    story_hindi = b.get('story_hindi', '')
    if story_hindi and len(story_hindi) < 50:
        field_errors.append(f"story_hindi too short: {len(story_hindi)} chars")
        has_error = True
    
    # 3. Check significance
    sig = b.get('significance', '')
    if sig and len(sig) < 80:
        field_errors.append(f"significance too short: {len(sig)} chars")
        has_error = True
        
    # 4. Check benefits
    benefits = b.get('benefits', [])
    if not benefits or len(benefits) < 3:
        field_errors.append(f"benefits: only {len(benefits)} (need 3+)")
        has_error = True
    
    # 5. Check SEO fields
    seo = b.get('seo', {})
    if not seo:
        field_errors.append("MISSING: 'seo' block")
        has_error = True
    else:
        for seo_field in ['meta_title', 'meta_description', 'keywords']:
            if not seo.get(seo_field):
                field_errors.append(f"MISSING seo.{seo_field}")
                has_error = True
    
    # 6. Check verses
    verses = b.get('verses', [])
    expected = TRADITIONAL_VERSE_COUNT.get(slug, 3)
    if len(verses) < expected:
        verse_errors.append(f"Only {len(verses)} verses (expected {expected})")
        has_error = True
    
    for vi, v in enumerate(verses):
        lines = v.get('lines', [])
        if not lines:
            verse_errors.append(f"Verse {vi+1}: NO LINES at all!")
            has_error = True
            continue
        for li, line in enumerate(lines):
            for field in ['hindi', 'roman', 'english']:
                val = line.get(field, '')
                if not val or len(val.strip()) < 3:
                    verse_errors.append(f"Verse {vi+1} Line {li+1}: '{field}' is EMPTY")
                    has_error = True
            # Check hindi_meaning exists
            if not line.get('hindi_meaning'):
                verse_errors.append(f"Verse {vi+1} Line {li+1}: 'hindi_meaning' is EMPTY")
                has_error = True
    
    # Print results
    if field_errors:
        for e in field_errors:
            print(f"   ❌ {e}")
    if verse_errors:
        for e in verse_errors:
            print(f"   ❌ {e}")
    if not has_error:
        print(f"   ✅ ALL {len(verses)} verses & all fields complete")
    
    ERRORS.extend([f"[{slug}] {e}" for e in field_errors + verse_errors])

print(f"\n{'='*70}")
print("AUDIT SUMMARY")
print(f"{'='*70}")
if ERRORS:
    print(f"\n❌ {len(ERRORS)} TOTAL ERRORS FOUND")
    # Group by bhajan
    from collections import defaultdict
    by_bhajan = defaultdict(list)
    for e in ERRORS:
        slug = e.split(']')[0][1:]
        by_bhajan[slug].append(e)
    for slug, errs in by_bhajan.items():
        print(f"\n  {slug}: {len(errs)} errors")
else:
    print("\n✅ ALL BHAJANS ARE COMPLETELY FILLED!")
