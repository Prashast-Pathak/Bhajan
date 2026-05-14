import re
import glob
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

RICH_CSS = """<style id="rich-mobile-menu-styles">
  .mobile-menu-links details { border-bottom: 1px solid var(--border, #D9CDBA); }
  .mobile-menu-links details summary { padding: 10px 20px; color: var(--text-sec, #5C3D20); font-size: 13px; font-weight: 700; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; }
  .mobile-menu-links details summary::-webkit-details-marker { display: none; }
  .mobile-menu-links details summary::after { content: '+'; font-size: 1.1rem; color: var(--saffron, #C96A1F); }
  .mobile-menu-links details[open] summary::after { content: '−'; }
  .mobile-menu-links details[open] summary { background: var(--surface2, #E6DDD0); color: var(--saffron, #C96A1F); }
  .details-content { background: var(--surface, #EDE6D8); padding: 10px 16px 14px; display: flex; flex-wrap: wrap; gap: 6px; }
  .details-content a { padding: 5px 10px; font-size: .78rem; background: rgba(255,255,255,.6); border: 1px solid var(--border, #D9CDBA); border-radius: 50px; text-decoration: none; color: var(--text-sec, #5C3D20); }
  .details-content a:hover { background: var(--saffron, #C96A1F); color: #fff !important; border-color: var(--saffron, #C96A1F); }
  .details-content.full-col { flex-direction: column; gap: 0; padding: 0; }
  .details-content.full-col a { background: none; border: none; border-radius: 0; padding: 9px 20px; border-bottom: 1px solid rgba(0,0,0,.05); font-size: .87rem; }
</style>"""

RICH_HTML = """<!-- Mobile Menu Overlay -->
<div class="mobile-menu-overlay" id="mobileMenuOverlay" onclick="toggleMobileMenu()"></div>
<div class="mobile-menu-drawer" id="mobileMenu">
<div class="mobile-menu-header">
<div style="display:flex;align-items:center;gap:8px;">
<div style="width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,#C96A1F,#6E1515);display:flex;align-items:center;justify-content:center;font-size:15px;color:#fff;">ॐ</div>
<span style="font-size:12px;font-weight:900;color:#6E1515;letter-spacing:.06em;">NAKSHATRA BHAJAN</span>
</div>
<button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
</div>
<div class="mobile-menu-links">
<a href="/">🏠 Bhajan Home</a>
<a href="/bhajans.html">🪔 Bhajans</a>
<a href="/bhagavad-gita.html">📖 Bhagavad Gita</a>
<a href="/shlokas.html">🕉️ Sacred Shlokas</a>
<a href="/prayers.html">🙏 Prayers &amp; Puja</a>
<a href="/upanishads.html">📚 Upanishads</a>
<a href="/wisdom.html">💬 Life Wisdom</a>
<div class="menu-divider"></div>
<div style="padding:6px 20px 3px;font-size:.62rem;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:#C96A1F;">🌐 MAIN WEBSITE</div>
<a href="https://ournakshatra.com/" style="color:#6E1515;font-weight:bold;">🏠 ournakshatra.com</a>
<a href="https://ournakshatra.com/janam_landing.html">✨ Free Kundli</a>
<a href="https://ournakshatra.com/match_landing.html">💞 Match Making</a>
<div class="menu-divider"></div>
<div style="padding:6px 20px 3px;font-size:.62rem;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:#C96A1F;">🔭 JYOTISH LIBRARY</div>
<details><summary>🪐 Navagraha</summary><div class="details-content"><a href="/planet/surya/">Surya</a><a href="/planet/chandra/">Chandra</a><a href="/planet/mangal/">Mangal</a><a href="/planet/budha/">Budha</a><a href="/planet/guru/">Guru</a><a href="/planet/shukra/">Shukra</a><a href="/planet/shani/">Shani</a><a href="/planet/rahu/">Rahu</a><a href="/planet/ketu/">Ketu</a></div></details>
<details><summary>⭐ 27 Nakshatras</summary><div class="details-content"><a href="/nakshatra/ashwini/">Ashwini</a><a href="/nakshatra/bharani/">Bharani</a><a href="/nakshatra/krittika/">Krittika</a><a href="/nakshatra/rohini/">Rohini</a><a href="/nakshatra/mrigashira/">Mrigashira</a><a href="/nakshatra/ardra/">Ardra</a><a href="/nakshatra/punarvasu/">Punarvasu</a><a href="/nakshatra/pushya/">Pushya</a><a href="/nakshatra/ashlesha/">Ashlesha</a><a href="/nakshatra/magha/">Magha</a><a href="/nakshatra/purva-phalguni/">P.Phalguni</a><a href="/nakshatra/uttara-phalguni/">U.Phalguni</a><a href="/nakshatra/hasta/">Hasta</a><a href="/nakshatra/chitra/">Chitra</a><a href="/nakshatra/swati/">Swati</a><a href="/nakshatra/vishakha/">Vishakha</a><a href="/nakshatra/anuradha/">Anuradha</a><a href="/nakshatra/jyeshtha/">Jyeshtha</a><a href="/nakshatra/mula/">Mula</a><a href="/nakshatra/purva-ashadha/">P.Ashadha</a><a href="/nakshatra/uttara-ashadha/">U.Ashadha</a><a href="/nakshatra/shravana/">Shravana</a><a href="/nakshatra/dhanishtha/">Dhanishtha</a><a href="/nakshatra/shatabhisha/">Shatabhisha</a><a href="/nakshatra/purva-bhadrapada/">P.Bhadrapada</a><a href="/nakshatra/uttara-bhadrapada/">U.Bhadrapada</a><a href="/nakshatra/revati/">Revati</a></div></details>
<details><summary>♈ 12 Rashis</summary><div class="details-content"><a href="/rashi/mesh/">Mesh</a><a href="/rashi/vrishabha/">Vrishabha</a><a href="/rashi/mithuna/">Mithuna</a><a href="/rashi/karka/">Karka</a><a href="/rashi/simha/">Simha</a><a href="/rashi/kanya/">Kanya</a><a href="/rashi/tula/">Tula</a><a href="/rashi/vrischika/">Vrischika</a><a href="/rashi/dhanu/">Dhanu</a><a href="/rashi/makara/">Makara</a><a href="/rashi/kumbha/">Kumbha</a><a href="/rashi/meena/">Meena</a></div></details>
<details><summary>🛡️ Yogas &amp; Doshas</summary><div class="details-content full-col"><a href="/remedy/">✨ View All</a><a href="/remedy/mangal-dosha/">Mangal Dosha</a><a href="/remedy/kaal-sarp-dosha/">Kaal Sarp</a><a href="/remedy/sade-sati/">Sade Sati</a><a href="/remedy/hamsa-yoga/">Hamsa Yoga</a><a href="/remedy/dhana-yoga/">Dhana Yoga</a></div></details>
<details><summary>🌙 Tithi &amp; Muhurat</summary><div class="details-content full-col"><a href="/tithi/ekadashi/">Ekadashi</a><a href="/tithi/purnima/">Purnima</a><a href="/muhurat/vivah/">Vivah Muhurat</a><a href="/muhurat/griha-pravesh/">Griha Pravesh</a></div></details>
<div class="menu-divider"></div>
<a href="/favorites.html">❤️ Saved Favorites</a>
<a href="/about.html">ℹ️ About Us</a>
<a href="/contact.html">📞 Contact</a>
</div>
</div>"""

