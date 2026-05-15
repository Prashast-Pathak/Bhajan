import json
from pathlib import Path
import html

ROOT = Path('/Users/prashastpathak/Bhajan')
DATA = ROOT / 'data' / 'gita.json'
OUT = ROOT / 'gita'

def safe(v):
    return html.escape(str(v or ""))

def generate_chapter_pages():
    with open(DATA, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    OUT.mkdir(exist_ok=True)
    
    for ch in data.get('chapters', []):
        ch_num = ch['chapter']
        slug = f"chapter-{ch_num}"
        ch_dir = OUT / slug
        ch_dir.mkdir(exist_ok=True)
        
        verses_html = ""
        for v in ch.get('verses', []):
            v_num = v['verse']
            sanskrit = safe(v.get('sanskrit', '')).replace('\\n', '<br>')
            roman = safe(v.get('roman', '')).replace('\\n', '<br>')
            hindi = safe(v.get('hindi_translation', ''))
            english = safe(v.get('english_translation', ''))
            
            verses_html += f"""
            <div id="verse-{v_num}" class="card verse-card" style="margin-bottom: 24px; scroll-margin-top: 100px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 16px;">
                    <span class="gita-badge">Verse {v_num}</span>
                    <button class="toggle-btn" onclick="copyVerseLink({ch_num}, {v_num})" aria-label="Copy Link" style="min-width:32px; min-height:32px; font-size:16px;">🔗</button>
                </div>
                
                <div class="verse-devanagari" style="margin-bottom: 16px;">
                    {sanskrit}
                </div>
                
                <div class="verse-roman" style="margin-bottom: 20px;">
                    {roman}
                </div>
                
                <div style="background: rgba(201, 106, 31, 0.05); padding: 16px; border-radius: 8px; border-left: 4px solid var(--saffron); margin-bottom: 12px;">
                    <strong style="color:var(--saffron);">Hindi:</strong> {hindi}
                </div>
                
                <div style="background: rgba(124, 58, 237, 0.05); padding: 16px; border-radius: 8px; border-left: 4px solid var(--krishna);">
                    <strong style="color:var(--krishna);">English:</strong> {english}
                </div>
            </div>
            """
            
        # Get CTA for this chapter
        cta_html = ""
        # The CTA logic was in scripts/generate_programmatic_pages.py, I'll add a simplified generic one here
        # that redirects back to the main UI or tools
        
        page_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <title>Bhagavad Gita Chapter {ch_num} - {safe(ch.get('title_english', ''))} | NAKSHATRA</title>
  
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Read all verses of Bhagavad Gita Chapter {ch_num}: {safe(ch.get('title_english', ''))}. Complete Sanskrit slokas, Hindi meaning, and English translation.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Lato:wght@400;600;700;900&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --bg: #F5F0E8;
      --surface: #EDE6D8;
      --surface2: #E6DDD0;
      --saffron: #C96A1F;
      --maroon: #6E1515;
      --gold: #A8832A;
      --text: #2A1A08;
      --text-sec: #5C3D20;
      --text-muted: #8C6A45;
      --border: #D9CDBA;
      --krishna: #7C3AED;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      background-color: var(--bg);
      color: var(--text);
      font-family: 'Lato', sans-serif;
      margin: 0;
      padding: 0;
      line-height: 1.6;
    }}
    .container {{
      max-width: 800px;
      margin: 0 auto;
      padding: 20px 16px 80px;
    }}
    .devanagari {{ font-family: 'Tiro Devanagari Hindi', serif; }}
    
    .card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
    }}
    .verse-devanagari {{
      font-family: 'Tiro Devanagari Hindi', serif;
      font-size: 22px;
      line-height: 1.8;
      color: var(--text);
    }}
    .verse-roman {{
      font-size: 16px;
      font-style: italic;
      color: var(--text-sec);
      line-height: 1.7;
    }}
    .gita-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: rgba(124, 58, 237, 0.10);
      border: 1px solid rgba(124, 58, 237, 0.4);
      color: #5b21b6;
      border-radius: 99px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 4px 12px;
    }}
    
    header {{
      text-align: center;
      margin-bottom: 40px;
    }}
    h1 {{
      font-size: 28px;
      color: var(--maroon);
      margin-bottom: 8px;
    }}
    h2 {{
      font-size: 18px;
      color: var(--text-sec);
      font-weight: 600;
      margin-top: 0;
    }}
    .summary {{
      background: white;
      padding: 20px;
      border-radius: 12px;
      border: 1px solid var(--border);
      margin-bottom: 40px;
      color: var(--text-sec);
      font-size: 15px;
    }}
    
    #toast {{
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #333;
      color: white;
      padding: 12px 24px;
      border-radius: 99px;
      font-weight: 600;
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 1000;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }}
    #toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}
    .nav-buttons {{
      display: flex;
      justify-content: space-between;
      margin-top: 40px;
    }}
    .nav-btn {{
      padding: 12px 24px;
      background: var(--surface2);
      color: var(--text);
      text-decoration: none;
      border-radius: 8px;
      font-weight: 600;
      border: 1px solid var(--border);
    }}
  </style>
