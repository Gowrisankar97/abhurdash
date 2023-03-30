def dosha(d1):
    dosha=[]
    vata_samaa=['Enthusiasm',
  'Respiration',
  'Normal movements of body',
  'Normal expulsion of urges',
  'Normal Sense organs function']
    vata_vriddhi= ['Leanness',
  'Blackish discoloration',
  'Tremor',
  'Abdominal distension',
  'Constipation',
  'Decreased body strength',
  'Decreased sense organ functioning',
  'Insomnia',
  'Incoherent speech',
  'Dizziness',
  'Nervousness']
    vata_kshaya=['Weakness of body parts',
  'Decreased speech',
  'Decreased physical activity',
  'Uconsciousness']
    pitta_samaa=['Optimal digestion',
  'Optimal hunger',
  'Optimal Thirst',
  'Normal colour and complexion',
  'Increased intelligence']
    pitta_vriddhi= ['Yellow faeces',
  'Yellow urine',
  'Yellow eyes',
  'Yellow skin',
  'Increased hunger',
  'Increased thirst',
  'Burning sensation',
  'Insomnia']
    pitta_kshaya=['Indigestion', 'Coldness', 'Loss of skin texture']
    kapha_samaa=['Physical stability',
  'Compactness of joints',
  'Virility',
  'Mental toughness']
    kapha_vriddhi=['Decreased digestion',
  'Excess salivation',
  'Laziness,',
  'Heaviness',
  'White faeces',
  'White urine',
  'White eyes',
  'Coldness',
  'Loose joints',
  'Dyspnea',
  'Cough',
  'Excess sleep']
    kapha_kshaya=['Giddiness', 'Heart palpitation']

    for i in d1:
        if str(i) in vata_samaa:
            dosha.append("Vata-samaa")
        elif str(i) in vata_vriddhi:
            dosha.append("Vata-vrriddhi")
        elif str(i) in vata_kshaya:
            dosha.append("Vata-kshaya")
        elif str(i) in pitta_samaa:
            dosha.append("Pitta-samaa")
        elif str(i) in pitta_kshaya:
            dosha.append("Pitta-kshaya")
        elif str(i) in pitta_vriddhi:
            dosha.append("Pitta-vriddhi")
        elif str(i) in kapha_samaa:
            dosha.append("Kapha-samaa")
        elif str(i) in kapha_kshaya:
            dosha.append("Kapha-kshaya")
        elif str(i) in kapha_vriddhi:
            dosha.append("Kapha-vriddhi")

    doshas = list(set(dosha))
    return doshas


def dhatus (d2):
    rasa_samaa=['Optimum nourshment']
    rasa_vriddhi=['Increased salivation',
  'Anorexia',
  'Nausea',
  'Channel block',
  'Aversion to sweets',
  'Body pain']
    rasa_kshaya=['Dryness of body', 'Tiredness', 'Emaciation', 'Intolerant to sounds']
    rakta_samaa=['Proper blood supply']
    rakta_vriddhi=['Skin disorders',
  'Bleeding disorders',
  'Jaundice',
  'Decreased digestion',
  'Darkness below eyes',
  'Red urine',
  'Redness',
  'Red eyes']
    raktha_kshaya=['Dry skin', 'Desires sour and cold substances', 'Flaccid veins']
    mamsa_samaa=['Optimum muscle growth', 'Well-built body']
    mamsa_vriddhi=['Enlarged neck and thighs', 'Tumors']
    mamsa_kshaya=['Weak sense organs', 'Wasting of buttocks and thighs', 'Joint pain']
    medas_samaa=['Stable eyes', 'Stable body', 'Optimum unctousness']
    medas_vriddhi=['Tiredness',
  'Dyspnoea on exertion',
  'Drooping buttocks',
  'breasts and abdomen']
    medas_kshaya=['Loss of hip sensation', 'Emaciation']
    asthi_samaa= ['Erect body posture', 'Withstand heavy work']
    asthi_vriddhi=['Increased bones', 'Increased teeth']
    asthi_kshaya=['Tooth fall', 'Hair fall', 'Falling nails', 'Pricking joint pain']
    majja_samaa=['Increased body strength']
    majja_vriddhi=['Heavy eyes', 'Heaviness of body']
    majja_kshaya=['Hollow bones', 'Bone pain', 'Giddiness', 'Black-outs']
    dhatus=[]
    for i in  d2:
        if i in rasa_samaa:
            dhatus.append("Rada-samaa")
        elif i in rasa_vriddhi:
            dhatus.append("Rasa-vriddhi")
        elif i in rasa_kshaya:
            dhatus.append("Rasa-kshaya")
        elif i in rakta_samaa:
            dhatus.append("Rakta-samaa")
        elif i in rakta_vriddhi:
            dhatus.append("Rakta-vriddhi")
        elif i in raktha_kshaya:
            dhatus.append("Rakta-kshaya")
        elif i in mamsa_samaa:
            dhatus.append("Mamsa-samaa")
        elif i in mamsa_vriddhi:
            dhatus.append("Mamsa-vriddhi")
        elif i in mamsa_kshaya:
            dhatus.append("Mamsa-kshaya")
        elif i in medas_samaa:
            dhatus.append("Medas-samaa")
        elif i in medas_vriddhi:
            dhatus.append("Medas-vriddhi")
        elif i in medas_kshaya:
            dhatus.append("Medas-kshaya")
        elif i in asthi_samaa:
            dhatus.append('Asthi-samaa')
        elif i in asthi_vriddhi:
            dhatus.append("Asthi-vriddhi")
        elif i in asthi_kshaya:
            dhatus.append("Asthi-kshaya")
        elif i in majja_samaa:
            dhatus.append("Majja-samaa")
        elif i in majja_vriddhi:
            dhatus.append("Majja-vriddhi")
        elif i in majja_kshaya:
            dhatus.append("Majja-kshaya")
    dhatus=list(set(dhatus))
    return  dhatus


