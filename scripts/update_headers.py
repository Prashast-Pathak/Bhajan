import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADER_HTML = """<header class="main-header">
  <div class="header-inner">
    <!-- Left: Logo + Hamburger -->
    <div style="display:flex; align-items:center; gap:10px;">
      <button class="hamburger-btn" onclick="toggleMobileMenu()" aria-label="Open Menu">
        <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.5" fill="none"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
      <a href="index.html" class="logo-link">
        <div class="logo-om">ॐ</div>
        <div class="logo-text">
          <span class="logo-title">सनातन ज्ञान सागर</span>
          <span class="logo-sub">The Ocean of Eternal Wisdom</span>
        </div>
      </a>
    </div>

    <!-- Center: Desktop Nav -->
    <nav class="desktop-nav" aria-label="Main navigation">
      <a href="index.html">Home</a>
      <a href="bhajans.html">Bhajans</a>
      <a href="bhagavad-gita.html">Gita</a>
      <a href="shlokas.html">Shlokas</a>
      <a href="prayers.html">Prayers</a>
      <a href="upanishads.html">Upanishads</a>
      <a href="wisdom.html">Wisdom</a>
    </nav>

    <!-- Right: Icons -->
    <div class="header-icons">
      <button class="header-icon-btn" id="darkToggle" aria-label="Dark mode" title="Dark mode">🌙</button>
      <button class="header-icon-btn" id="headerFavBtn" onclick="window.location.href='favorites.html'" title="Saved" aria-label="Saved">❤️</button>
    </div>
  </div>
</header>

<!-- Mobile Menu Overlay -->
<div id="mobileMenuOverlay" class="mobile-menu-overlay" onclick="toggleMobileMenu()"></div>
<div id="mobileMenu" class="mobile-menu-drawer">
  <div class="mobile-menu-header">
    <div class="logo-om" style="width:36px;height:36px;font-size:18px;">ॐ</div>
    <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
  </div>
  <div class="mobile-menu-links">
    <a href="index.html">🏠 Home</a>
    <a href="bhajans.html">🪔 Bhajans</a>
    <a href="bhagavad-gita.html">📖 Bhagavad Gita</a>
    <a href="shlokas.html">🕉️ Sacred Shlokas</a>
    <a href="prayers.html">🙏 Prayers &amp; Puja</a>
    <a href="upanishads.html">📚 Upanishads</a>
    <a href="wisdom.html">💬 Life Wisdom</a>
    <div class="menu-divider"></div>
    <a href="favorites.html">❤️ Saved Favorites</a>
    <a href="about.html">ℹ️ About Us</a>
    <a href="contact.html">📞 Contact</a>
  </div>
</div>

<script>
function toggleMobileMenu() {
  const menu = document.getElementById('mobileMenu');
  const overlay = document.getElementById('mobileMenuOverlay');
  if(menu.classList.contains('active')) {
    menu.classList.remove('active');
    overlay.classList.remove('active');
  } else {
    menu.classList.add('active');
    overlay.classList.add('active');
  }
}
</script>

<script>
// ── GLOBAL UI TOGGLES ──
(function() {
  // Apply initial states immediately to prevent flash
  const isDark = localStorage.getItem('sgs_dark') === 'true';
  if (isDark) document.body.classList.add('dark-mode');
  
  const isChanting = localStorage.getItem('sgs_chanting_mode') === 'true';
  if (isChanting) document.body.classList.add('chanting-mode');

  let fontSize = parseInt(localStorage.getItem('sgs_fontsize') || '22');
  document.documentElement.style.setProperty('--font-size-hindi', fontSize + 'px');
  document.documentElement.style.setProperty('--hindi-size', fontSize + 'px');

  document.addEventListener('DOMContentLoaded', () => {
    // Dark Mode Toggle
    const darkBtn = document.getElementById('darkToggle');
    if (darkBtn) {
      darkBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('sgs_dark', document.body.classList.contains('dark-mode'));
      });
    }
  });
})();
</script>"""

