import json
import urllib.request
import os
import re

print("Downloading Gita data from github...")
base_url = "https://raw.githubusercontent.com/gita/gita/master/data/"
urls = {
    "chapters": base_url + "chapters.json",
    "verses": base_url + "verse.json",
    "translations": base_url + "translation.json",
    "commentaries": base_url + "commentary.json"
}

data_cache = {}
for key, url in urls.items():
    print(f"Fetching {url}...")
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data_cache[key] = json.loads(response.read().decode('utf-8'))

print("Data fetched. Processing...")

# Index chapters
chapters_by_num = {c['chapter_number']: c for c in data_cache['chapters']}

# Index verses
verses_by_chapter = {}
for v in data_cache['verses']:
    ch_num = v['chapter_number']
    if ch_num not in verses_by_chapter:
        verses_by_chapter[ch_num] = []
    verses_by_chapter[ch_num].append(v)

# Index translations by verse_id
translations_by_verse = {}
for t in data_cache['translations']:
    vid = t['verse_id']
    if vid not in translations_by_verse:
        translations_by_verse[vid] = []
    translations_by_verse[vid].append(t)

# Index commentaries by verse_id
commentaries_by_verse = {}
for c in data_cache['commentaries']:
    vid = c['verse_id']
    if vid not in commentaries_by_verse:
        commentaries_by_verse[vid] = []
    commentaries_by_verse[vid].append(c)

def get_preferred(items, preferred_authors, default_lang=None):
    if not items:
        return ""
    
    # Try to find preferred authors in order
    for author in preferred_authors:
        for item in items:
            if item.get('authorName') == author:
                # remove prefix like "।।1.1।। धृतराष्ट्र बोले - " if present
                desc = item.get('description', '')
                desc = re.sub(r'।।\d+\.\d+।।\s*', '', desc)
                desc = re.sub(r'\(टिप्पणी प0 \d+\.\d+\)', '', desc)
                return desc.strip()
                
    # Fallback to any in the correct language
    for item in items:
        if default_lang and item.get('lang') == default_lang:
            desc = item.get('description', '')
            desc = re.sub(r'।।\d+\.\d+।।\s*', '', desc)
            return desc.strip()
    return ""

def parse_word_meanings(wm_str):
    if not wm_str:
        return []
    result = []
    pairs = wm_str.split(';')
    for pair in pairs:
        # Sometimes separated by '—', sometimes by '-'
        if '—' in pair:
            parts = pair.split('—', 1)
        elif '-' in pair:
            parts = pair.split('-', 1)
        else:
            parts = [pair, ""]
            
        word = parts[0].strip()
        meaning = parts[1].strip() if len(parts) > 1 else ""
        if word:
            result.append({
                "word": word,
                "meaning_hindi": "",
                "meaning_english": meaning
            })
    return result

new_chapters = []

for ch_num in range(8, 19):
    c_data = chapters_by_num.get(ch_num)
    if not c_data:
        continue
        
    chapter_obj = {
        "chapter": ch_num,
        "title_sanskrit": c_data.get('name', ''),
        "title_english": c_data.get('name_translation', ''),
        "title_hindi": c_data.get('name_transliterated', ''),  # Best fallback
        "summary_hindi": c_data.get('chapter_summary_hindi', ''),
        "summary_english": c_data.get('chapter_summary', ''),
        "verse_count": c_data.get('verses_count', 0),
        "key_themes": [],
        "seo": {
            "meta_title": f"Bhagavad Gita Chapter {ch_num} - {c_data.get('name_translation', '')}",
            "meta_description": f"Read and understand Chapter {ch_num} of the Bhagavad Gita: {c_data.get('name_translation', '')} with English and Hindi translations.",
            "keywords": ["Bhagavad Gita", f"Chapter {ch_num}", c_data.get('name_translation', '')]
        },
        "verses": []
    }
    
    v_list = verses_by_chapter.get(ch_num, [])
    # Sort verses by verse number
    v_list.sort(key=lambda x: x['verse_number'])
    
    for v in v_list:
        vid = v['id']
        v_num = v['verse_number']
        
        t_list = translations_by_verse.get(vid, [])
        c_list = commentaries_by_verse.get(vid, [])
        
        # Select best translations
        hin_trans = get_preferred(t_list, ["Swami Ramsukhdas", "Swami Tejomayananda"], "hindi")
        eng_trans = get_preferred(t_list, ["Swami Adidevananda", "Swami Sivananda"], "english")
        
        hin_comm = get_preferred(c_list, ["Swami Chinmayananda"], "hindi")
        eng_comm = get_preferred(c_list, ["Swami Chinmayananda", "Swami Sivananda"], "english")
        
        verse_obj = {
            "verse": v_num,
            "slug": f"chapter-{ch_num}-verse-{v_num}",
            "sanskrit": v.get('text', '').strip(),
            "roman": v.get('transliteration', '').strip(),
            "word_meanings": parse_word_meanings(v.get('word_meanings', '')),
            "hindi_translation": hin_trans,
            "english_translation": eng_trans,
            "hindi_commentary": hin_comm,
            "english_commentary": eng_comm,
            "life_application": "",
            "topics": [],
            "famous": False
        }
        chapter_obj["verses"].append(verse_obj)
        
    new_chapters.append(chapter_obj)

print(f"Generated {len(new_chapters)} chapters.")

# Now load existing gita.json and append
gita_path = "/Users/prashastpathak/Bhajan/data/gita.json"
with open(gita_path, 'r', encoding='utf-8') as f:
    gita_data = json.load(f)

# Ensure chapters 8-18 don't already exist to avoid duplication
existing_chs = set(c['chapter'] for c in gita_data.get('chapters', []))

added = 0
for ch in new_chapters:
    if ch['chapter'] not in existing_chs:
        gita_data['chapters'].append(ch)
        added += 1

# Sort chapters
gita_data['chapters'].sort(key=lambda x: x['chapter'])

with open(gita_path, 'w', encoding='utf-8') as f:
    json.dump(gita_data, f, ensure_ascii=False, indent=2)

print(f"Successfully appended {added} chapters to gita.json!")
