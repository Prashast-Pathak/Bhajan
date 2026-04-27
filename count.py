import json

def get_count(path, key=None):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if key: data = data.get(key, [])
            return len(data), data
    except:
        return 0, []

bhajan_c, bhajans = get_count("data/bhajans.json")
shloka_c, shlokas = get_count("data/shlokas.json")
prayer_c, prayers = get_count("data/prayers.json", "prayers")
upa_c, upanishads = get_count("data/upanishads.json")
wis_c, wisdoms = get_count("data/wisdom.json", "topics")

# Gita is special
gita_verses = 0
try:
    with open("data/gita.json", "r") as f:
        gita = json.load(f).get("chapters", [])
        for c in gita:
            gita_verses += len(c.get("verses", []))
except:
    pass

# Calculating pages:
# Bhajans: 7 general intents per bhajan + 2 intents per verse
b_pages = 0
for b in bhajans:
    b_pages += 7
    verses = b.get("verses", [])
    b_pages += len(verses) * 2

# Shlokas: 4 general intents
# Prayers: 3 general intents
# Upanishads: 3 general intents
# Wisdom: 3 general intents
# Gita: 3 intents per verse

print(f"Bhajans: {bhajan_c} items -> {b_pages} pages")
print(f"Shlokas: {shloka_c} items -> {shloka_c * 4} pages")
print(f"Prayers: {prayer_c} items -> {prayer_c * 3} pages")
print(f"Upanishads: {upa_c} items -> {upa_c * 3} pages")
print(f"Wisdom: {wis_c} items -> {wis_c * 3} pages")
print(f"Gita: {gita_verses} verses -> {gita_verses * 3} pages")
total = b_pages + (shloka_c * 4) + (prayer_c * 3) + (upa_c * 3) + (wis_c * 3) + (gita_verses * 3)
print(f"Total Programmatic Pages to be generated: {total}")