STYLE_HTML = """<style id="premium-header-styles">
  /* ── HEADER ── */
  .main-header {
    position: sticky; top: 0; z-index: 1000;
    background: rgba(245,240,232,0.92) !important;
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border-bottom: 1px solid rgba(0,0,0,0.07);
    box-shadow: 0 2px 16px rgba(0,0,0,0.04);
    padding: 0 20px;
  }
  body.dark-mode .main-header {
    background: rgba(22,22,22,0.92) !important;
    border-bottom: 1px solid rgba(255,255,255,0.06);
  }
  .main-header .header-inner {
    max-width: 1200px; margin: 0 auto;
    display: grid;
    grid-template-columns: auto 1fr auto;
    align-items: center;
    gap: 16px;
    height: 64px;
  }

  /* Logo */
  .logo-link { display: flex; align-items: center; gap: 10px; text-decoration: none; flex-shrink: 0; }
  .logo-om {
    width: 40px; height: 40px; border-radius: 50%;
    background: linear-gradient(135deg, var(--saffron), var(--maroon));
    display: flex; align-items: center; justify-content: center;
    font-family: var(--font-hindi); font-size: 20px; color: #fff;
    flex-shrink: 0;
  }
  .logo-text { display: flex; flex-direction: column; }
  .logo-title { font-family: var(--font-hindi); font-size: 17px; font-weight: 700; color: var(--maroon); line-height: 1.2; }
  .logo-sub { font-size: 10px; color: var(--text-muted); letter-spacing: 0.3px; }

  /* Desktop Nav — center column */
  .desktop-nav {
    display: flex; gap: 2px; align-items: center; justify-content: center;
  }
  .desktop-nav a {
    text-decoration: none; color: var(--text-sec); font-size: 13px; font-weight: 600;
    padding: 7px 11px; border-radius: 8px; transition: all 0.18s;
    white-space: nowrap;
  }
  .desktop-nav a:hover { background: var(--surface); color: var(--saffron); }
  .desktop-nav a.active { background: var(--surface2); color: var(--saffron); }

  /* Icons — right column */
  .header-icons { display: flex; align-items: center; gap: 4px; flex-shrink: 0; }
  .header-icon-btn {
    background: transparent; border: 1px solid transparent; cursor: pointer;
    font-size: 17px; width: 38px; height: 38px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    color: var(--maroon); transition: all 0.18s; flex-shrink: 0;
  }
  .header-icon-btn:hover { background: var(--surface); border-color: var(--border); }

  /* Hamburger */
  .hamburger-btn {
    background: transparent; border: none; color: var(--text);
    cursor: pointer; display: none; align-items: center; justify-content: center;
    padding: 8px; border-radius: 8px; transition: 0.2s; flex-shrink: 0;
  }
  .hamburger-btn:hover { background: var(--surface2); }

  /* Mobile Menu */
  .mobile-menu-overlay {
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5); backdrop-filter: blur(4px);
    z-index: 1999; opacity: 0; pointer-events: none; transition: 0.3s ease;
  }
  .mobile-menu-overlay.active { opacity: 1; pointer-events: auto; }
  .mobile-menu-drawer {
    position: fixed; top: 0; left: -300px; bottom: 0; width: 280px;
    background: var(--bg); z-index: 2000; box-shadow: 4px 0 24px rgba(0,0,0,0.12);
    transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex; flex-direction: column;
  }
  .mobile-menu-drawer.active { left: 0; }
  .mobile-menu-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 20px 24px; border-bottom: 1px solid var(--border);
  }
  .close-menu-btn { background: none; border: none; font-size: 24px; color: var(--text-muted); cursor: pointer; }
  .mobile-menu-links { padding: 20px; display: flex; flex-direction: column; gap: 6px; overflow-y: auto; }
  .mobile-menu-links a {
    text-decoration: none; color: var(--text); font-size: 15px; font-weight: 600;
    padding: 11px 14px; border-radius: 8px; transition: 0.18s;
  }
  .mobile-menu-links a:hover { background: var(--surface); color: var(--saffron); }
  .menu-divider { height: 1px; background: var(--border); margin: 8px 0; }

  /* Chanting mode — hide all meaning blocks */
  body.chanting-mode .meaning-section,
  body.chanting-mode .line-meaning-hindi,
  body.chanting-mode .line-meaning-en,
  body.chanting-mode .line-meaning-label { display: none !important; }

  @media (max-width: 960px) {
    .desktop-nav { display: none !important; }
    .hamburger-btn { display: flex !important; }
    .logo-text { display: none; }
    .main-header .header-inner { grid-template-columns: auto auto; }
    .chanting-btn { display: none !important; }
  }
</style>
</head>"""


for file in ROOT.glob("*.html"):
    content = file.read_text(encoding="utf-8")

    # 1. Replace old style block (whether it exists or not, always update it)
    if '<style id="premium-header-styles">' in content:
        content = re.sub(
            r'<style id="premium-header-styles">.*?</style>\s*</head>',
            STYLE_HTML,
            content,
            flags=re.DOTALL
        )
    else:
        content = content.replace("</head>", STYLE_HTML)

    # 2. Replace old <header> block (whether old or new style)
    if '<header class="main-header">' in content:
        content = re.sub(
            r'<header class="main-header">.*?</script>',
            HEADER_HTML,
            content,
            flags=re.DOTALL
        )
    else:
        content = re.sub(r'<header>.*?</header>', HEADER_HTML, content, flags=re.DOTALL)

    file.write_text(content, encoding="utf-8")
    print(f"Updated {file.name}")
