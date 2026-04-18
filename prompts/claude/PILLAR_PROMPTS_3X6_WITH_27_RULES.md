# 3 Prompts per Pillar (18 total) with 27 Mandatory Rules

Use these exactly in Claude. Each prompt includes the full rule set.

## Universal 27 Rules (paste in every Claude run)
1. Keep JSON valid at all times.
2. Do not change key names.
3. Do not remove required keys.
4. Do not add extra keys unless requested.
5. Use clean UTF-8 Devanagari.
6. Keep transliteration pronounceable.
7. Keep English natural and human.
8. Avoid AI-sounding repetition.
9. Keep spiritual tone respectful.
10. No sensational claims.
11. No guaranteed results language.
12. No medical cure claims.
13. No legal/financial guarantee claims.
14. Use "traditionally believed" phrasing for benefits.
15. No fear-based manipulation.
16. No harmful/tantric unsafe instructions.
17. No restricted beej-mantra practice instructions.
18. Keep Sanskrit and meanings aligned.
19. Keep source references accurate.
20. Keep slugs lowercase-hyphenated.
21. Keep SEO title readable and natural.
22. Keep SEO description concise (<160 chars).
23. Keep tags relevant to intent.
24. Keep cross-links meaningful.
25. Keep commentary practical for daily life.
26. If uncertain, mark uncertainty and avoid fabrication.
27. Output only JSON (no markdown, no explanation).

---

## Bhajans (3 Prompts)

### Bhajans Prompt 1: Fear to Courage
Fill `templates/pillar-json/bhajans.template.json` with one bhajan focused on courage, discipline, and emotional resilience. Target users searching fear relief and confidence. Follow all 27 rules above. Return only JSON.

### Bhajans Prompt 2: Devotion and Love
Fill `templates/pillar-json/bhajans.template.json` with one Krishna/Ram devotion bhajan for bhakti, surrender, and peace. Keep story and significance deeply human. Follow all 27 rules above. Return only JSON.

### Bhajans Prompt 3: Festival Intent
Fill `templates/pillar-json/bhajans.template.json` with one festival-specific bhajan (choose one major festival). Include practical timing/occasion fields and meaningful SEO. Follow all 27 rules above. Return only JSON.

---

## Shlokas (3 Prompts)

### Shlokas Prompt 1: Daily Protection
Fill `templates/pillar-json/shlokas.template.json` with one shloka used in daily prayer for inner protection and stability. Add accurate source and clean word-by-word meanings. Follow all 27 rules above. Return only JSON.

### Shlokas Prompt 2: Student/Focus Intent
Fill `templates/pillar-json/shlokas.template.json` with one shloka for focus, wisdom, and disciplined action. Keep commentary practical for students and professionals. Follow all 27 rules above. Return only JSON.

### Shlokas Prompt 3: Peace/Stress Intent
Fill `templates/pillar-json/shlokas.template.json` with one calming shloka for stress and overthinking. Keep tone gentle and grounded. Follow all 27 rules above. Return only JSON.

---

## Prayers (3 Prompts)

### Prayers Prompt 1: Morning Routine
Fill `templates/pillar-json/prayers.template.json` with one 10–15 minute beginner morning prayer sequence. Keep steps practical and realistic. Follow all 27 rules above. Return only JSON.

### Prayers Prompt 2: New Beginnings
Fill `templates/pillar-json/prayers.template.json` with one puja sequence for starting new work/business/study phase. Keep materials simple and accessible. Follow all 27 rules above. Return only JSON.

### Prayers Prompt 3: Family Harmony
Fill `templates/pillar-json/prayers.template.json` with one evening family prayer flow for calm communication and gratitude. Follow all 27 rules above. Return only JSON.

---

## Bhagavad Gita (3 Prompts)

### Gita Prompt 1: Anxiety
Fill `templates/pillar-json/gita.template.json` with one verse entry for anxiety/overthinking intent with practical life application. Follow all 27 rules above. Return only JSON.

### Gita Prompt 2: Failure and Recovery
Fill `templates/pillar-json/gita.template.json` with one verse entry focused on failure, courage, and steady effort. Keep commentary modern and actionable. Follow all 27 rules above. Return only JSON.

### Gita Prompt 3: Karma and Detachment
Fill `templates/pillar-json/gita.template.json` with one verse entry about action without attachment. Keep translation readable for beginners. Follow all 27 rules above. Return only JSON.

---

## Upanishads (3 Prompts)

### Upanishads Prompt 1: Atman Identity
Fill `templates/pillar-json/upanishads.template.json` with one verse-focused entry teaching Atman identity in beginner language. Follow all 27 rules above. Return only JSON.

### Upanishads Prompt 2: Impermanence
Fill `templates/pillar-json/upanishads.template.json` with one teaching on impermanence, detachment, and discernment. Keep commentary practical, not abstract-only. Follow all 27 rules above. Return only JSON.

### Upanishads Prompt 3: Awareness and Silence
Fill `templates/pillar-json/upanishads.template.json` with one teaching centered on awareness, silence, and self-inquiry. Follow all 27 rules above. Return only JSON.

---

## Wisdom (3 Prompts)

### Wisdom Prompt 1: Anxiety Topic
Fill `templates/pillar-json/wisdom.template.json` with one anxiety topic containing 5 quotes from valid scripture references and practical applications. Follow all 27 rules above. Return only JSON.

### Wisdom Prompt 2: Anger Topic
Fill `templates/pillar-json/wisdom.template.json` with one anger-management topic containing 5 quotes and daily-life guidance. Follow all 27 rules above. Return only JSON.

### Wisdom Prompt 3: Failure Topic
Fill `templates/pillar-json/wisdom.template.json` with one failure-and-resilience topic containing 5 quotes and non-preachy practical applications. Follow all 27 rules above. Return only JSON.
