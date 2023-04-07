from flask import Flask, render_template, request
app = Flask(__name__)
import assess



@app.route('/', methods=['GET',"POST"])
def dropdown():
    if request.method == "POST":

     dosha = request.form.getlist("dosha")
     dhatus = request.form.getlist("dhatus")
     bala = request.form.getlist("bala")
     desha = request.form.getlist("desha")
     kaala = request.form.getlist("kaala")
     anala = request.form.getlist("anala")
     saatmya = request.form.getlist("saatmya")
     satva = request.form.getlist("satva")
     rogakaala = request.form.getlist("rogakaala")
     doshas=assess.dosha(dosha)
     dhatus=assess.dhatus(dhatus)
     bala=assess.bala(bala)
     desha=assess.desha(desha)
     kaala=assess.kaala(kaala)
     anala=assess.anala(anala)
     saatmya=assess.saatmya(saatmya)
     satva=assess.satva(satva)
     rogakaala=assess.rogakaala(rogakaala)
     division = ["Dosha", "Dhatus", "Bala", "Desha", "Kaala", "Anala", "Saatmya", "Satva", "Rogakaala"]
     creteria = [doshas, dhatus, bala, desha, kaala, anala, saatmya,satva,rogakaala]
     output=assess.assesform(division,creteria)


     return render_template("result.html",division=output)
    else:
        dosha=['Enthusiasm',
 'Respiration',
 'Normal movements of body',
 'Normal expulsion of urges',
 'Normal Sense organs function',
 'Leanness',
 'Blackish discoloration',
 'Tremor',
 'Abdominal distension',
 'Constipation',
 'Decreased body strength',
 'Decreased sense organ functioning',
 'Insomnia',
 'Incoherent speech',
 'Dizziness',
 'Nervousness',
 'Weakness of body parts',
 'Decreased speech',
 'Decreased physical activity',
 'Uconsciousness',
 'Optimal digestion',
 'Optimal hunger',
 'Optimal Thirst',
 'Normal colour and complexion',
 'Increased intelligence',
 'Yellow faeces',
 'Yellow urine',
 'Yellow eyes',
 'Yellow skin',
 'Increased hunger',
 'Increased thirst',
 'Burning sensation',
 'Insomnia',
 'Indigestion',
 'Coldness',
 'Loss of skin texture',
 'Physical stability',
 'Compactness of joints',
 'Virility',
 'Mental toughness',
 'Decreased digestion',
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
 'Excess sleep',
 'Giddiness',
 'Heart palpitation']
        dhatus=['Optimum nourshment',
 'Increased salivation',
 'Anorexia',
 'Nausea',
 'Channel block',
 'Aversion to sweets',
 'Body pain',
 'Dryness of body',
 'Tiredness',
 'Emaciation',
 'Intolerant to sounds',
 'Proper blood supply',
 'Skin disorders',
 'Bleeding disorders',
 'Jaundice',
 'Decreased digestion',
 'Darkness below eyes',
 'Red urine',
 'Redness',
 'Red eyes',
 'Dry skin',
 'Desires sour and cold substances',
 'Flaccid veins',
 'Optimum muscle growth',
 'Well-built body',
 'Enlarged neck and thighs',
 'Tumors',
 'Weak sense organs',
 'Wasting of buttocks and thighs',
 'Joint pain',
 'Stable eyes',
 'Stable body',
 'Optimum unctousness',
 'Tiredness',
 'Dyspnoea on exertion',
 'Drooping buttocks',
 'Dropping breasts and abdomen',
 'Loss of hip sensation',
 'Emaciation',
 'Erect body posture',
 'Withstand heavy work',
 'Increased bones',
 'Increased teeth',
 'Tooth fall',
 'Hair fall',
 'Falling nails',
 'Pricking joint pain',
 'Increased body strength',
 'Heavy eyes',
 'Heaviness of body',
 'Hollow bones',
 'Bone pain',
 'Giddiness',
 'Black-outs']
        desha=["Wetland","Normal","Dry land"]
        kaala=["Less than 1 year old","1-2 years old",">2 years old"]
        bala=["Cannot perform any activities","Can perform activities with difficulty","Call perform all activities"]
        anala=["No hunger even after no intake","Moderate appetite","Extremely hungry after heavy food"]
        satva=["Cries often","Difficult to comfort when hurt","Hurts others on purpose","Scared, Slow learner","Annoyed easily","Unfriendly with everyone","Friendly with strangers",
               "Cries reasonably","Can withstand little pain","Kind - hearted","Learn at normal pace","Disobedient at times","Hyperactive","Sleeps late","Choosy friends",
               "Brave, Withstand any pain","Strong,Fast learner","Obedient,Friendly with all"]
        saatmya=["Prefers only specific taste","Doesn’t take dairy products","Prefers some tastes only",
"Prefers all taste of food and dairy products"]
        rogakaala=["Symptoms occurred within a week","Symptoms persisting for a month","Symptoms persisting from months to years"]

        return render_template('input.html', doshas=dosha,dhatuss=dhatus,deshas=desha,kaalas=kaala,balas=bala,analas=anala,satvas=satva,saatmyas=saatmya,rogakaalas=rogakaala)
if __name__ == "__main__":
    app.run(port=5000)