import joblib
import os
os.chdir("C://Users//gowrisankar//PycharmProjects//abhurdash//pkl")

def mlpredict(v):
    result=[]
    forest=joblib.load('modelrf.pkl')
    logistic=joblib.load('modellr.pkl')
    ridge=joblib.load('modelridge.pkl')

    p1=forest.predict(v)+1
    p2=logistic.predict(v)+1
    p3=ridge.predict(v)+1
    result.append(p1)
    result.append(p2)
    result.append(p3)

    print(result)

    return result,p1



def resulteva(r,p1):
    dg=0
    scode=0
    r=max(r)
    if r==p1:
        dg=r
    elif r!=p1:
        dg=p1
        scode=1
    else:
        scode=2


    return dg,scode


def rprocess(r,sc):
    comment="Results From Three Model"
    diag="Not Predicted"
    r=list(r)
    if int(r[0])==1:
        diag="Pangu"
    elif int(r[0])==2:
        diag="Unmada"
    elif int(r[0])==3:
        diag="Sarvanga vata"
    elif int(r[0])==4:
        diag="Apasmara"
    elif int(r[0])==5:
        diag="Vicharchika Kushta"

    if sc==1:
        comment="Result from one model"
    elif sc==2:
        comment="Model Not able to Predict"

    return diag,comment


def mlresult(inp):
    r,p=mlpredict(inp)
    dg,code=resulteva(r,p)
    diag,com=rprocess(dg,code)

    return diag,com




""""test=[[3.0,
  1.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  1.0,
  0.0,
  0.0,
  0.0,
  0.0,
  1.0,
  1.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0]]"""
#ty,p1=mlresult(test)