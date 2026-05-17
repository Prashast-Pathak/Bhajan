import json
import re
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')
DATA = ROOT / 'data'

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# 1. Fix Hub Pages - Add SEO content
hub_texts = {
    'bhajans.html': '<h2>About Hindu Bhajans</h2><p>Bhajans are devotional songs that express love, surrender, and reverence to the divine. Rooted in ancient Indian traditions, these songs are a core part of Bhakti Yoga (the path of devotion). Singing or listening to bhajans purifies the mind, brings inner peace, and connects the soul with the supreme. Explore our vast collection of Hindi bhajans, complete with translations, meanings, and Roman transliterations to help you chant accurately.</p>',
    'shlokas.html': '<h2>Sacred Sanskrit Shlokas</h2><p>Shlokas are ancient Sanskrit verses, often structured in specific poetic meters, used for prayer, meditation, and passing down spiritual wisdom. These verses carry powerful phonetic vibrations that calm the nervous system and awaken spiritual consciousness. Our library provides authentic Sanskrit text, Hindi meanings, and English translations of the most powerful daily shlokas, mantras, and stotras for your spiritual practice.</p>',
    'prayers.html': '<h2>Hindu Prayers and Puja Guide</h2><p>Prayer (Prarthana) and Puja are foundational practices in Sanatana Dharma. They are ways to express gratitude, seek guidance, and align oneself with cosmic energies. This section offers step-by-step guides for daily prayers, aarti rituals, and specific deity worship. Understand the profound meanings behind these rituals with our detailed English and Hindi translations, making your devotional practice more meaningful.</p>',
    'upanishads.html': '<h2>Wisdom of the Upanishads</h2><p>The Upanishads are the philosophical culmination of the Vedas, exploring the ultimate nature of reality (Brahman) and the individual soul (Atman). They form the core of Vedanta philosophy. Here, we distill the profound teachings, stories, and metaphors from major Upanishads like the Isha, Kena, Katha, and Brihadaranyaka. Dive deep into these timeless texts to discover the ultimate truth of existence.</p>',
    'wisdom.html': '<h2>Spiritual Wisdom & Quotes</h2><p>Sanatana Dharma offers a wealth of practical wisdom for navigating the complexities of human life. This section categorizes profound quotes, teachings, and life lessons from ancient sages, scriptures, and spiritual masters. Whether you are seeking guidance on dharma (duty), karma (action), peace, or self-realization, you will find transformative insights translated clearly into English and Hindi.</p>'
}

for filename, text in hub_texts.items():
    p = ROOT / filename
    if not p.exists(): continue
    content = p.read_text(encoding='utf-8')
    # Inject before the <main> tag or inside it
    if '<div class="content-wrapper"' in content:
        content = content.replace('<div class="content-wrapper"', f'<article class="seo-content" style="padding: 20px; max-width: 1100px; margin: 0 auto; color: var(--text-sec);">{text}</article>\n<div class="content-wrapper"')
        p.write_text(content, encoding='utf-8')

# 2. Fix Index.html Orphan Pages
bhajans = load_json(DATA / 'bhajans.json')
gita = load_json(DATA / 'gita.json')['chapters']

links_html = '<div class="seo-sitemap" style="padding: 20px; max-width: 1100px; margin: 0 auto;"><h3>Popular Links</h3><ul style="display: flex; flex-wrap: wrap; gap: 10px; list-style: none; padding: 0;">'
for b in bhajans[:15]:
    links_html += f'<li><a href="/bhajan/{b["slug"]}/" style="color: var(--saffron); text-decoration: none;">{b["title_roman"]}</a></li>'
for c in gita:
    links_html += f'<li><a href="/gita/{c["chapter"]}/" style="color: var(--saffron); text-decoration: none;">Bhagavad Gita Chapter {c["chapter"]}</a></li>'
links_html += '</ul></div>'

idx = ROOT / 'index.html'
idx_content = idx.read_text(encoding='utf-8')
if '<div class="seo-sitemap"' not in idx_content:
    idx_content = idx_content.replace('</main>', f'</main>\n{links_html}')
    idx.write_text(idx_content, encoding='utf-8')

print("Fixed Hubs and Index!")