def process_file(filepath):
    try:
        content = filepath.read_text(encoding="utf-8")
        original_content = content
        
        # Inject CSS if not present
        if '<style id="rich-mobile-menu-styles">' not in content:
            content = content.replace('</head>', f'{RICH_CSS}\n</head>')
        
        # Replace old mobile menu HTML
        # Look for something like:
        # <!-- Mobile Menu Overlay -->
        # ...
        # </div>
        # OR:
        # <div id="mobileMenuOverlay" ...>
        # ...
        # </div>
        # </div>
        # We will use regex to find the block from <div id="mobileMenuOverlay"...> up to the end of <div id="mobileMenu"...>
        
        # It's safer to just look for <div id="mobileMenuOverlay" OR <div class="mobile-menu-overlay"
        pattern = re.compile(r'<!-- Mobile Menu Overlay -->.*?<div id="mobileMenu"[^>]*>.*?</div>\s*</div>', re.DOTALL)
        if pattern.search(content):
            content = pattern.sub(RICH_HTML, content)
        else:
            pattern2 = re.compile(r'<div id="mobileMenuOverlay"[^>]*>.*?<div id="mobileMenu"[^>]*>.*?</div>\s*</div>', re.DOTALL)
            if pattern2.search(content):
                content = pattern2.sub(RICH_HTML, content)
            else:
                pattern3 = re.compile(r'<div class="mobile-menu-overlay" id="mobileMenuOverlay"[^>]*>.*?<div class="mobile-menu-drawer" id="mobileMenu"[^>]*>.*?</div>\s*</div>', re.DOTALL)
                if pattern3.search(content):
                    content = pattern3.sub(RICH_HTML, content)
                else:
                    print(f"Skipping {filepath} (mobile menu not found)")
                    return

        if content != original_content:
            filepath.write_text(content, encoding="utf-8")
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

html_files = list(ROOT.glob("*.html"))
# Also apply to programmatic files
prog_files = list(ROOT.glob("programmatic/**/*.html"))

# We might skip remedy/ since they already have it, but they might need the same exact block anyway
# Actually let's just do top level and programmatic.

for f in html_files + prog_files:
    process_file(f)