def desha(d3):
    desha=[]
    for a in d3:
        if str(a)=="Wetland":
            desha.append("Anoopa")
        elif str(a)=="Dry land":
            desha.append("Jaagarana")
        elif str(a)=="Normal":
            desha.append("Saadharana")
    desha=list(set(desha))
    return  desha

def kaala(d4):
    kaala=[]
    for a in d4:
        if str(a)=="Less than 1 year old":
            kaala.append("Ksheerapa")
        elif str(a)=="1-2 years old":
            kaala.append("Ksheera-annada")
        elif str(a)==">2 years old":
            kaala.append("Annada")
    kaala=list(set(kaala))
    return kaala

def bala(d5):
    bala=[]
    for a in d5:
        if str(a)=="Cannot perform any activities":
            bala.append("Avara")
        elif str(a)=="Can perform activities with difficulty":
            bala.append("Madhyama")
        elif str(a)=="Call perform all activities":
            bala.append("Pravara")
    bala=list(set(bala))
    return bala

def anala(d6):
    anala=[]
    for a in d6:
        if str(a)=="No hunger even after no intake":
            anala.append("Avara")
        elif str(a)=="Moderate appetite":
            anala.append("Madhyama")
        elif str(a)=="Extremely hungry after heavy food":
            anala.append("Pravara")
    anala=list(set(anala))
    return anala
def satva(d7):
    satva=[]
    avara=["Cries often","Difficult to comfort when hurt","Hurts others on purpose","Scared, Slow learner","Annoyed easily","Unfriendly with everyone","Friendly with strangers"]
    madhyama=["Cries reasonably","Can withstand little pain","Kind - hearted","Learn at normal pace","Disobedient at times","Hyperactive","Sleeps late","Choosy friends"]
    pravara=["Brave, Withstand any pain","Strong,Fast learner","Obedient,Friendly with all"]
    for i in d7:
        if i in avara:
            satva.append("Avara")
        elif i in madhyama:
            madhyama.append("Madhyama")
        elif i in pravara:
            pravara.append("Pravara")

    satva=list(set(satva))
    return satva

def saatmya(d8):
    saatmya=[]
    avara=["Prefers only specific taste","Doesn’t take dairy products"]
    for a in d8:
         if str(a) in avara:
             saatmya.append("Avara")
         elif str(a)=="Prefers some tastes only":
             saatmya.append("Madhyama")
         elif str(a)=="Prefers all taste of food and dairy products":
             saatmya.append("Pravara")
    saatmya=list(set(saatmya))
    return saatmya

def rogakaala(d9):
    rogakaala=[]

    for a in d9:
         if str(a)=="Symptoms occurred within a week":
             rogakaala.append("Avara")
         elif str(a)=="Symptoms persisting for a month":
             rogakaala.append("Madhyama")
         elif str(a)=="Symptoms persisting from months to years":
             rogakaala.append("Pravara")
    rogakaala=list(set(rogakaala))
    return rogakaala


def assesform(a, b):
 finaloutput1 = ["Division-creteria"]
 for i in range(len(a)):
  tex = str(a[i] + " -> " + str(b[i])[2:-2])
  finaloutput1.append(tex)
 return finaloutput1
