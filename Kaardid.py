from itertools import compress, product, combinations
import random
from random import sample

mängijaAlustab = True #True, kui alustab mängija, false kui robot.
loobunud = [False, False]
mastid = ["d", "s", "c", "h"] # d = ruutu, s = poti, c = risti, h = ärtu
kaardid = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
punktid = {
    "mängija": 99,
    "vastane": 99,
    "pangas": 2}

kaardipakk = []
for kaart in kaardid:
    for mast in mastid:
        mastikaart = kaart+mast
        kaardipakk.append(mastikaart)

def sega(kaardid):
    mängijaKäsi = []
    kuldkalaKäsi = []
    ühiskaardid = []
    for i in range(3):
        random.shuffle(kaardid)
    for i in range(2):
        mängijaKäsi.append(kaardid.pop())
        kuldkalaKäsi.append(kaardid.pop())
    for i in range(3):
        ühiskaardid.append(kaardid.pop())
    
    return kaardid, mängijaKäsi, kuldkalaKäsi, ühiskaardid

segatudPakk, mängijaKäsi, kuldkalaKäsi, ühiskaardid = sega(kaardipakk)

def uusKaart(segatudPakk, ühiskaardid):
    uusKaart = segatudPakk.pop()
    print("Lauale tuleb uus kaart: ",uusKaart)
    ühiskaardid.append(uusKaart)
    return segatudPakk, ühiskaardid
    
def panustamisVoor(ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud):
    print("Laual on:",ühiskaardid,". Pangas on hetkel",punktid["pangas"],"punkti.")
    if punktid["mängija"] == 0 or punktid["vastane"] == 0:
        if(len(ühiskaardid) < 5):
            segatudPakk, ühiskaardid = uusKaart(segatudPakk, ühiskaardid)
            print("Laual on:",ühiskaardid,". Pangas on hetkel",punktid["pangas"],"punkti.")
        return ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud        
    if mängijaAlustab: #mängija alustab
        käigulõpp = False
        mängijaTegevus = input("Kas soovid passida(X) või panustada(B)? ")
        while not (mängijaTegevus == "X" or mängijaTegevus == "B"):
            mängijaTegevus = input("Ei saanud aru. Kas soovid passida(X) või panustada(B)?")
            
        if mängijaTegevus == "X": #Mängija passib
            print("Mängija passib.")
            robotiTegevus = robotiKäik(mängijaTegevus, ["X"])
            if robotiTegevus == "X": #Robot passib järgi
                print("Vastane passib.")
                if(len(ühiskaardid) < 5):
                    segatudPakk, ühiskaardid = uusKaart(segatudPakk, ühiskaardid)
                return ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud
                
        else: #mängija panustab
            mängijapunkte = punktid["mängija"]
            panus = panusta(mängijapunkte, 1)
            punktid["mängija"] -= panus
            punktid["pangas"] += panus
            print("Mängija panustab",panus,"punkti.")
            robotiTegevus = robotiKäik(mängijaTegevus, ["C", "F"])
            if robotiTegevus == "F":
                print("Vastane loobub.")
                loobunud[1] = True
                pank = punktid["pangas"]
                punktid["pangas"] -= pank
                punktid["mängija"] += pank
                return ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud
            elif robotiTegevus == "C":
                print("Vastane maksab")
                punktid["vastane"] -= panus
                punktid["pangas"] += panus
                if(len(ühiskaardid) < 5):
                    segatudPakk, ühiskaardid = uusKaart(segatudPakk, ühiskaardid)
                return ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud
    
def panusta(maxPunkte, minpanus):
    strPanus = input("Sisesta panuse/tõste suurus. Lubatud panuse suurus "+str(minpanus)+" kuni "+str(maxPunkte)+": ")
    panus = 0
    while not is_integer(strPanus):
        strPanus = input("Ei saanud aru. Lubatud panuse suurus"+str(minpanus)+" kuni "+str(maxPunkte)+": ")
    if(is_integer(strPanus)):
        panus = int(strPanus)
        if (panus < 1 or panus > maxPunkte) and panus >= minpanus :
            print("Negatiivne arv või sul ei ole piisavalt punkte")
            panusta(maxPunkte, minpanus)
    return panus
                
#Leitud siit: https://note.nkmk.me/en/python-check-int-float/
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
    

def robotiKäik(mängijaTegevus, valikud): ## TODO
    if mängijaTegevus == "X":
        return "X"
    else:
        return random.choice(valikud)

def mäng(ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud, mängijaKäsi):
    voor = 0
    lõpeta = False
    while lõpeta == False and not(punktid["mängija"] == 0 or punktid["vastane"] == 0):        
        while voor < 3 and (True not in loobunud):
            print("mängijal on:",mängijaKäsi)
            panustamisVoor(ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud)
            voor += 1
        #SIIA LÄHEB KÄTE TUVASTUS
        print("Seis käe lõpus: ",punktid)
        if(punktid["mängija"] == 0 or punktid["vastane"] == 0):
            print("\nLõpptulemus:",punktid)
            return
        küsimus = input("Kas mängime veel ühe käe? (JAH) või (EI): ")
        while küsimus.lower() not in ["jah", "ei"]:
            küsimus = input("Kas mängime veel ühe käe? (JAH) või (EI): ")
        if küsimus.lower() == "ei":
            lõpeta = True
        voor = 0
        segatudPakk, mängijaKäsi, kuldkalaKäsi, ühiskaardid = sega(kaardipakk)
        
mäng(ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud, mängijaKäsi)
      