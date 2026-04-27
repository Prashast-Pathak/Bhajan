# Upanishads: Prompt + JSON Structure + 4 Topics

## Claude Prompt (copy-paste)
Generate one Upanishad entry/section in the structure below using ONLY authentic, source-backed Upanishadic verses/teachings (no newly composed philosophical text).
Rules: valid JSON, no key changes, philosophical clarity for beginners, no fabricated claims, no mystical exaggeration, practical commentary, output only JSON.

## JSON Structure
```json
{
  "id": 5001,
  "slug": "authentic-upanishad-slug",
  "name_english": "",
  "name_hindi": "",
  "name_sanskrit": "",
  "source_name": "",
  "source_ref": "",
  "source_edition": "",
  "is_excerpt": false,
  "excerpt_range": "full verse context",
  "verification_notes": "",
  "veda": "",
  "total_verses": 0,
  "sections": [],
  "theme_english": "",
  "theme_hindi": "",
  "intro_english": "",
  "intro_hindi": "",
  "related_gita_chapters": [],
  "verses": [
    {
      "verse": 1,
      "slug": "",
      "source_name": "",
      "source_ref": "",
      "source_line_index": "",
      "sanskrit": "",
      "roman": "",
      "hindi_translation": "",
      "english_translation": "",
      "commentary": "",
      "keywords": []
    }
  ]
}
```

## 4 Authentic Upanishad Targets
1. ईशोपनिषद् मंत्र 1 (`isha-upanishad-1`)
2. केनोपनिषद् 1.1 (`kena-upanishad-1`)
3. कठोपनिषद् 1.2.18 (`katha-upanishad-1-2-18`)
4. माण्डूक्य उपनिषद् मंत्र 7 (`mandukya-upanishad-7`)
