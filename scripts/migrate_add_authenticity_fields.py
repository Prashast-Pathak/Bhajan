#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write(path, obj):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')


def ensure(d, k, v):
    if k not in d:
        d[k] = v


def patch_bhajans(arr):
    for it in arr:
        ensure(it, 'source_name', it.get('title_english') or it.get('title_hindi') or 'Traditional Bhajan')
        ensure(it, 'source_ref', 'Traditional source')
        ensure(it, 'source_edition', 'Trusted published edition')
        ensure(it, 'is_excerpt', False)
        ensure(it, 'excerpt_range', 'full')
        ensure(it, 'verification_notes', 'Verify with trusted source before publish.')
        for blk in it.get('verses', []) if isinstance(it.get('verses', []), list) else []:
            ensure(blk, 'source_name', it.get('source_name', ''))
            ensure(blk, 'source_ref', it.get('source_ref', ''))
            ensure(blk, 'source_line_index', '')


def patch_shlokas(arr):
    for it in arr:
        ensure(it, 'source_name', it.get('title_english') or it.get('title_hindi') or 'Shloka')
        ensure(it, 'source_edition', 'Trusted published edition')
        ensure(it, 'is_excerpt', False)
        ensure(it, 'excerpt_range', 'full verse')
        ensure(it, 'verification_notes', 'Verify text and reference against trusted source.')


def patch_prayers(d):
    arr = d.get('prayers', []) if isinstance(d, dict) else []
    for it in arr:
        ensure(it, 'source_name', it.get('title_english') or it.get('title_hindi') or 'Traditional Prayer')
        ensure(it, 'source_ref', 'Traditional paddhati')
        ensure(it, 'source_edition', 'Trusted puja manual or tradition')
        ensure(it, 'is_excerpt', True)
        ensure(it, 'excerpt_range', 'short sequence')
        ensure(it, 'verification_notes', 'Validate steps with tradition before publish.')
        for st in it.get('steps', []) if isinstance(it.get('steps', []), list) else []:
            ensure(st, 'source_name', it.get('source_name', ''))
            ensure(st, 'source_ref', it.get('source_ref', ''))
            ensure(st, 'source_line_index', f"Step {st.get('step','')}")


def patch_gita(d):
    chapters = d.get('chapters', []) if isinstance(d, dict) else []
    for ch in chapters:
        ensure(ch, 'source_name', 'Bhagavad Gita')
        ensure(ch, 'source_ref', f"Chapter {ch.get('chapter','')}")
        ensure(ch, 'source_edition', 'Trusted published edition')
        ensure(ch, 'is_excerpt', False)
        ensure(ch, 'excerpt_range', 'full chapter context')
        ensure(ch, 'verification_notes', 'Verify verse text and numbering.')
        for v in ch.get('verses', []) if isinstance(ch.get('verses', []), list) else []:
            verse_ref = f"{ch.get('chapter','')}.{v.get('verse','')}"
            ensure(v, 'source_name', 'Bhagavad Gita')
            ensure(v, 'source_ref', verse_ref)
            ensure(v, 'source_line_index', verse_ref)


def patch_upanishads(arr):
    for it in arr:
        ensure(it, 'source_name', it.get('name_english') or it.get('name_hindi') or 'Upanishad')
        ensure(it, 'source_ref', 'Primary text')
        ensure(it, 'source_edition', 'Trusted published edition')
        ensure(it, 'is_excerpt', False)
        ensure(it, 'excerpt_range', 'full text context')
        ensure(it, 'verification_notes', 'Verify mantra text and numbering.')
        for v in it.get('verses', []) if isinstance(it.get('verses', []), list) else []:
            ensure(v, 'source_name', it.get('source_name', ''))
            ensure(v, 'source_ref', f"Mantra {v.get('verse','')}")
            ensure(v, 'source_line_index', str(v.get('verse','')))


def patch_wisdom(d):
    topics = d.get('topics', []) if isinstance(d, dict) else []
    for it in topics:
        ensure(it, 'source_name', 'Scripture-backed wisdom compilation')
        ensure(it, 'source_ref', 'Curated source references')
        ensure(it, 'source_edition', 'Trusted scripture editions')
        ensure(it, 'is_excerpt', True)
        ensure(it, 'excerpt_range', 'selected quotes')
        ensure(it, 'verification_notes', 'Every quote must map to source verse.')
        for q in it.get('quotes', []) if isinstance(it.get('quotes', []), list) else []:
            ensure(q, 'source_name', q.get('source', ''))
            ensure(q, 'source_edition', 'Trusted edition')
            ensure(q, 'source_line_index', q.get('source_ref', ''))


def main():
    bh = read(DATA/'bhajans.json'); patch_bhajans(bh); write(DATA/'bhajans.json', bh)
    sh = read(DATA/'shlokas.json'); patch_shlokas(sh); write(DATA/'shlokas.json', sh)
    pr = read(DATA/'prayers.json'); patch_prayers(pr); write(DATA/'prayers.json', pr)
    gi = read(DATA/'gita.json'); patch_gita(gi); write(DATA/'gita.json', gi)
    up = read(DATA/'upanishads.json'); patch_upanishads(up); write(DATA/'upanishads.json', up)
    wi = read(DATA/'wisdom.json'); patch_wisdom(wi); write(DATA/'wisdom.json', wi)
    print('Authenticity fields added to all data JSON files.')


if __name__ == '__main__':
    main()
