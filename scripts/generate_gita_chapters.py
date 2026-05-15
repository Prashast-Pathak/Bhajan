import json
from pathlib import Path
import html

ROOT = Path('/Users/prashastpathak/Bhajan')
DATA = ROOT / 'data' / 'gita.json'
OUT = ROOT / 'gita'

def safe(v):
    if v is None: return ""
    return html.escape(str(v)).replace('&#x27;', "'").replace('&quot;', '"')

def generate():
    with open(DATA, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    OUT.mkdir(exist_ok=True)
    
    redirects_entries = []
    
    for ch in data.get('chapters', []):
        ch_num = ch['chapter']
        ch_dir = OUT / str(ch_num)
        ch_dir.mkdir(exist_ok=True)
        
        redirects_entries.append(f"/gita/{ch_num}/*   /gita/{ch_num}/index.html   200")
        
        ch_json = json.dumps(ch, ensure_ascii=False)
        
        verse_list_html = ""
        for v in sorted(ch.get('verses', []), key=lambda x: x['verse']):
            v_num = v['verse']
            sanskrit_first_line = v.get('sanskrit', '').split('\\n')[0].replace('\\r', '')
            english_snippet = v.get('english_translation', '')[:100] + '...'
            famous_html = '<span style="font-size:11px;color:var(--gold);">⭐ Famous</span>' if v.get('famous') else ''
            
            verse_list_html += f"""
            <a href="/gita/{ch_num}/{v_num}/" onclick="openVerseModal({v_num}); event.preventDefault();"
               class="card card-hover {'famous-verse' if v.get('famous') else ''}" style="text-decoration:none;display:block;">
              <div class="flex items-center justify-between mb-2">
                <span class="chapter-badge">Verse {v_num}</span>
                {famous_html}
              </div>
              <p class="verse-devanagari devanagari-only" style="font-size:18px;margin:0 0 6px 0;white-space:pre-line;">{sanskrit_first_line}</p>
              <p style="font-size:13px;color:var(--text-muted);margin:0 0 6px 0;">{english_snippet}</p>
            </a>
            """
            
        page_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <title>Bhagavad Gita Chapter {ch_num} - {safe(ch.get('title_english', ''))} | NAKSHATRA</title>
  
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Read all verses of Bhagavad Gita Chapter {ch_num}: {safe(ch.get('title_english', ''))}.">
  <link rel="canonical" href="https://bhajan.ournakshatra.com/gita/{ch_num}/">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Lato:wght@400;600;700;900&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  
  <style>
    :root {{
      --bg: #F5F0E8; --surface: #EDE6D8; --surface2: #E6DDD0;
      --saffron: #C96A1F; --maroon: #6E1515; --gold: #A8832A;
      --text: #2A1A08; --text-sec: #5C3D20; --text-muted: #8C6A45;
      --border: #D9CDBA; --krishna: #7C3AED; --radius: 12px;
    }}
    body.dark-mode {{ --bg: #1a1a1a; --surface: #2d2d2d; --surface2: #3d3d3d; --text: #e8e8e8; --text-sec: #b8b8b8; --text-muted: #888; --border: #444; }}
    
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background-color: var(--bg); color: var(--text); font-family: 'Lato', sans-serif; }}
    
    .devanagari {{ font-family: 'Tiro Devanagari Hindi', serif; }}
    body.fs-small  .verse-devanagari {{ font-size: 18px !important; }}
    body.fs-normal .verse-devanagari {{ font-size: 22px !important; }}
    body.fs-large  .verse-devanagari {{ font-size: 26px !important; }}
    body.fs-xlarge .verse-devanagari {{ font-size: 30px !important; }}
    
    body.script-roman    .devanagari-only  {{ display: none !important; }}
    body.script-devanagari .roman-only     {{ display: none !important; }}
    
    .verse-devanagari {{ font-family: 'Tiro Devanagari Hindi', serif; font-size: 22px; line-height: 1.8; color: var(--text); }}
    .verse-roman {{ font-size: 16px; font-style: italic; color: var(--text-sec); line-height: 1.7; }}
    
    .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; }}
    .card-hover {{ transition: border-color 0.15s, box-shadow 0.15s; }}
    .card-hover:hover {{ border-color: var(--saffron); box-shadow: 0 2px 8px rgba(201,106,31,0.12); }}
    
    .chapter-badge {{ background: rgba(168, 131, 42, 0.12); border: 1px solid rgba(168, 131, 42, 0.45); color: var(--gold); border-radius: 99px; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 3px 10px; }}
    
    .toggle-btn {{ min-width: 44px; min-height: 44px; display: inline-flex; align-items: center; justify-content: center; border-radius: 8px; border: 1px solid var(--border); background: var(--surface2); color: var(--text-sec); font-size: 13px; font-weight: 600; cursor: pointer; padding: 0 14px; transition: all 0.15s; }}
    .toggle-btn.active {{ background: var(--saffron); color: white; border-color: var(--saffron); }}
    
    .section-heading {{ font-size: 16px; font-weight: 700; color: var(--maroon); border-bottom: 2px solid var(--border); padding-bottom: 8px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
    
    .word-table th {{ background: var(--surface2); color: var(--text-sec); font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 8px 12px; text-align: left; }}
    .word-table td {{ padding: 8px 12px; border-top: 1px solid var(--border); font-size: 14px; vertical-align: top; }}
    
    .action-bar {{ position: sticky; bottom: 0; left: 0; right: 0; background: var(--bg); border-top: 1px solid var(--border); padding: 10px 16px; z-index: 3500; display:flex; gap:8px; justify-content:center; border-radius: 0 0 var(--radius) var(--radius); }}
    @media(max-width: 600px) {{ .action-bar {{ border-radius: 0; }} }}
    .action-btn {{ flex: 1; max-width: 120px; min-height: 44px; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; border: 2px solid transparent; display: flex; align-items: center; justify-content: center; gap: 5px; background:var(--surface2); color:var(--text); }}
    .btn-whatsapp {{ background: #25D366; color: white; }}
    
    .verse-nav-btn {{ min-height: 44px; min-width: 44px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--border); border-radius: 8px; background: var(--surface); color: var(--text-sec); font-size: 14px; font-weight: 600; cursor: pointer; text-decoration: none; padding: 0 16px; }}
    .verse-nav-btn.disabled {{ opacity: 0.4; pointer-events: none; }}
    
    #toast {{ position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%) translateY(20px); background: var(--text); color: white; padding: 10px 20px; border-radius: 99px; font-size: 13px; font-weight: 600; z-index: 4000; opacity: 0; transition: all 0.3s; pointer-events: none; }}
    #toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
    
    /* ===== MODAL ===== */
    .modal-backdrop {{ position: fixed; inset: 0; z-index: 3000; background: rgba(42,26,8,0.65); backdrop-filter: blur(4px); display: none; align-items: flex-start; justify-content: center; padding: 16px; overflow-y: auto; }}
    .modal-backdrop.open {{ display: flex; }}
    .modal {{ background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); width: 100%; max-width: 780px; margin: auto; animation: modalIn 0.2s ease; box-shadow: 0 20px 60px rgba(0,0,0,0.25); position: relative; }}
    @keyframes modalIn {{ from {{ opacity: 0; transform: translateY(20px) scale(0.97); }} to {{ opacity: 1; transform: none; }} }}
    .modal-header {{ display: flex; align-items: flex-start; justify-content: flex-start; gap: 12px; padding: 24px 24px 16px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: var(--bg); z-index: 10; border-radius: var(--radius) var(--radius) 0 0; }}
    .modal-title-en {{ font-size: 22px; font-weight: 700; color: var(--maroon); line-height:1.2; }}
    .modal-title-hi {{ font-family: 'Tiro Devanagari Hindi', serif; font-size: 17px; color: var(--text-sec); margin-top: 2px; }}
    .modal-close {{ background: transparent; border: none; flex-shrink: 0; cursor: pointer; color: var(--text); display: flex; align-items: center; justify-content: center; transition: background 0.2s; padding: 8px; border-radius: 8px; margin-left: -8px; margin-top: 0px; width: auto; height: auto; }}
    .modal-close:hover {{ background: var(--surface2); color: var(--saffron); }}
    .modal-body {{ padding: 20px 24px; display: flex; flex-direction: column; gap: 20px; }}
    
    @media(max-width: 600px) {{
      .modal-backdrop {{ padding: 0; }}
      .modal {{ border-radius: 0; min-height: 100vh; display: flex; flex-direction: column; }}
      .modal-header {{ border-radius: 0; }}
      .action-bar {{ position: sticky; bottom: 0; }}
    }}
  </style>

  <style id="premium-header-styles">
    /* ── HEADER ── */
    .main-header {{
      position: sticky; top: 0; z-index: 1000;
      background: rgba(245,240,232,0.92) !important;
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border-bottom: 1px solid rgba(0,0,0,0.07);
      box-shadow: 0 2px 16px rgba(0,0,0,0.04);
      padding: 0 20px;
    }}
    body.dark-mode .main-header {{
      background: rgba(22,22,22,0.92) !important;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }}
    .main-header .header-inner {{
      max-width: 1200px; margin: 0 auto;
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      gap: 16px;
      height: 64px;
    }}
    .logo-link {{ display: flex; align-items: center; gap: 10px; text-decoration: none; flex-shrink: 0; }}
    .logo-om {{
      width: 40px; height: 40px; border-radius: 50%;
      background: linear-gradient(135deg, var(--saffron), var(--maroon));
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-hindi); font-size: 20px; color: #fff;
      flex-shrink: 0;
    }}
    .logo-text {{ display: flex; flex-direction: column; }}
    .logo-title {{ font-family: var(--font-hindi); font-size: 17px; font-weight: 700; color: var(--maroon); line-height: 1.2; }}
    .logo-sub {{ font-size: 10px; color: var(--text-muted); letter-spacing: 0.3px; }}
    .desktop-nav {{ display: flex; gap: 2px; align-items: center; justify-content: center; }}
    .desktop-nav a {{
      text-decoration: none; color: var(--text-sec); font-size: 13px; font-weight: 600;
      padding: 7px 11px; border-radius: 8px; transition: all 0.18s; white-space: nowrap;
    }}
    .desktop-nav a:hover {{ background: var(--surface); color: var(--saffron); }}
    .header-icons {{ display: flex; align-items: center; gap: 4px; flex-shrink: 0; }}
    .header-icon-btn {{
      background: transparent; border: 1px solid transparent; cursor: pointer;
      font-size: 17px; width: 38px; height: 38px; border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      color: var(--maroon); transition: all 0.18s; flex-shrink: 0;
    }}
    .header-icon-btn:hover {{ background: var(--surface); border-color: var(--border); }}
    .hamburger-btn, .back-btn {{
      background: transparent; border: none; color: var(--text);
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      padding: 8px; border-radius: 8px; transition: 0.2s; flex-shrink: 0;
    }}
    .hamburger-btn {{ display: none; }}
    .hamburger-btn:hover, .back-btn:hover {{ background: var(--surface2); }}
    .mobile-menu-overlay {{
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.5); backdrop-filter: blur(4px);
      z-index: 1999; opacity: 0; pointer-events: none; transition: 0.3s ease;
    }}
    .mobile-menu-overlay.active {{ opacity: 1; pointer-events: auto; }}
    .mobile-menu-drawer {{
      position: fixed; top: 0; left: -300px; bottom: 0; width: 280px;
      background: var(--bg); z-index: 2000; box-shadow: 4px 0 24px rgba(0,0,0,0.12);
      transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex; flex-direction: column;
    }}
    .mobile-menu-drawer.active {{ left: 0; }}
    .mobile-menu-header {{
      display: flex; align-items: center; justify-content: space-between;
      padding: 20px 24px; border-bottom: 1px solid var(--border);
    }}
    .close-menu-btn {{ background: none; border: none; font-size: 24px; color: var(--text-muted); cursor: pointer; }}
    .mobile-menu-links {{ padding: 20px; display: flex; flex-direction: column; gap: 6px; overflow-y: auto; }}
    .mobile-menu-links a {{
      text-decoration: none; color: var(--text); font-size: 15px; font-weight: 600;
      padding: 11px 14px; border-radius: 8px; transition: 0.18s;
    }}
    .mobile-menu-links a:hover {{ background: var(--surface); color: var(--saffron); }}
    .menu-divider {{ height: 1px; background: var(--border); margin: 8px 0; }}
    @media (max-width: 960px) {{
      .desktop-nav {{ display: none !important; }}
      .hamburger-btn {{ display: flex !important; }}
      .logo-text {{ display: none; }}
      .main-header .header-inner {{ grid-template-columns: auto auto; }}
    }}
  </style>

  <style id="rich-mobile-menu-styles">
    .mobile-menu-links details {{ border-bottom: 1px solid var(--border, #D9CDBA); }}
    .mobile-menu-links details summary {{ padding: 10px 20px; color: var(--text-sec, #5C3D20); font-size: 13px; font-weight: 700; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; }}
    .mobile-menu-links details summary::-webkit-details-marker {{ display: none; }}
    .mobile-menu-links details summary::after {{ content: '+'; font-size: 1.1rem; color: var(--saffron, #C96A1F); }}
    .mobile-menu-links details[open] summary::after {{ content: '−'; }}
    .mobile-menu-links details[open] summary {{ background: var(--surface2, #E6DDD0); color: var(--saffron, #C96A1F); }}
    .details-content {{ background: var(--surface, #EDE6D8); padding: 10px 16px 14px; display: flex; flex-wrap: wrap; gap: 6px; }}
    .details-content a {{ padding: 5px 10px; font-size: .78rem; background: rgba(255,255,255,.6); border: 1px solid var(--border, #D9CDBA); border-radius: 50px; text-decoration: none; color: var(--text-sec, #5C3D20); }}
    .details-content a:hover {{ background: var(--saffron, #C96A1F); color: #fff !important; border-color: var(--saffron, #C96A1F); }}
  </style>
</head>
<body class="fs-normal script-both">

  <header class="main-header">
    <div class="header-inner">
      <div style="display:flex; align-items:center; gap:4px;">
        <script>
          function handleMainHeaderBack() {{
            window.location.href = '/bhagavad-gita.html';
          }}
        </script>
        <button class="back-btn" onclick="handleMainHeaderBack()" aria-label="Go Back" title="Go Back">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        </button>
        <button class="hamburger-btn" onclick="toggleMobileMenu()" aria-label="Open Menu">
          <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="2.5" fill="none"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
        </button>
        <a href="/index.html" class="logo-link">
          <div class="logo-om">ॐ</div>
          <div class="logo-text">
            <span class="logo-title">सनातन ज्ञान सागर</span>
            <span class="logo-sub">The Ocean of Eternal Wisdom</span>
          </div>
        </a>
      </div>

      <nav class="desktop-nav" aria-label="Main navigation">
        <a href="/index.html">Home</a>
        <a href="/bhajans.html">Bhajans</a>
        <a href="/bhagavad-gita.html" class="active">Gita</a>
        <a href="/shlokas.html">Shlokas</a>
        <a href="/prayers.html">Prayers</a>
        <a href="/upanishads.html">Upanishads</a>
        <a href="/wisdom.html">Wisdom</a>
      </nav>

      <div class="header-icons">
        <button class="header-icon-btn" onclick="document.body.classList.toggle('dark-mode')" aria-label="Dark mode" title="Dark mode">🌙</button>
      </div>
    </div>
  </header>

  <div class="mobile-menu-overlay" id="mobileMenuOverlay" onclick="toggleMobileMenu()"></div>
  <div class="mobile-menu-drawer" id="mobileMenu">
    <div class="mobile-menu-header">
      <div style="display:flex;align-items:center;gap:8px;">
        <div style="width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,#C96A1F,#6E1515);display:flex;align-items:center;justify-content:center;font-size:15px;color:#fff;">ॐ</div>
        <span style="font-size:12px;font-weight:900;color:#6E1515;letter-spacing:.06em;">NAKSHATRA</span>
      </div>
      <button class="close-menu-btn" onclick="toggleMobileMenu()">✕</button>
    </div>
    <div class="mobile-menu-links">
      <a href="/">🏠 Home</a>
      <a href="/bhajans.html">🪔 Bhajans</a>
      <a href="/bhagavad-gita.html">📖 Gita</a>
      <a href="/shlokas.html">🕉️ Shlokas</a>
      <a href="/prayers.html">🙏 Prayers</a>
      <a href="/upanishads.html">📚 Upanishads</a>
      <a href="/wisdom.html">💬 Wisdom</a>
    </div>
  </div>

  <script>
    function toggleMobileMenu() {{
      const menu = document.getElementById('mobileMenu');
      const overlay = document.getElementById('mobileMenuOverlay');
      menu.classList.toggle('active');
      overlay.classList.toggle('active');
    }}
  </script>

  <!-- THE CHAPTER PAGE -->
  <main id="chapter-view" class="max-w-5xl mx-auto px-4 py-6 pb-24">
    <nav class="text-sm mb-5" style="color:var(--text-muted); font-size:13px; font-weight:600;">
      <a href="/bhagavad-gita.html" style="color:var(--saffron); text-decoration:none;">← Back to Gita Hub</a>
    </nav>
    
    <div class="card mb-5" style="border-left:4px solid var(--krishna);">
      <h1 class="devanagari" style="font-size:28px;font-weight:700;color:var(--maroon);margin:0 0 4px 0;">{safe(ch.get('title_sanskrit', ''))}</h1>
      <p style="font-size:18px;color:var(--text-sec);margin:0 0 16px 0;">{safe(ch.get('title_english', ''))}</p>
      <h2 style="font-size:14px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:8px;">सारांश / Summary</h2>
      <p class="devanagari" style="font-size:17px;line-height:1.9;color:var(--text-sec);margin-bottom:12px;">{safe(ch.get('summary_hindi', ''))}</p>
      <p style="font-size:15px;line-height:1.8;color:var(--text-muted);">{safe(ch.get('summary_english', ''))}</p>
    </div>
    
    <div class="mb-3" style="color:var(--text-muted);font-size:14px;text-align:center;">
      Click any verse to read full translation and meaning
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      {verse_list_html}
    </div>
  </main>
  
  <footer style="background:var(--surface); border-top:1px solid var(--border); padding:32px 16px; text-align:center;">
    <div style="max-width:1100px; margin:0 auto;">
      <div style="font-family:var(--font-hindi); font-size:32px; color:var(--saffron); margin-bottom:8px;">ॐ</div>
      <p style="font-family:var(--font-hindi); font-size:15px; color:var(--text-sec); margin-bottom:16px;">सनातन ज्ञान सागर — The Ocean of Eternal Wisdom</p>
      <div style="font-size:12px; color:var(--text-muted);">© 2026 NAKSHATRA. All rights reserved.</div>
    </div>
  </footer>

  <!-- THE POP-UP MODAL -->
  <div class="modal-backdrop" id="modalBackdrop" role="dialog" aria-modal="true">
    <div class="modal" id="modalBox">
      <div class="modal-header">
        <button class="modal-close" onclick="closeVerseModal()" aria-label="Go Back">
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        </button>
        <div>
          <div class="modal-title-en" id="modalTitleEn">Bhagavad Gita Chapter {ch_num}</div>
          <div class="modal-title-hi" id="modalTitleHi">{safe(ch.get('title_sanskrit', ''))}</div>
        </div>
      </div>
      
      <div class="modal-body" id="modal-content"></div>
      
      <div class="action-bar" id="action-bar" style="display:none;">
        <button class="action-btn btn-whatsapp" onclick="shareWhatsApp()">📱 Share</button>
        <button class="action-btn" onclick="copyVerse()">📋 Copy</button>
      </div>
    </div>
  </div>

  <div id="toast"></div>

  <script>
    const CHAPTER_DATA = {ch_json};
    let currentVerse = null;
    
    let scriptPref = localStorage.getItem('sgs_script') || 'both';
    let fontPref = localStorage.getItem('sgs_font') || 'normal';
    applyPrefs();
    
    function applyPrefs() {{
      document.body.className = document.body.className.replace(/fs-\w+/, '').trim();
      document.body.classList.add('fs-' + fontPref);
      document.body.classList.remove('script-devanagari', 'script-roman', 'script-both');
      document.body.classList.add('script-' + scriptPref);
    }}
    
    function setScript(pref) {{
      scriptPref = pref;
      localStorage.setItem('sgs_script', pref);
      applyPrefs();
      document.querySelectorAll('.script-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.querySelector(`.script-btn[data-val="${{pref}}"]`);
      if(activeBtn) activeBtn.classList.add('active');
    }}
    
    function setFont(pref) {{
      fontPref = pref;
      localStorage.setItem('sgs_font', pref);
      applyPrefs();
      document.querySelectorAll('.font-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.querySelector(`.font-btn[data-val="${{pref}}"]`);
      if(activeBtn) activeBtn.classList.add('active');
    }}

    function openVerseModal(verseNum) {{
      const v = CHAPTER_DATA.verses.find(x => x.verse == verseNum);
      if(!v) return;
      currentVerse = v;
      
      const sorted = [...CHAPTER_DATA.verses].sort((a,b)=>a.verse-b.verse);
      const idx = sorted.findIndex(x => x.verse == verseNum);
      const prevV = idx > 0 ? sorted[idx-1] : null;
      const nextV = idx < sorted.length-1 ? sorted[idx+1] : null;
      
      const wordRows = (v.word_meanings || []).map(w => `
        <tr>
          <td class="devanagari" style="font-size:18px;font-weight:600;color:var(--krishna);">${{w.word}}</td>
          <td class="devanagari" style="color:var(--text-sec);font-size:16px;">${{w.meaning_hindi || ''}}</td>
          <td style="color:var(--text-muted);font-style:italic;">${{w.meaning_english || ''}}</td>
        </tr>`).join('');
        
      const html = `
        <div class="flex items-center justify-between mb-5">
          <button onclick="${{prevV ? `openVerseModal(${{prevV.verse}})` : 'return false'}}" class="verse-nav-btn ${{!prevV ? 'disabled' : ''}}">← Prev</button>
          <span style="color:var(--text-muted);font-size:13px;font-weight:700;">Verse ${{v.verse}} of ${{sorted.length}}</span>
          <button onclick="${{nextV ? `openVerseModal(${{nextV.verse}})` : 'return false'}}" class="verse-nav-btn ${{!nextV ? 'disabled' : ''}}">Next →</button>
        </div>
        
        <div class="flex flex-wrap gap-2 mb-5">
          <div class="flex gap-1">
            <button class="toggle-btn script-btn ${{scriptPref==='both'?'active':''}}" data-val="both" onclick="setScript('both')">हिंदी+Roman</button>
            <button class="toggle-btn script-btn ${{scriptPref==='devanagari'?'active':''}}" data-val="devanagari" onclick="setScript('devanagari')">हिंदी</button>
            <button class="toggle-btn script-btn ${{scriptPref==='roman'?'active':''}}" data-val="roman" onclick="setScript('roman')">Roman</button>
          </div>
          <div class="flex gap-1">
            <button class="toggle-btn font-btn ${{fontPref==='small'?'active':''}}" data-val="small" onclick="setFont('small')">A-</button>
            <button class="toggle-btn font-btn ${{fontPref==='normal'?'active':''}}" data-val="normal" onclick="setFont('normal')">A</button>
            <button class="toggle-btn font-btn ${{fontPref==='large'?'active':''}}" data-val="large" onclick="setFont('large')">A+</button>
          </div>
        </div>

        <div class="card mb-5" style="border-left:4px solid var(--krishna);">
          <div class="section-heading">🕉️ Sanskrit Original — संस्कृत</div>
          <p class="verse-devanagari devanagari-only mb-3" style="white-space:pre-line;">${{v.sanskrit.replace(/\\n/g, '<br>')}}</p>
          <p class="verse-roman roman-only" style="white-space:pre-line;">${{(v.roman||'').replace(/\\n/g, '<br>')}}</p>
        </div>
        
        ${{wordRows ? `
        <div class="card mb-5">
          <div class="section-heading">📚 Word by Word — शब्द-अर्थ</div>
          <div style="overflow-x:auto;">
            <table class="word-table w-full" style="border-collapse:collapse;">
              <thead><tr><th>Sanskrit</th><th>Hindi</th><th>English</th></tr></thead>
              <tbody>${{wordRows}}</tbody>
            </table>
          </div>
        </div>` : ''}}
        
        <div class="card mb-5">
          <div class="section-heading">🇮🇳 Hindi Translation</div>
          <p class="devanagari" style="font-size:18px;line-height:1.9;">${{v.hindi_translation}}</p>
        </div>
        
        <div class="card mb-5" style="border-left:3px solid var(--gold);">
          <div class="section-heading">🌐 English Translation</div>
          <p style="font-size:17px;line-height:1.8;font-style:italic;">"${{v.english_translation}}"</p>
        </div>
        
        ${{v.hindi_commentary ? `
        <div class="card mb-5">
          <div class="section-heading">📖 Hindi Commentary</div>
          <p class="devanagari" style="font-size:17px;line-height:1.9;">${{v.hindi_commentary}}</p>
        </div>` : ''}}
        
        ${{v.english_commentary ? `
        <div class="card mb-5">
          <div class="section-heading">📝 English Commentary</div>
          <p style="font-size:16px;line-height:1.85;">${{v.english_commentary}}</p>
        </div>` : ''}}
      `;
      
      document.getElementById('modal-content').innerHTML = html;
      document.getElementById('modalBackdrop').classList.add('open');
      document.getElementById('action-bar').style.display = 'flex';
      document.body.style.overflow = 'hidden';
      
      history.pushState(null, null, '/gita/' + CHAPTER_DATA.chapter + '/' + verseNum + '/');
      document.title = `Bhagavad Gita Chapter ${{CHAPTER_DATA.chapter}} Verse ${{verseNum}}`;
      document.getElementById('modalBackdrop').scrollTo(0, 0);
    }}
    
    function closeVerseModal() {{
      document.getElementById('modalBackdrop').classList.remove('open');
      document.getElementById('action-bar').style.display = 'none';
      document.body.style.overflow = '';
      history.pushState(null, null, '/gita/' + CHAPTER_DATA.chapter + '/');
      document.title = `Bhagavad Gita Chapter ${{CHAPTER_DATA.chapter}} | NAKSHATRA`;
    }}
    
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.textContent = msg; t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2500);
    }}
    
    function copyVerse() {{
      if(!currentVerse) return;
      const v = currentVerse;
      const url = window.location.origin + window.location.pathname;
      const text = `Bhagavad Gita Chapter ${{CHAPTER_DATA.chapter}}, Verse ${{v.verse}}\\n\\n${{v.hindi_translation}}\\n\\n${{url}}`;
      navigator.clipboard.writeText(text).then(() => showToast('📋 Copied to clipboard!'));
    }}
    
    function shareWhatsApp() {{
      if(!currentVerse) return;
      const v = currentVerse;
      const url = window.location.origin + window.location.pathname;
      const msg = `🙏 *Bhagavad Gita — Chapter ${{CHAPTER_DATA.chapter}}, Verse ${{v.verse}}*\\n\\n${{v.sanskrit}}\\n\\n*अर्थ:* ${{v.hindi_translation}}\\n\\n👇\\n${{url}}`;
      window.open('https://wa.me/?text=' + encodeURIComponent(msg), '_blank');
    }}
    
    window.addEventListener('load', () => {{
      const pathParts = window.location.pathname.split('/').filter(p => p);
      if (pathParts.length >= 3 && pathParts[0] === 'gita') {{
        const vNum = parseInt(pathParts[2]);
        if (vNum) openVerseModal(vNum);
      }}
    }});
    
    window.addEventListener('popstate', () => {{
      const pathParts = window.location.pathname.split('/').filter(p => p);
      if (pathParts.length < 3) {{
        document.getElementById('modalBackdrop').classList.remove('open');
        document.getElementById('action-bar').style.display = 'none';
        document.body.style.overflow = '';
      }} else {{
        const vNum = parseInt(pathParts[2]);
        if (vNum) openVerseModal(vNum);
      }}
    }});
  </script>
</body>
</html>"""
        with open(ch_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(page_html)
            
    # Update _redirects
    redirects_path = ROOT / '_redirects'
    existing_redirects = ""
    if redirects_path.exists():
        with open(redirects_path, 'r', encoding='utf-8') as f:
            existing_redirects = f.read()
            
    new_redirects = []
    for line in existing_redirects.split('\n'):
        if not line.startswith('/gita/'):
            new_redirects.append(line)
            
    new_redirects.append("\n# Gita SPA Routes for 18 Master Pages")
    new_redirects.extend(redirects_entries)
    
    with open(redirects_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_redirects))
            
    print("Generated 18 Master Chapter pages with Same-URL Cloudflare configuration!")

if __name__ == "__main__":
    generate()
