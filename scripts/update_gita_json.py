import json
import urllib.request
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan/data')
CURRENT_GITA_PATH = ROOT / 'gita.json'

def fetch_json(url):
    print(f"Fetching {url}...")
    req = urllib.request.urlopen(url)
    return json.loads(req.read().decode('utf-8'))

print("Downloading complete Gita data from GitHub...")
verses_data = fetch_json('https://raw.githubusercontent.com/gita/gita/master/data/verse.json')
translations_data = fetch_json('https://raw.githubusercontent.com/gita/gita/master/data/translation.json')

print("Loading existing gita.json for chapter metadata...")
with open(CURRENT_GITA_PATH, 'r', encoding='utf-8') as f:
    current_gita = json.load(f)

# Group verses by chapter
verses_by_chapter = {i: [] for i in range(1, 19)}
for v in verses_data:
    ch = v['chapter_number']
    if 1 <= ch <= 18:
        verses_by_chapter[ch].append(v)

# Group translations by verse_id
# We want Hindi (Swami Ramsukhdas author_id=11 or lang='hindi')
# and English (Swami Sivananda author_id=16 or lang='english')
translations_by_verse = {}
for t in translations_data:
    vid = t['verse_id']
    if vid not in translations_by_verse:
        translations_by_verse[vid] = {'hindi': '', 'english': ''}
    
    # Author ID 1 or 11 are often good for Hindi
    if t['lang'] == 'hindi' and not translations_by_verse[vid]['hindi']:
        translations_by_verse[vid]['hindi'] = t['description']
    # Author ID 16 (Sivananda) or 18 (Gambhirananda) for English
    if t['lang'] == 'english' and t['authorName'] == 'Swami Sivananda':
        translations_by_verse[vid]['english'] = t['description']
    elif t['lang'] == 'english' and not translations_by_verse[vid]['english']:
        translations_by_verse[vid]['english'] = t['description']

# Build the new chapters array, preserving existing chapter metadata
new_chapters = []

for ch_data in current_gita.get('chapters', []):
    ch_num = ch_data['chapter']
    print(f"Processing Chapter {ch_num}...")
    
    # Preserve existing chapter metadata
    new_ch = {
        k: v for k, v in ch_data.items() if k != 'verses' and k != 'verse_count'
    }
    
    # Get the verses for this chapter from the newly downloaded data
    ch_verses_raw = verses_by_chapter.get(ch_num, [])
    ch_verses_raw.sort(key=lambda x: x['verse_number'])
    
    new_verses = []
    
    # Create a lookup for existing verses to preserve any custom formatting if we want
    # but the simplest is just to rebuild from the fresh data to ensure completeness
    for v_raw in ch_verses_raw:
        vid = v_raw['id']
        v_num = v_raw['verse_number']
        
        # Clean up text
        sanskrit = v_raw.get('text', '').strip()
        sanskrit = sanskrit.replace('।।', '॥') # Standardize double danda
        
        roman = v_raw.get('transliteration', '').strip()
        
        # Parse word meanings from "word—meaning; word—meaning"
        wm_str = v_raw.get('word_meanings', '').strip()
        word_meanings = []
        if wm_str:
            pairs = wm_str.split(';')
            for pair in pairs:
                parts = pair.split('—')
                if len(parts) == 2:
                    word_meanings.append({
                        "word": parts[0].strip(),
                        "meaning_english": parts[1].strip(),
                        "meaning_hindi": "" # The API mostly has English word meanings
                    })
        
        trans = translations_by_verse.get(vid, {})
        hindi_trans = trans.get('hindi', '').strip()
        english_trans = trans.get('english', '').strip()
        
        # Remove commentary tags if they exist like "।।1.1।। धृतराष्ट्र बोले (टिप्पणी प0 1.2)..."
        if hindi_trans.startswith('।।'):
            import re
            hindi_trans = re.sub(r'^।।.*?।।\s*', '', hindi_trans)
            hindi_trans = re.sub(r'\(टिप्पणी.*?\)', '', hindi_trans).strip()
            
        
        new_verse = {
            "verse": v_num,
            "slug": f"chapter-{ch_num}-verse-{v_num}",
            "sanskrit": sanskrit,
            "roman": roman,
            "word_meanings": word_meanings,
            "hindi_translation": hindi_trans,
            "english_translation": english_trans,
            "purport_hindi": "",
            "purport_english": "",
            "practical_application_hindi": "",
            "practical_application_english": "",
            "topics": []
        }
        
        # If the verse existed in the old file, copy over purports, practical application, and topics
        for old_v in ch_data.get('verses', []):
            if old_v['verse'] == v_num:
                # Keep the new sanskrit and translations as they are complete, 
                # but merge the custom fields
                new_verse['purport_hindi'] = old_v.get('purport_hindi', '')
                new_verse['purport_english'] = old_v.get('purport_english', '')
                new_verse['practical_application_hindi'] = old_v.get('practical_application_hindi', '')
                new_verse['practical_application_english'] = old_v.get('practical_application_english', '')
                new_verse['topics'] = old_v.get('topics', [])
                
                # If the old verse had better hindi word meanings, merge them
                old_wm = {wm['word']: wm for wm in old_v.get('word_meanings', [])}
                for new_wm in new_verse['word_meanings']:
                    if new_wm['word'] in old_wm:
                        new_wm['meaning_hindi'] = old_wm[new_wm['word']].get('meaning_hindi', '')
                break
                
        new_verses.append(new_verse)
    
    new_ch['verse_count'] = len(new_verses)
    new_ch['verses'] = new_verses
    new_chapters.append(new_ch)

current_gita['chapters'] = new_chapters
current_gita['last_updated'] = '2026-05-15'

# Save the updated file
import tempfile
import shutil

temp_file = tempfile.mktemp()
with open(temp_file, 'w', encoding='utf-8') as f:
    json.dump(current_gita, f, ensure_ascii=False, indent=2)

shutil.move(temp_file, CURRENT_GITA_PATH)
print(f"Successfully updated {CURRENT_GITA_PATH} with all verses.")

# Print summary
total_verses = sum(len(c['verses']) for c in new_chapters)
print(f"Total chapters: {len(new_chapters)}")
print(f"Total verses: {total_verses}")
