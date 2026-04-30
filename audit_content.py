import json

files = {
    'Bhajans': ('data/bhajans.json', 'verses'),
    'Shlokas': ('data/shlokas.json', 'shlokas'),
    'Prayers': ('data/prayers.json', 'prayers'),
    'Wisdom': ('data/wisdom.json', 'topics'),
    'Upanishads': ('data/upanishads.json', 'upanishads'),
    'Gita': ('data/gita.json', None)
}

print("--- COMPLETE CONTENT AUDIT ---")

for category, (filepath, key) in files.items():
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        if key and isinstance(data, dict) and key in data:
            items = data[key]
        elif isinstance(data, list):
            items = data
        else:
            items = []
            
        print(f"\n[{category}] - Total Items: {len(items)}")
        
        for item in items:
            name = item.get('title_roman') or item.get('title_english') or item.get('title') or item.get('slug')
            
            # Check length of content
            length = 0
            if 'verses' in item and isinstance(item['verses'], list):
                length = len(item['verses'])
            elif 'steps' in item and isinstance(item['steps'], list):
                length = len(item['steps'])
            elif 'lines' in item and isinstance(item['lines'], list):
                length = len(item['lines'])
            elif 'mantras' in item and isinstance(item['mantras'], list):
                length = len(item['mantras'])
            elif 'points' in item and isinstance(item['points'], list):
                length = len(item['points'])
            elif 'key_concepts' in item and isinstance(item['key_concepts'], list):
                length = len(item['key_concepts'])
            elif 'shlokas' in item and isinstance(item['shlokas'], list):
                length = len(item['shlokas'])
                
            status = "OK"
            if length == 0:
                status = "EMPTY (STUB)"
            elif category == 'Bhajans' and length <= 2:
                status = f"SHORT ({length} verses) - Needs check"
            elif category == 'Prayers' and length <= 3:
                status = f"SHORT ({length} steps) - Needs check"
                
            if status != "OK":
                print(f"  - {name}: {status}")
                
    except Exception as e:
        print(f"Error reading {category}: {e}")
