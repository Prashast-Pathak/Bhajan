# Bhajan Content (Templates)

Add one file per bhajan/stotra/chalisa here.

## Filename

Use the slug:
- `hanuman-chalisa.json`

## Minimal template

```json
{
  "slug": "hanuman-chalisa",
  "type": "chalisa",
  "deity": "Hanuman",
  "language": "hi",
  "title_hindi": "हनुमान चालीसा",
  "title_roman": "Hanuman Chalisa",
  "title_english": "Hanuman Chalisa",
  "seo": {
    "meta_title": "Hanuman Chalisa (Hindi) — Lyrics with Meaning | Sanatan Gyan Sagar",
    "meta_description": "Read Hanuman Chalisa in Hindi with roman + meaning. Free, fast, and shareable.",
    "keywords": ["hanuman chalisa", "lyrics", "meaning", "hindi"]
  },
  "rights": { "license": "traditional", "source": "traditional/public domain", "notes": "" },
  "safety": { "disallow_beej": true },
  "crosslinks": { "astrology_intents": ["weak_mars", "protection_prayer"] },
  "verses": [
    {
      "type": "intro",
      "label_hindi": "दोहा",
      "label_english": "Doha",
      "lines": [
        {
          "hindi": "श्री गुरु चरन सरोज रज...",
          "roman": "Shri Guru Charan Saroj Raj...",
          "hindi_meaning": "…",
          "english": "…"
        }
      ]
    }
  ]
}
```

## Notes
- `rights` is mandatory. If you don’t know copyright status, **don’t add it**.
- Beej syllables are blocked by default by the build script.

