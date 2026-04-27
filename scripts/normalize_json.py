import json
from pathlib import Path

DATA_DIR = Path('data')

BHAJAN_SCHEMA = {
    "id": None,
    "slug": "",
    "title_hindi": "",
    "title_roman": "",
    "title_english": "",
    "deity": "",
    "duration_minutes": None,
    "raga": None,
    "composer": "Traditional",
    "language": "Hindi",
    "timing": "",
    "occasion": "",
    "tags": [],
    "topics": [],
    "priority": 999,
    "featured": False,
    "festival": [],
    "when_to_sing": {
        "time": [],
        "occasion": []
    },
    "story": None,
    "story_hindi": None,
    "significance": None,
    "significance_hindi": None,
    "benefits": [],
    "seo": {
        "meta_title": "",
        "meta_description": "",
        "keywords": []
    },
    "verses": [],
    "related": []
}

def normalize_file(file_path, schema):
    if not file_path.exists():
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    normalized_data = []
    for item in data:
        normalized_item = {}
        for key, default_val in schema.items():
            if key in item:
                # Keep existing value if it's not null, or if default is also None
                if item[key] is not None or default_val is None:
                    normalized_item[key] = item[key]
                else:
                    normalized_item[key] = default_val
            else:
                # Missing key, provide default
                # deep copy default for dict/list
                if isinstance(default_val, list):
                    normalized_item[key] = []
                elif isinstance(default_val, dict):
                    normalized_item[key] = {}
                    for k, v in default_val.items():
                        normalized_item[key][k] = [] if isinstance(v, list) else v
                else:
                    normalized_item[key] = default_val
        
        # Also copy over any extra keys that might exist (just in case)
        for key in item:
            if key not in schema:
                normalized_item[key] = item[key]
                
        normalized_data.append(normalized_item)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(normalized_data, f, ensure_ascii=False, indent=2)
    print(f"Normalized {file_path.name}")

if __name__ == '__main__':
    normalize_file(DATA_DIR / 'bhajans.json', BHAJAN_SCHEMA)
