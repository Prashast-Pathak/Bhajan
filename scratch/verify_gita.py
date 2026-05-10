import json

with open('/Users/prashastpathak/Bhajan/data/gita.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chapters = {c['chapter']: c for c in data.get('chapters', [])}

for ch in [3, 4, 5, 6, 7]:
    if ch not in chapters:
        print(f"❌ Chapter {ch}: MISSING")
        continue
    
    c = chapters[ch]
    verses = c.get('verses', [])
    verse_nums = sorted([v['verse'] for v in verses])
    expected = {3: 43, 4: 42, 5: 29, 6: 47, 7: 30}
    
    # Check count
    count_ok = len(verses) == expected[ch]
    
    # Check no gaps in verse numbers
    gaps = [i for i in range(1, expected[ch]+1) if i not in verse_nums]
    
    # Check famous verses are marked correctly
    famous_expected = {
        3: [3, 21, 27, 35, 37],
        4: [7, 8, 11, 18, 34],
        5: [10, 16, 18, 29],
        6: [6, 19, 29, 32, 47],
        7: [3, 7, 14, 16, 19]
    }
    famous_actual = [v['verse'] for v in verses if v.get('famous')]
    famous_missing = [n for n in famous_expected[ch] if n not in famous_actual]
    famous_extra = [n for n in famous_actual if n not in famous_expected[ch]]
    
    # Check no JSON bracket errors remain
    bracket_errors = sum(1 for v in verses for wm in v.get('word_meanings', []) if not isinstance(wm, dict))
    
    print(f"Chapter {ch}:")
    print(f"  Verses: {len(verses)}/{expected[ch]} {'✅' if count_ok else '❌'}")
    print(f"  Gaps: {gaps if gaps else 'None ✅'}")
    print(f"  Famous missing: {famous_missing if famous_missing else 'None ✅'}")
    print(f"  Famous extra: {famous_extra if famous_extra else 'None ✅'}")
    print(f"  Bracket errors: {bracket_errors if bracket_errors else '0 ✅'}")
    print()
