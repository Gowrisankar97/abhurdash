from flask import Flask, render_template, request
app = Flask(__name__)
import assess
import dataps
import mlpred

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
     symptoms=[dosha,dhatus,bala,desha,kaala,anala,saatmya,satva,rogakaala]


     doshas=assess.dosha(dosha)
     dhatus=assess.dhatus(dhatus)
     bala=assess.bala(bala)
     desha=assess.desha(desha)
     kaala=assess.kaala(kaala)
     anala=assess.anala(anala)
     saatmya=assess.saatmya(saatmya)
     satva=assess.satva(satva)
     rogakaala=assess.rogakaala(rogakaala)
     year=request.form.getlist("age")
     month=request.form.getlist("month")
     age=dataps.agecv(year[0],month[0])
     gender=request.form.getlist("Gender")
     walk=request.form.getlist("walk")
     speech=request.form.getlist("speech")
     limb=request.form.getlist("limb")
     eyec=request.form.getlist("eyec")
     response=request.form.getlist("response")
     hyper=request.form.getlist("hyper")
     activity=request.form.getlist("activity")
     concen=request.form.getlist("concen")
     headache=request.form.getlist("headache")
     conv=request.form.getlist("convolution")
     conv=dataps.sectomin(conv[0])
     mouth=request.form.getlist("mouth")
     itch=request.form.getlist("itch")
     ooz=request.form.getlist("ooz")
     lesion=request.form.getlist("lesion")
     milestone=request.form.getlist("milestone")
     feed=request.form.getlist("feed")
     neck=request.form.getlist("neck")
     sepsis=request.form.getlist("sepsis")
     respiratory=request.form.getlist("respiratory")
     eye=request.form.getlist("eye")
     body=request.form.getlist("body")
     jlimbs=request.form.getlist("jlimbs")
     fever=request.form.getlist("fever")
     delivery=request.form.getlist("delivery")

     dosv=dataps.doshavalues(list(doshas))

     mlinp=[age,int(gender[0]),int(walk[0]),int(speech[0]),int(limb[0]),int(eyec[0]),int(response[0]),int(hyper[0]),int(activity[0]),int(concen[0]),int(headache[0]),conv,int(mouth[0]),int(itch[0]),int(ooz[0]),int(lesion[0]),int(milestone[0]),"D","D","D",int(feed[0]),int(neck[0]),int(sepsis[0]),int(respiratory[0]),int(eye[0]),int(body[0]),int(jlimbs[0]),int(fever[0]),int(delivery[0])]
     print(mlinp)
     fmlinp=dataps.dosharp(mlinp,dosv)

     division = ["Sthaanika-Dosha", "Dhatus", "Bala", "Desha", "Kaala", "Anala", "Saatmya", "Satva", "Rogakaala"]
     creteria = [doshas, dhatus, bala, desha, kaala, anala, saatmya,satva,rogakaala]
     output=assess.assesform(division,creteria)
     output1=assess.symform(division,symptoms)
     diag,comm=mlpred.mlresult([fmlinp])
     nulltest = fmlinp
     nulltest.pop(0)
     nulltest.pop(0)
     if len(set(nulltest))>1:
      return render_template("result.html",division=output,symp=output1,result=diag,com=comm)
     else:
      return render_template("alert.html")
    else:
        dosha=['No Option','Enthusiasm',
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
 'Unconsciousness',
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
        dhatus=['No Option','Optimum nourishment',
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
        desha=['No Option',"Wetland","Normal","Dry land"]
        kaala=['No Option',"Less than 1 year old","1-2 years old",">2 years old"]
        bala=['No Option',"Cannot perform any activities","Can perform activities with difficulty","Can perform all activities"]
        anala=['No Option',"No hunger even after no intake","Moderate appetite","Extremely hungry after heavy food"]
        satva=['No Option',"Cries often","Difficult to comfort when hurt","Hurts others on purpose","Scared, Slow learner","Annoyed easily","Unfriendly with everyone","Friendly with strangers",
               "Cries reasonably","Can withstand little pain","Kind - hearted","Learn at normal pace","Disobedient at times","Hyperactive","Sleeps late","Choosy friends",
               "Brave, Withstand any pain","Strong,Fast learner","Obedient,Friendly with all"]
        saatmya=['No Option',"Prefers only specific taste","Doesn’t take dairy products","Prefers some tastes only",
"Prefers all taste of food and dairy products"]
        rogakaala=['No Option',"Symptoms occurred within a week","Symptoms persisting for a month","Symptoms persisting from months to years"]

        return render_template('input.html', doshas=dosha,dhatuss=dhatus,deshas=desha,kaalas=kaala,balas=bala,analas=anala,satvas=satva,saatmyas=saatmya,rogakaalas=rogakaala)
if __name__ == "__main__":
    app.run(port=5000)