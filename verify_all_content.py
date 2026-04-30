import json

def verify_bhajans():
    with open('data/bhajans.json', 'r') as f:
        data = json.load(f)
    print("\n--- BHAJANS ---")
    all_good = True
    for item in data:
        if not item.get('verses') or len(item['verses']) == 0:
            print(f"Missing verses: {item.get('slug')}")
            all_good = False
    if all_good: print("All Bhajans have content.")

def verify_shlokas():
    with open('data/shlokas.json', 'r') as f:
        data = json.load(f)
        if isinstance(data, dict):
            data = data.get('shlokas', [])
    print("\n--- SHLOKAS ---")
    all_good = True
    for item in data:
        if not item.get('sanskrit') or not item.get('word_by_word'):
            print(f"Missing content: {item.get('slug')}")
            all_good = False
    if all_good: print("All Shlokas have content.")

def verify_prayers():
    with open('data/prayers.json', 'r') as f:
        data = json.load(f).get('prayers', [])
    print("\n--- PRAYERS ---")
    all_good = True
    for item in data:
        if not item.get('steps') or len(item['steps']) == 0:
            print(f"Missing steps: {item.get('slug')}")
            all_good = False
    if all_good: print("All Prayers have content.")

def verify_wisdom():
    with open('data/wisdom.json', 'r') as f:
        data = json.load(f).get('topics', [])
    print("\n--- WISDOM ---")
    all_good = True
    for item in data:
        if not item.get('quotes') or len(item['quotes']) == 0:
            print(f"Missing quotes: {item.get('slug')}")
            all_good = False
    if all_good: print("All Wisdom Topics have content.")

def verify_upanishads():
    with open('data/upanishads.json', 'r') as f:
        data = json.load(f)
    print("\n--- UPANISHADS ---")
    all_good = True
    for item in data:
        if not item.get('verses') or len(item['verses']) == 0:
            print(f"Missing verses: {item.get('slug')}")
            all_good = False
    if all_good: print("All Upanishads have content.")

def verify_gita():
    with open('data/gita.json', 'r') as f:
        data = json.load(f).get('chapters', [])
    print("\n--- GITA ---")
    all_good = True
    for ch in data:
        if not ch.get('verses') or len(ch['verses']) == 0:
            print(f"Missing verses: Chapter {ch.get('chapter')}")
            all_good = False
    if all_good: print("All Gita Chapters have content.")

try:
    verify_bhajans()
    verify_shlokas()
    verify_prayers()
    verify_wisdom()
    verify_upanishads()
    verify_gita()
except Exception as e:
    print(f"Error: {e}")
