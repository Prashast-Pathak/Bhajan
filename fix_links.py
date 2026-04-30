import os
import re

def fix_file(file_path, replacements):
    if not os.path.exists(file_path): return
    with open(file_path, 'r') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(file_path, 'w') as f:
        f.write(content)

# 1. index.html - fix gita chapters
fix_file('index.html', [
    ('href="/gita/chapter-${c.chapter}/"', 'href="bhagavad-gita.html#ch${c.chapter}"')
])

# 2. bhajans.html
fix_file('bhajans.html', [
    ('href="bhajan.html?slug=${b.slug}"', 'href="/bhajan/${b.slug}/"')
])

# 3. wisdom.html
fix_file('wisdom.html', [
    ('href="bhagavad-gita.html#ch${q.gita_chapter}v${q.gita_verse}"', 'href="/gita/${q.gita_chapter}/${q.gita_verse}/"')
])

# 4. upanishads.html
fix_file('upanishads.html', [
    ('href="wisdom.html?topic=${verse.cross_links.wisdom_topic}"', 'href="/wisdom/${verse.cross_links.wisdom_topic}/"'),
    ('href="shlokas.html?slug=${verse.cross_links.shloka_slug}"', 'href="/shloka/${verse.cross_links.shloka_slug}/"'),
    ('href="bhagavad-gita.html?chapter=${verse.cross_links.gita_chapter}&verse=${verse.cross_links.gita_verse}"', 'href="/gita/${verse.cross_links.gita_chapter}/${verse.cross_links.gita_verse}/"'),
    ('href="bhagavad-gita.html?chapter=${verse.cross_links.gita_chapter}"', 'href="bhagavad-gita.html#ch${verse.cross_links.gita_chapter}"')
])

# 5. bhagavad-gita.html
fix_file('bhagavad-gita.html', [
    ('href="/bhagavad-gita.html?chapter=${ch.chapter}&verse=${v.verse}"', 'href="/gita/${ch.chapter}/${v.verse}/"'),
    ('href="/bhagavad-gita.html?chapter=${v.chapter}&verse=${v.verse}"', 'href="/gita/${v.chapter}/${v.verse}/"'),
    ('href="/bhagavad-gita.html?chapter=${ch.chapter}&verse=${ov.verse}"', 'href="/gita/${ch.chapter}/${ov.verse}/"'),
    ('href="/wisdom.html?topic=${t}"', 'href="/wisdom/${t}/"')
])

print("Fixed cross-links across all templates.")
