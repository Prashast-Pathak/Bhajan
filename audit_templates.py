import os
import re

files = ['wisdom.html', 'upanishads.html', 'prayers.html', 'shlokas.html', 'bhagavad-gita.html', 'bhajans.html']
for f in files:
    with open(f, 'r') as file:
        content = file.read()
        print(f'=== {f} ===')
        
        # Check back button logic
        if 'window.location.pathname;' in content and 'p ===' in content:
            print('Back button logic: FIXED')
        else:
            print('Back button logic: BROKEN')
            
        # Extract link patterns in JS
        links = re.findall(r'href=[\"\'\`]?([^\`\"\'<>]+)[\"\'\`]?', content)
        # We only care about links generated in the JS loop for the cards
        card_links = [l for l in links if '${' in l or '?' in l]
        print('Dynamic Card Links found in JS:', set(card_links))
