import json

new_verses = [
    {
      "lines": [
        {
          "hindi": "मेरी चौखट पे चल के आज चारो धाम आये हैं।",
          "roman": "Meri chaukhat pe chal ke aaj, Charo dham aaye hain,",
          "english": "Today, all four holy pilgrimage sites have walked to my doorstep,",
          "hindi_meaning": "आज मेरे द्वार पर स्वयं चारों धाम चलकर आए हैं,"
        },
        {
          "hindi": "बजाओ ढोल स्वागत में, मेरे घर राम आये हैं।",
          "roman": "Bajao dhol swagat mein, Mere ghar Ram aaye hain.",
          "english": "Beat the drums in welcome, for Lord Ram has come to my home.",
          "hindi_meaning": "ढोल-नगाड़ों से स्वागत करो, क्योंकि मेरे घर राम आए हैं।"
        }
      ]
    },
    {
      "lines": [
        {
          "hindi": "कथा शबरी की जैसे जुड़ गयी, मेरी कहानी से।",
          "roman": "Katha Shabri ki jaise jud gayi, Meri kahani se,",
          "english": "My story has become connected with the tale of Shabari,",
          "hindi_meaning": "मेरी कहानी शबरी की कथा से जुड़ गई है,"
        },
        {
          "hindi": "ना रोको आज धोने दो, चरण आँखों के पानी से।",
          "roman": "Na roko aaj dhone do, Charan aankhon ke paani se,",
          "english": "Do not stop me today, let me wash His feet with my tears.",
          "hindi_meaning": "मुझे मत रोको, आज प्रभु के चरण अपने आंसुओं से धोने दो।"
        },
        {
          "hindi": "बहुत खुश हैं मेरे आँसू, के प्रभु के काम आये हैं।",
          "roman": "Bahut khush hain mere aansu, Ke Prabhu ke kaam aaye hain,",
          "english": "My tears are so happy that they are of use to the Lord,",
          "hindi_meaning": "मेरे आंसू बहुत खुश हैं कि वे भगवान के काम आ रहे हैं,"
        },
        {
          "hindi": "बजाओ ढोल स्वागत में, मेरे घर राम आये हैं।",
          "roman": "Bajao dhol swagat mein, Mere ghar Ram aaye hain.",
          "english": "Beat the drums in welcome, for Lord Ram has come to my home.",
          "hindi_meaning": "ढोल-नगाड़ों से स्वागत करो, क्योंकि मेरे घर राम आए हैं।"
        }
      ]
    },
    {
      "lines": [
        {
          "hindi": "तुमको पा के क्या पाया है, सृष्टि के कण-कण से पूछो।",
          "roman": "Tumko paa ke kya paaya hai, Srishti ke kan-kan se puchho,",
          "english": "Ask every particle of creation what I have gained by finding You,",
          "hindi_meaning": "तुम्हें पाकर मैंने क्या पाया है, यह सृष्टि के कण-कण से पूछो,"
        },
        {
          "hindi": "तुमको खोने का दुःख क्या है, कौशल्या के मन से पूछो।",
          "roman": "Tumko khone ka dukh kya hai, Kaushalya ke mann se puchho.",
          "english": "Ask the heart of Mother Kaushalya what the pain of losing You feels like.",
          "hindi_meaning": "तुम्हें खोने का दुख क्या होता है, माता कौशल्या के हृदय से पूछो।"
        }
      ]
    },
    {
      "lines": [
        {
          "hindi": "द्वार मेरे ये अभागे, आज इनके भाग जागे।",
          "roman": "Dwaar mere ye abhage, Aaj inke bhaag jaage,",
          "english": "These unfortunate doors of mine have awakened to good fortune today,",
          "hindi_meaning": "मेरे इन अभागे द्वारों के आज भाग्य जाग उठे हैं,"
        },
        {
          "hindi": "बड़ी लंबी इंतज़ारी हुई, रघुवर तुम्हारी तब आई है सवारी।",
          "roman": "Badi lambi intezaari hui, Raghuvar tumhari tab aayi hai sawaari,",
          "english": "After a very long wait, O Raghuvar, Your chariot has finally arrived.",
          "hindi_meaning": "बहुत लंबे इंतजार के बाद हे रघुवर, तुम्हारी सवारी आई है।"
        },
        {
          "hindi": "संदेशे आज खुशियों के, हमारे नाम आये हैं।",
          "roman": "Sandeshe aaj khushiyon ke, Humare naam aaye hain,",
          "english": "Messages of true joy have come in our name today,",
          "hindi_meaning": "आज खुशियों के संदेश हमारे नाम आए हैं,"
        },
        {
          "hindi": "बजाओ ढोल स्वागत में, मेरे घर राम आये हैं।",
          "roman": "Bajao dhol swagat mein, Mere ghar Ram aaye hain.",
          "english": "Beat the drums in welcome, for Lord Ram has come to my home.",
          "hindi_meaning": "ढोल-नगाड़ों से स्वागत करो, क्योंकि मेरे घर राम आए हैं।"
        }
      ]
    },
    {
      "lines": [
        {
          "hindi": "दर्शन पा के हे अवतारी, धन्य हुए हैं नैन पुजारी।",
          "roman": "Darshan paa ke he avtari, Dhanya hue hain nain pujari,",
          "english": "Having Your vision, O Divine Avatar, these worshipping eyes are blessed.",
          "hindi_meaning": "हे अवतारी, आपके दर्शन पाकर मेरे पुजारी नयन धन्य हो गए हैं।"
        },
        {
          "hindi": "जीवन नैया तुमने तारी, मंगल भवन अमंगल हारी।",
          "roman": "Jeewan naiya tumne taari, Mangal bhavan amangal haari,",
          "english": "You have rowed my boat of life across, O abode of auspiciousness and destroyer of inauspiciousness.",
          "hindi_meaning": "आपने मेरे जीवन की नैया पार लगा दी, हे मंगल के धाम और अमंगल हरने वाले।"
        }
      ]
    },
    {
      "lines": [
        {
          "hindi": "निर्धन का तुम धन हो राघव, तुम ही रामायण हो राघव।",
          "roman": "Nirdhan ka tum dhan ho Raghav, Tum hi Ramayan ho Raghav,",
          "english": "You are the wealth of the poor, O Raghav, You Yourself are the Ramayan.",
          "hindi_meaning": "हे राघव, आप निर्धन का धन हैं, आप ही रामायण हैं।"
        },
        {
          "hindi": "सब दुःख हरना अवध बिहारी, मंगल भवन अमंगल हारी।",
          "roman": "Sab dukh harna Avadh Bihari, Mangal bhavan amangal haari,",
          "english": "Remove all my sorrows, O Lord of Avadh, abode of auspiciousness and destroyer of inauspiciousness.",
          "hindi_meaning": "हे अवध बिहारी, मेरे सभी दुखों को हर लें, मंगल भवन अमंगल हारी।"
        },
        {
          "hindi": "चरण की धूल ले लूँ मैं, मेरे भगवान आये हैं।",
          "roman": "Charan ki dhool le loon main, Mere bhagwan aaye hain,",
          "english": "Let me take the dust of Your feet, for my God has arrived.",
          "hindi_meaning": "मैं आपके चरणों की धूल मस्तक पर लगा लूं, क्योंकि मेरे भगवान आए हैं।"
        },
        {
          "hindi": "बजाओ ढोल स्वागत में, मेरे घर राम आये हैं।",
          "roman": "Bajao dhol swagat mein, Mere ghar Ram aaye hain.",
          "english": "Beat the drums in welcome, for Lord Ram has come to my home.",
          "hindi_meaning": "ढोल-नगाड़ों से स्वागत करो, क्योंकि मेरे घर राम आए हैं।"
        }
      ]
    }
]

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'mere-ghar-ram-aayo':
        b['verses'] = new_verses

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Expanded 'mere-ghar-ram-aayo' from 3 to 6 complete verses!")
