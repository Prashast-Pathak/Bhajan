import re

with open('bhajan.html', 'r', encoding='utf-8') as f:
    bhajan_html = f.read()

# Extract CSS
css_match = re.search(r'(\.main-header \{.*?\n  \}\n</style>)', bhajan_html, re.DOTALL)
if not css_match:
    print("Could not extract CSS from bhajan.html")
    exit(1)
header_css = css_match.group(1).replace('</style>', '')

# Extract Mobile Menu JS
js_match = re.search(r'(function toggleMobileMenu.*?\}\n)', bhajan_html, re.DOTALL)
if not js_match:
    print("Could not extract JS from bhajan.html")
    exit(1)
mobile_js = js_match.group(1)

# Now read gita.html
with open('bhagavad-gita.html', 'r', encoding='utf-8') as f:
    gita_html = f.read()

# 1. Replace the CSS
if '.main-header' not in gita_html:
    gita_html = gita_html.replace('</style>', header_css + '</style>')

# 2. Build the new Header HTML
new_header = """<header class="main-header">
  <div class="header-inner">
    <!-- Left: Logo + Hamburger -->
    <div style="display:flex; align-items:center; gap:10px;">
      <button class="hamburger-btn" onclick="toggleMobileMenu()" aria-label="Open Menu">
        <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.5" fill="none"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
      <a href="index.html" class="logo-link">
        <div class="logo-om">ॐ</div>
        <div class="logo-text">
          <span class="logo-title" style="color:var(--krishna);">भगवद गीता</span>
          <span class="logo-sub">Sanatan Gyan Sagar</span>
        </div>
      </a>
    </div>

    <!-- Center: Desktop Nav -->
    <nav class="desktop-nav" aria-label="Main navigation">
      <a href="index.html">Home</a>
      <a href="bhajans.html">Bhajans</a>
      <a href="bhagavad-gita.html" class="active">Gita</a>
      <a href="shlokas.html">Shlokas</a>
      <a href="prayers.html">Prayers</a>
      <a href="upanishads.html">Upanishads</a>
      <a href="wisdom.html">Wisdom</a>
    </nav>

    <!-- Right: Icons -->
    <div class="header-icons">
      <button class="header-icon-btn" id="font-toggle" aria-label="Font size" title="Font size">अ</button>
      <button class="header-icon-btn" id="dark-toggle" aria-label="Dark mode" title="Dark mode">🌙</button>
      <button class="header-icon-btn" id="search-toggle" onclick="toggleSearch()" aria-label="Search" title="Search">🔍</button>
      <button class="header-icon-btn" onclick="window.location.href='favorites.html'" aria-label="Saved" title="Saved">❤️</button>
    </div>
  </div>
  
  <!-- Search bar -->
  <div id="search-bar" class="hidden px-4 py-2 border-t" style="border-color:var(--border);">
    <input id="search-input" type="search"
      placeholder="श्लोक, विषय खोजें... Search verses, topics..."
      class="w-full text-base p-3 rounded-lg border-2 outline-none"
      style="border-color:var(--border);background:white;color:var(--text);"
      oninput="handleSearch(this.value)"
      onfocus="this.style.borderColor='var(--krishna)'"
      onblur="this.style.borderColor='var(--border)'">
    <div id="search-results" class="hidden bg-white shadow-xl rounded-lg mt-1 overflow-hidden" style="border:1px solid var(--border);max-height:320px;overflow-y:auto;"></div>
  </div>
</header>

<!-- Mobile Menu Overlay -->
<div id="mobileMenuOverlay" class="mobile-menu-overlay" onclick="toggleMobileMenu()"></div>
<div id="mobileMenu" class="mobile-menu-drawer">
  <div class="mobile-menu-header">
    <div style="font-family:var(--font-hindi); font-weight:700; color:var(--krishna); font-size:18px;">
      भगवद गीता
    </div>
    <button class="close-menu-btn" onclick="toggleMobileMenu()">×</button>
  </div>
  <div class="mobile-menu-links">
    <a href="index.html">🏠 Home</a>
    <div class="menu-divider"></div>
    <a href="bhajans.html">🪔 Bhajans</a>
    <a href="bhagavad-gita.html" style="color:var(--krishna);">📖 Bhagavad Gita</a>
    <a href="shlokas.html">🕉️ Shlokas</a>
    <a href="prayers.html">🙏 Prayers</a>
    <a href="upanishads.html">📜 Upanishads</a>
    <a href="wisdom.html">💬 Wisdom</a>
    <div class="menu-divider"></div>
    <a href="favorites.html">❤️ Saved Favorites</a>
  </div>
</div>
"""

# Replace existing header in gita
old_header_pattern = r'<header class="sticky.*?</header>'
gita_html = re.sub(old_header_pattern, new_header, gita_html, flags=re.DOTALL)

# Inject JS if not present
if 'toggleMobileMenu' not in gita_html:
    gita_html = gita_html.replace('</script>\n</body>', mobile_js + '\n</script>\n</body>')

with open('bhagavad-gita.html', 'w', encoding='utf-8') as f:
    f.write(gita_html)

print("Updated bhagavad-gita.html")
