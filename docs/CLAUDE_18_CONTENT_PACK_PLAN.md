# Claude 18-Piece Starter Content Plan (3 per pillar x 6 pillars)

You asked for 18 pieces total. This plan gives exactly 18 high-impact items.

## 1) Bhajans (3)
1. Hanuman bhajan for fear and courage seekers
2. Krishna bhajan for love and devotion seekers
3. Shiva bhajan for inner discipline seekers

## 2) Shlokas (3)
1. Daily protection shloka with meaning
2. Clarity and wisdom shloka for students/professionals
3. Peace and surrender shloka for stress relief intent

## 3) Prayers (3)
1. Morning 10-minute prayer routine
2. New beginning puja sequence (career/business)
3. Family harmony evening prayer sequence

## 4) Bhagavad Gita (3)
1. Verse for anxiety and overthinking
2. Verse for failure and resilience
3. Verse for action without attachment

## 5) Upanishads (3)
1. Atman identity teaching (beginner-friendly)
2. Impermanence and detachment teaching
3. Awareness and silence teaching

## 6) Wisdom Topics (3)
1. Anxiety topic cluster (5 quotes)
2. Failure topic cluster (5 quotes)
3. Anger topic cluster (5 quotes)

---

## Exact prompting formula for each piece
Use this input set in Claude:
1. `prompts/claude/MASTER_CONTENT_SYSTEM_PROMPT.md`
2. One pillar prompt (`01...06`)
3. Matching template JSON file
4. Your topic title and audience intent

## Expected output per item
- One valid JSON object or array entry matching that pillar schema.
- Human tone, practical guidance, devotional integrity.
- SEO-ready slugs/titles/descriptions.

## Scaling from 18 to 333 each pillar
When ready to scale to 333 each pillar:
- Use same schema + prompt system.
- Batch process by themes (deity/occasion/problem/season).
- Ingest through backend API so sheets + SEO pages update automatically.
- Keep weekly quality audit on 20 random items.
