import os
import re

HEADER_CSS = """
    /* HEADER */
    .main-header { position: sticky; top: 0; z-index: 100; background: rgba(245,240,232,0.92); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); padding: 0 16px; }
    .main-header .header-inner { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; height: 60px; gap: 12px; }
    .hamburger-btn { display: none; background: none; border: none; cursor: pointer; color: var(--maroon); align-items: center; justify-content: center; padding: 4px; }
    .logo-link { text-decoration: none; display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
    .logo-om { width: 36px; height: 36px; background: linear-gradient(135deg, var(--saffron), var(--maroon)); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 18px; font-family: var(--font-hindi); }
    .logo-text { display: flex; flex-direction: column; line-height: 1.1; }
    .logo-title { font-family: var(--font-hindi); font-size: 16px; color: var(--maroon); font-weight: 600; }
    .logo-sub { font-size: 9px; color: var(--text-muted); letter-spacing: 0.2px; }
    .desktop-nav { display: flex; gap: 4px; align-items: center; justify-content: center; }
    .desktop-nav a { text-decoration: none; color: var(--text-sec); font-size: 13px; padding: 6px 12px; border-radius: 8px; font-weight: 500; transition: all 0.2s; white-space: nowrap; }
    .desktop-nav a:hover, .desktop-nav a.active { background: var(--surface); color: var(--saffron); }
    .header-icons { display: flex; gap: 4px; align-items: center; justify-content: flex-end; }
    .header-icon-btn { background: none; border: none; cursor: pointer; font-size: 18px; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; transition: 0.2s; color: var(--text-sec); }
    .header-icon-btn:hover { background: var(--surface); color: var(--maroon); }
    .chanting-btn { background: rgba(201,106,31,0.1); color: var(--saffron); border: 1px solid rgba(201,106,31,0.2); font-size: 12px; font-weight: 600; border-radius: 20px; padding: 4px 12px; height: 32px; display: flex; align-items: center; gap: 4px; cursor: pointer; transition: all 0.2s; }
    .chanting-btn:hover { background: var(--saffron); color: #fff; }

    /* MOBILE MENU DRAWER */
    .mobile-menu-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 999; opacity: 0; pointer-events: none; transition: opacity 0.3s; }
    .mobile-menu-overlay.active { opacity: 1; pointer-events: auto; }
    .mobile-menu-drawer { position: fixed; top: 0; left: -280px; width: 280px; height: 100vh; background: var(--bg); z-index: 1000; box-shadow: 4px 0 24px rgba(0,0,0,0.1); transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1); display: flex; flex-direction: column; overflow: hidden; }
    .mobile-menu-drawer.active { left: 0; }
    .mobile-menu-header { display: flex; align-items: center; justify-content: space-between; padding: 16px 20px; border-bottom: 1px solid var(--border); }
    .close-menu-btn { background: none; border: none; font-size: 24px; color: var(--text-muted); cursor: pointer; }
    .mobile-menu-links { padding: 20px; display: flex; flex-direction: column; gap: 6px; overflow-y: auto; }
    .mobile-menu-links a { text-decoration: none; color: var(--text); font-size: 15px; font-weight: 600; padding: 11px 14px; border-radius: 8px; transition: 0.18s; }
    .mobile-menu-links a:hover { background: var(--surface); color: var(--saffron); }
    .menu-divider { height: 1px; background: var(--border); margin: 8px 0; }

    @media (max-width: 960px) {
      .desktop-nav { display: none !important; }
      .hamburger-btn { display: flex !important; }
      .logo-text { display: none; }
      .main-header .header-inner { grid-template-columns: auto auto; }
      .chanting-btn { display: none !important; }
    }
"""

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
// ── UI TOGGLES (consolidated) ──
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

    // Font Size Toggle (optional)
    const fontBtn = document.getElementById('fontToggle');
    if (fontBtn) {
      fontBtn.addEventListener('click', () => {
        fontSize += 2;
        if (fontSize > 36) fontSize = 18;
        document.documentElement.style.setProperty('--font-size-hindi', fontSize + 'px');
        document.documentElement.style.setProperty('--hindi-size', fontSize + 'px');
        localStorage.setItem('sgs_fontsize', fontSize);
      });
    }

    // Chanting Toggle (optional)
    const chantBtn = document.getElementById('chantingToggle');
    if (chantBtn) {
      function updateChantBtn() {
        const on = document.body.classList.contains('chanting-mode');
        chantBtn.innerHTML = on ? '📖 Study' : '🎵 Chant';
        chantBtn.title = on ? 'Switch to Study Mode' : 'Switch to Chanting Mode';
      }
      updateChantBtn();
      chantBtn.addEventListener('click', () => {
        document.body.classList.toggle('chanting-mode');
        localStorage.setItem('sgs_chanting_mode', document.body.classList.contains('chanting-mode'));
        updateChantBtn();
      });
    }
  });
})();
</script>"""

# HTML files to process
import glob

files = glob.glob("*.html")

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # 1. Replace CSS
    # Remove existing HEADER to MOBILE MENU or media max-width 960px block if exists
    # To be safe, we might just look for where to inject CSS.
    # Actually, we can remove `<style>` blocks that contain `/* HEADER */` down to `</style>`? No, that would remove other CSS.
    
    # Let's write a targeted regex replacement
