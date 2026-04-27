#!/usr/bin/env python3
"""
fix_duplicate_ui_blocks.py
Collapses 3 × duplicate GLOBAL UI TOGGLES + CHANTING MODE blocks
into a single clean consolidated block in each template page.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent.parent

# Pages that have the 3-dupe pattern
PAGES = ["shlokas.html", "wisdom.html", "prayers.html", "upanishads.html"]

# ── The single canonical block to inject ──────────────────────────────────────
CANONICAL_BLOCK = """\
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

    // Font Size Toggle (optional — only present on some pages)
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

# ── Regex: matches ALL consecutive GLOBAL UI TOGGLES + CHANTING MODE blocks ──
# Each individual <script> block begins right after a blank line after the previous </script>
# We match the entire stretch from the first duplicate block up to and including
# the </script> closing the CHANTING MODE block (the last block before the breadcrumb).
DUPE_PATTERN = re.compile(
    r'(<script>\s*\n// ── GLOBAL UI TOGGLES ──.*?</script>\s*\n)+'  # 1–3 GLOBAL UI blocks
    r'(\s*<script>\s*\n// ── CHANTING MODE ──.*?</script>)',         # + CHANTING MODE block
    re.DOTALL
)

def fix_page(filename: str):
    path = ROOT / filename
    text = path.read_text(encoding="utf-8")

    matches = list(DUPE_PATTERN.finditer(text))
    if not matches:
        print(f"  [SKIP] {filename} — pattern not found (already fixed or different structure)")
        return

    if len(matches) > 1:
        print(f"  [WARN] {filename} — {len(matches)} pattern occurrences found, fixing first only")

    m = matches[0]
    print(f"  [FIX]  {filename} — replacing lines ~{text[:m.start()].count(chr(10))+1}–"
          f"{text[:m.end()].count(chr(10))+1} ({m.end()-m.start()} chars → {len(CANONICAL_BLOCK)} chars)")

    new_text = text[:m.start()] + CANONICAL_BLOCK + "\n" + text[m.end():]
    path.write_text(new_text, encoding="utf-8")
    print(f"         ✓ Saved {path.name}")

def main():
    print("=== Fixing duplicate UI toggle blocks ===\n")
    for page in PAGES:
        fix_page(page)
    print("\n=== Done ===")

if __name__ == "__main__":
    main()
