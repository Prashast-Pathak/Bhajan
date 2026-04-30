import json
import os

def generate_seo(item, category, name_key='title_english', desc_key='meaning_english'):
    title = item.get(name_key, '')
    if not title:
        title = item.get('name_english', item.get('title_sanskrit', ''))
    
    desc = item.get(desc_key, '')
    if not desc:
        desc = item.get('intro_english', item.get('summary_english', item.get('theme_english', '')))
    
    # Clean up desc
    if isinstance(desc, str):
        desc = desc[:150] + ('...' if len(desc) > 150 else '')
    else:
        desc = title

    meta_title = f"{title} | {category.capitalize()} | Sanatan Gyan Sagar"
    meta_desc = f"Read and understand {title}. {desc}"
    keywords = [title, category, 'Hinduism', 'Sanatan Dharma', 'Meaning', 'Translation']

    # Custom additions based on category
    if category == 'shloka':
        keywords.extend(['Mantra', 'Sanskrit Shloka'])
    elif category == 'prayer':
        keywords.extend(['Puja', 'Aarti', 'Ritual'])
    elif category == 'wisdom':
        keywords.extend(['Quotes', 'Life lessons', 'Dharma'])
    elif category == 'upanishad':
        keywords.extend(['Vedas', 'Philosophy', 'Vedanta'])
    elif category == 'gita':
        keywords.extend(['Bhagavad Gita', 'Krishna', 'Verses'])

    return {
        'meta_title': meta_title,
        'meta_description': meta_desc,
        'keywords': keywords
    }

def process_file(filename, category, name_key='title_english', desc_key='meaning_english', list_key=None):
    filepath = os.path.join('data', filename)
    if not os.path.exists(filepath):
        return 0

    with open(filepath, 'r') as f:
        raw = json.load(f)
    
    data = raw.get(list_key, raw) if list_key and isinstance(raw, dict) else raw
    if not isinstance(data, list):
        # Could be a single object or different structure, we'll try to handle lists
        if isinstance(raw, dict) and 'chapters' in raw:
             data = raw['chapters']
             list_key = 'chapters'
        else:
             return 0

    fixed = 0
    for item in data:
        if not item.get('seo'):
            item['seo'] = generate_seo(item, category, name_key, desc_key)
            fixed += 1

    if list_key and isinstance(raw, dict):
        raw[list_key] = data
        to_save = raw
    else:
        to_save = data

    with open(filepath, 'w') as f:
        json.dump(to_save, f, indent=2, ensure_ascii=False)
    
    return fixed

if __name__ == '__main__':
    total_fixed = 0
    total_fixed += process_file('shlokas.json', 'shloka', 'title_english', 'meaning_english', 'shlokas')
    total_fixed += process_file('prayers.json', 'prayer', 'title_english', 'intro_english', 'prayers')
    total_fixed += process_file('wisdom.json', 'wisdom', 'title_english', 'intro_english', 'topics')
    total_fixed += process_file('upanishads.json', 'upanishad', 'name_english', 'theme_english')
    total_fixed += process_file('gita.json', 'gita', 'title_english', 'summary_english', 'chapters')
    print(f"✅ Injected SEO metadata into {total_fixed} items across 5 pillars.")
