import json

files = {
    'Bhajans': 'data/bhajans.json',
    'Shlokas': 'data/shlokas.json',
    'Prayers': 'data/prayers.json',
    'Wisdom': 'data/wisdom.json',
    'Upanishads': 'data/upanishads.json',
    'Gita': 'data/gita.json'
}

print("--- CORRECT AUDIT ---")
for cat, path in files.items():
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            
        items = data
        if cat == 'Prayers': items = data['prayers']
        if cat == 'Wisdom': items = data['topics']
        if cat == 'Upanishads': items = data['upanishads']
        if cat == 'Gita': items = data['chapters']
            
        stubs = []
        for i in items:
            name = i.get('title_english') or i.get('title_roman') or i.get('slug') or str(i.get('chapter_number', ''))
            
            is_valid = False
            if cat == 'Bhajans' and i.get('verses') and len(i['verses']) > 0: is_valid = True
            if cat == 'Shlokas' and i.get('sanskrit'): is_valid = True
            if cat == 'Prayers' and i.get('steps') and len(i['steps']) > 0: is_valid = True
            if cat == 'Wisdom' and i.get('quotes') and len(i['quotes']) > 0: is_valid = True
            if cat == 'Upanishads' and i.get('key_concepts') and len(i['key_concepts']) > 0: is_valid = True
            if cat == 'Gita' and i.get('verses_count') > 0: is_valid = True
            
            if not is_valid:
                stubs.append(name)
                
        if stubs:
            print(f"[{cat}] - MISSING CONTENT FOR: {', '.join(stubs)}")
        else:
            print(f"[{cat}] - All {len(items)} items fully populated!")
            
    except Exception as e:
        print(f"[{cat}] - Error: {e}")