</head>
<body>

  <div class="container">
    <div style="margin-bottom: 20px;">
      <a href="/bhagavad-gita.html" style="color:var(--saffron); text-decoration:none; font-weight:600;">← Back to Gita Hub</a>
    </div>
    
    <header>
      <div class="gita-badge" style="margin-bottom: 12px; background: rgba(168, 131, 42, 0.12); color: var(--gold); border-color: rgba(168, 131, 42, 0.45);">Chapter {ch_num}</div>
      <h1 class="devanagari">{safe(ch.get('title_hindi', ''))}</h1>
      <h2>{safe(ch.get('title_english', ''))}</h2>
    </header>
    
    <div class="summary">
      <p style="margin-top:0; margin-bottom:12px;"><strong>Summary:</strong> {safe(ch.get('summary_english', ''))}</p>
      <p class="devanagari" style="margin:0;"><strong>सारांश:</strong> {safe(ch.get('summary_hindi', ''))}</p>
    </div>

    <!-- VERSES -->
    {verses_html}
    
    <div class="nav-buttons">
      {f'<a href="/gita/chapter-{ch_num-1}/" class="nav-btn">← Chapter {ch_num-1}</a>' if ch_num > 1 else '<div></div>'}
      {f'<a href="/gita/chapter-{ch_num+1}/" class="nav-btn">Chapter {ch_num+1} →</a>' if ch_num < 18 else '<div></div>'}
    </div>
  </div>
  
  <div id="toast"></div>

  <script>
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2500);
    }}
    
    function copyVerseLink(ch, v) {{
      const url = window.location.origin + window.location.pathname + '#verse-' + v;
      navigator.clipboard.writeText(url).then(() => showToast('🔗 Link copied to clipboard!'));
    }}
    
    // Auto-scroll logic if opened with a hash
    window.addEventListener('load', () => {{
      if (window.location.hash) {{
        const el = document.querySelector(window.location.hash);
        if (el) {{
          setTimeout(() => el.scrollIntoView({{ behavior: 'smooth', block: 'start' }}), 100);
          el.style.borderColor = 'var(--saffron)';
          el.style.boxShadow = '0 0 0 2px var(--saffron)';
          setTimeout(() => {{
            el.style.borderColor = 'var(--border)';
            el.style.boxShadow = 'none';
            el.style.transition = 'all 1s';
          }}, 2000);
        }}
      }}
    }});
  </script>
</body>
</html>"""

        with open(ch_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(page_html)
            
    print(f"Generated 18 Master Chapter pages in {OUT}")

if __name__ == "__main__":
    generate_chapter_pages()
