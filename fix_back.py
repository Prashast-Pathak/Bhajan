import os
import glob

# HTML templates
templates = [
    "index.html",
    "bhajans.html",
    "bhajan.html",
    "shlokas.html",
    "shloka.html",
    "wisdom.html",
    "prayers.html",
    "upanishads.html",
    "bhagavad-gita.html",
    "favorites.html",
    "about.html",
    "contact.html",
    "privacy-policy.html"
]

old_script = """        function handleMainHeaderBack() {
          const p = window.location.pathname;
          const topLevel = ['/index.html', '/', '/bhajans.html', '/shlokas.html', '/wisdom.html', '/prayers.html', '/upanishads.html', '/bhagavad-gita.html', '/favorites.html'];
          if (topLevel.some(t => p.endsWith(t))) {
            window.location.href = 'index.html';
          } else if (document.referrer && new URL(document.referrer).origin === window.location.origin) {
            window.history.back();
          } else {
            window.location.href = 'index.html';
          }
        }"""

new_script = """        function handleMainHeaderBack() {
          const p = window.location.pathname;
          const isTopLevel = p === '/' || p === '/index.html' || p.endsWith('/bhajans.html') || p.endsWith('/shlokas.html') || p.endsWith('/wisdom.html') || p.endsWith('/prayers.html') || p.endsWith('/upanishads.html') || p.endsWith('/bhagavad-gita.html') || p.endsWith('/favorites.html');
          
          if (isTopLevel) {
            window.location.href = '/';
          } else if (document.referrer && new URL(document.referrer).origin === window.location.origin) {
            window.history.back();
          } else {
            window.location.href = '/';
          }
        }"""

for f in templates:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
            
        content = content.replace(old_script, new_script)
        
        with open(f, 'w') as file:
            file.write(content)

print("Fixed Back Button logic in all templates.")
