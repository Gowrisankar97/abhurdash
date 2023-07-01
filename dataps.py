import  math
def doshavalues(vv):
    dv=[0,0,0]
    for v in vv:
        vata=["Vata-samaa","Vata-vrriddhi","Vata-kshaya"]
        pitta=["Pitta-samaa","Pitta-kshaya","Pitta-vriddhi"]
        kappa=["Kapha-samaa","Kapha-kshaya","Kapha-vriddhi"]
        if str(v) in vata:
             dv[0]=1
        elif str(v)in pitta:
             dv[1]=1
        elif str(v) in kappa:
             dv[2]=1
    return dv

def agecv(a,m):
   age = float(str(a) + "." + str(m))

   if int(m)<=6:
       a =float(math.floor(age))
   else:
       a =float(math.ceil(age))

   return a

def sectomin(s):
    minutes=int(s)/60
    minutes=round(minutes,2)
    return minutes



def dosharp(ds,rp):
    nw=ds
    ind=0
    for i in range(0,len(nw)):
        if nw[i]=="D":
            nw[i]=rp[ind]
            ind=ind+1



    print(nw)
    return nw



