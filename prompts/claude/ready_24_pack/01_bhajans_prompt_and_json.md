# Bhajans: Prompt + JSON Structure + 4 Topics

## Claude Prompt (copy-paste)
Use the JSON structure below and create one bhajan entry ONLY for an already-existing, authentic, traditional bhajan text (no newly written bhajan lines).
Follow these strict rules: keep valid JSON, no key changes, devotional tone, no miracle claims, no fear language, no medical/financial guarantees, no unsafe tantra instructions, no restricted beej-mantra practice guidance, accurate Hindi/Sanskrit/transliteration alignment, natural SEO title/description, output only JSON.

Return exactly one JSON object matching the schema.

## JSON Structure
```json
{
  "id": 1001,
  "slug": "authentic-bhajan-slug",
  "title_hindi": "",
  "title_roman": "",
  "title_english": "",
  "deity": "",
  "deity_color": "#EA580C",
  "language": "Hindi",
  "festival": [],
  "occasion": "",
  "timing": "",
  "raga": "",
  "composer": "Traditional",
  "source_name": "",
  "source_ref": "",
  "source_edition": "",
  "is_excerpt": false,
  "excerpt_range": "full",
  "verification_notes": "",
  "duration_minutes": 8,
  "tags": [],
  "topics": [],
  "story": "",
  "story_hindi": "",
  "significance": "",
  "significance_hindi": "",
  "benefits": ["Traditionally recited for inner peace."],
  "when_to_sing": {
    "festival": [],
    "time": ["Morning"],
    "occasion": ["Daily"]
  },
  "featured": false,
  "priority": 100,
  "verses": [
    {
      "type": "verse",
      "label_hindi": "पंक्ति",
      "label_english": "Verse",
      "source_name": "",
      "source_ref": "",
      "source_line_index": "",
      "lines": [
        {
          "hindi": "",
          "roman": "",
          "hindi_meaning": "",
          "english": ""
        }
      ]
    }
  ],
  "related": [],
  "seo": {
    "meta_title": "",
    "meta_description": "",
    "keywords": []
  }
}
```

## 4 Authentic Bhajan Names
1. भज गोविन्दम् (`bhaja-govindam`)
2. आदित्य हृदय स्तोत्र (`aditya-hridayam`)
3. राम रक्षा स्तोत्र (`ram-raksha-stotra`)
4. गणपति अथर्वशीर्ष (`ganapati-atharvashirsha`)
