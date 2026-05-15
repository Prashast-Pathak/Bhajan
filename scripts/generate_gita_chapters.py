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
        # The URL structure is /gita/1/, /gita/2/, etc.
        ch_dir = OUT / str(ch_num)
        ch_dir.mkdir(exist_ok=True)
        
        # Add 200 rewrite rule for Cloudflare so /gita/4/2/ serves /gita/4/index.html
        redirects_entries.append(f"/gita/{ch_num}/*   /gita/{ch_num}/index.html   200")
        
        ch_json = json.dumps(ch, ensure_ascii=False)
        
        verse_list_html = ""
        for v in sorted(ch.get('verses', []), key=lambda x: x['verse']):
            v_num = v['verse']
            sanskrit_first_line = v.get('sanskrit', '').split('\n')[0].replace('\r', '')
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
      --border: #D9CDBA; --krishna: #7C3AED;
    }}
    body.dark-mode {{ --bg: #1a1a1a; --surface: #2d2d2d; --surface2: #3d3d3d; --text: #e8e8e8; --text-sec: #b8b8b8; --text-muted: #888; --border: #444; }}
    
    * {{ box-sizing: border-box; }}
    body {{ background-color: var(--bg); color: var(--text); font-family: 'Lato', sans-serif; margin: 0; padding: 0; }}
    
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
    
    .gita-badge {{ display: inline-flex; align-items: center; gap: 5px; background: rgba(124, 58, 237, 0.10); border: 1px solid rgba(124, 58, 237, 0.4); color: #5b21b6; border-radius: 99px; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 3px 10px; }}
    .chapter-badge {{ background: rgba(168, 131, 42, 0.12); border: 1px solid rgba(168, 131, 42, 0.45); color: var(--gold); border-radius: 99px; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 3px 10px; }}
    .topic-chip {{ display: inline-block; background: rgba(201, 106, 31, 0.1); border: 1px solid rgba(201, 106, 31, 0.3); color: var(--saffron); border-radius: 99px; font-size: 11px; font-weight: 600; padding: 3px 10px; margin-right:4px; }}
    
    .toggle-btn {{ min-width: 44px; min-height: 44px; display: inline-flex; align-items: center; justify-content: center; border-radius: 8px; border: 1px solid var(--border); background: var(--surface2); color: var(--text-sec); font-size: 13px; font-weight: 600; cursor: pointer; padding: 0 14px; transition: all 0.15s; }}
    .toggle-btn.active {{ background: var(--saffron); color: white; border-color: var(--saffron); }}
    .toggle-btn:hover:not(.active) {{ border-color: var(--saffron); color: var(--saffron); }}
    
    .section-heading {{ font-size: 16px; font-weight: 700; color: var(--maroon); border-bottom: 2px solid var(--border); padding-bottom: 8px; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
    
    .word-table th {{ background: var(--surface2); color: var(--text-sec); font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 8px 12px; text-align: left; }}
    .word-table td {{ padding: 8px 12px; border-top: 1px solid var(--border); font-size: 14px; vertical-align: top; }}
    
    .action-bar {{ position: fixed; bottom: 0; left: 0; right: 0; background: var(--bg); border-top: 1px solid var(--border); padding: 10px 16px; z-index: 3500; display:flex; gap:8px; justify-content:center; }}
    .action-btn {{ flex: 1; max-width: 120px; min-height: 44px; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; border: 2px solid transparent; display: flex; align-items: center; justify-content: center; gap: 5px; background:var(--surface2); color:var(--text); }}
    .btn-whatsapp {{ background: #25D366; color: white; }}
    
    .verse-nav-btn {{ min-height: 44px; min-width: 44px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--border); border-radius: 8px; background: var(--surface); color: var(--text-sec); font-size: 14px; font-weight: 600; cursor: pointer; text-decoration: none; padding: 0 16px; }}
    .verse-nav-btn.disabled {{ opacity: 0.4; pointer-events: none; }}
    
    #toast {{ position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%) translateY(20px); background: var(--text); color: white; padding: 10px 20px; border-radius: 99px; font-size: 13px; font-weight: 600; z-index: 4000; opacity: 0; transition: all 0.3s; pointer-events: none; }}
    #toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
    
    /* MODAL STYLES */
    #verse-modal {{ position: fixed; inset: 0; background: var(--bg); z-index: 3000; overflow-y: auto; display: none; padding-bottom: 80px; }}
    #verse-modal.active {{ display: block; }}
    .modal-close {{ position: fixed; top: 16px; right: 16px; background: var(--surface2); border: none; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; color: var(--text); cursor: pointer; z-index: 3100; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
  </style>
</head>
<body class="fs-normal script-both">

  <!-- THE CHAPTER PAGE (Grid of verses) -->
  <div id="chapter-view" class="max-w-5xl mx-auto px-4 py-6 pb-24">
    <div style="margin-bottom: 20px;">
      <a href="/bhagavad-gita.html" style="color:var(--saffron); text-decoration:none; font-weight:600;">← Back to Gita Hub</a>
    </div>
    
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
  </div>

  <!-- THE POP-UP MODAL (For Individual Verses) -->
  <div id="verse-modal">
    <button class="modal-close" onclick="closeVerseModal()">✕</button>
    <div id="modal-content" class="max-w-3xl mx-auto px-4 py-8"></div>
    <div class="action-bar" id="action-bar" style="display:none;">
      <button class="action-btn btn-whatsapp" onclick="shareWhatsApp()">📱 Share</button>
      <button class="action-btn" onclick="copyVerse()">📋 Copy</button>
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
        <nav class="breadcrumb text-sm mb-5" style="color:var(--text-muted);">
          <a href="/bhagavad-gita.html" style="color:var(--saffron);">Gita</a> &rsaquo;
          <a href="/gita/${{CHAPTER_DATA.chapter}}/" onclick="closeVerseModal();return false;" style="color:var(--saffron);">Chapter ${{CHAPTER_DATA.chapter}}</a> &rsaquo;
          <span>Verse ${{v.verse}}</span>
        </nav>
        
        <div class="flex items-center justify-between mb-5">
          <button onclick="${{prevV ? `openVerseModal(${{prevV.verse}})` : 'return false'}}" class="verse-nav-btn ${{!prevV ? 'disabled' : ''}}">← Prev</button>
          <span style="color:var(--text-muted);font-size:12px;">Chapter ${{CHAPTER_DATA.chapter}} of 18</span>
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
      document.getElementById('verse-modal').classList.add('active');
      document.getElementById('action-bar').style.display = 'flex';
      document.body.style.overflow = 'hidden'; // Prevent background scroll
      
      // Update URL to /gita/4/2/ format
      history.pushState(null, null, '/gita/' + CHAPTER_DATA.chapter + '/' + verseNum + '/');
      
      // Update SEO Meta Tags
      document.title = `Bhagavad Gita Chapter ${{CHAPTER_DATA.chapter}} Verse ${{verseNum}}`;
      
      // Scroll modal to top
      document.getElementById('verse-modal').scrollTo(0, 0);
    }}
    
    function closeVerseModal() {{
      document.getElementById('verse-modal').classList.remove('active');
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
    
    // Auto-open modal if URL matches /gita/C/V/
    window.addEventListener('load', () => {{
      const pathParts = window.location.pathname.split('/').filter(p => p);
      // pathParts might be ['gita', '4', '2']
      if (pathParts.length >= 3 && pathParts[0] === 'gita') {{
        const vNum = parseInt(pathParts[2]);
        if (vNum) openVerseModal(vNum);
      }}
    }});
    
    // Handle browser back button
    window.addEventListener('popstate', () => {{
      const pathParts = window.location.pathname.split('/').filter(p => p);
      if (pathParts.length < 3) {{
        // We went back to /gita/4/
        document.getElementById('verse-modal').classList.remove('active');
        document.getElementById('action-bar').style.display = 'none';
        document.body.style.overflow = '';
      }} else {{
        // We went to /gita/4/3/
        const vNum = parseInt(pathParts[2]);
        if (vNum) openVerseModal(vNum);
      }}
    }});
  </script>
</body>
</html>"""
        with open(ch_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(page_html)
            
    # Update _redirects file to ensure /gita/4/2/ serves /gita/4/index.html (200 rewrite)
    redirects_path = ROOT / '_redirects'
    existing_redirects = ""
    if redirects_path.exists():
        with open(redirects_path, 'r', encoding='utf-8') as f:
            existing_redirects = f.read()
            
    # Remove old gita redirects if they exist to avoid duplicates
    new_redirects = []
    for line in existing_redirects.split('\n'):
        if not line.startswith('/gita/'):
            new_redirects.append(line)
            
    # Append the new ones
    new_redirects.append("\n# Gita SPA Routes for 18 Master Pages")
    new_redirects.extend(redirects_entries)
    
    with open(redirects_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_redirects))
            
    print("Generated 18 Master Chapter pages with Same-URL Cloudflare configuration!")

if __name__ == "__main__":
    generate()
