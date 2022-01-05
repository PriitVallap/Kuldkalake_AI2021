from itertools import compress, product, combinations
import random
from random import sample

mängijaAlustab = True #True, kui alustab mängija, false kui robot.
loobunud = [False, False]
mastid = ["d", "s", "c", "h"] # d = ruutu, s = poti, c = risti, h = ärtu
kaardid = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
punktid = {
    "mängija": 100,
    "vastane": 100,
    "pangas": 0}

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
print("mängijal on:",mängijaKäsi)
print("vastasel on:",kuldkalaKäsi)

def panustamisVoor(ühiskaardid, segatudPakk, mängijaAlustab, punktid, loobunud):
    print("Laual on:",ühiskaardid,". Pangas on hetkel",punktid["pangas"],"punkti.")
    if mängijaAlustab:
        käigulõpp = False
        mängijaTegevus = input("Kas soovid passida(X) või panustada(B)? ")
        while not (mängijaTegevus == "X" or mängijaTegevus == "B"):
            mängijaTegevus = input("Ei saanud aru. Kas soovid passida(X) või panustada(B)?")
            print(mängijaTegevus)
            
        if mängijaTegevus == "X":
            print("Mängija passib.")
            robotiTegevus = robotiKäik()
            if robotiTegevus == "X":
                print("Vastane passib.")
                if(len(ühiskaardid) < 5):
                    uusKaart = segatudPakk.pop()
                    print("Lauale tuleb uus kaart: ",uusKaart)
                    ühiskaardid.append(uusKaart)
                return ühiskaardid, segatudPakk, mängijaAlustab, punktid
        else:
            mängijapunkte = punktid["mängija"]
            panus = panusta(mängijapunkte)
            print(panus)
            punktid["mängija"] -= panus
            punktid["pangas"] += panus
            print(punktid)
            
    else:
        robotiTegevus = robotiKäik() ## TODO
        if robotiTegevus == "X":
            print("Vastane passib.")
        elif robotiTegevus == "B":
            robotiPanus        

def panusta(maxPunkte):
    strPanus = input("Sisesta panuse suurus. Lubatud panuse suurus 1 kuni "+str(maxPunkte)+": ")
    panus = 0
    while not is_integer(strPanus):
        strPanus = input("Ei saanud aru. Lubatud panuse suurus 1 kuni "+str(maxPunkte)+": ")
    if(is_integer(strPanus)):
        panus = int(strPanus)
        if panus < 1 or panus > maxPunkte :
            print("Negatiivne arv või sul ei ole piisavalt punkte")
            panusta(maxPunkte)

    print(panus)
    return panus
                
#Leitud siit: https://note.nkmk.me/en/python-check-int-float/
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
    

def robotiKäik(): ## TODO
    return "X"

def mäng(ühiskaardid, segatudPakk, mängijaAlustab, punktid):
    panustamisVoor(ühiskaardid, segatudPakk, mängijaAlustab, punktid);
    panustamisVoor(ühiskaardid, segatudPakk, mängijaAlustab, punktid);
    panustamisVoor(ühiskaardid, segatudPakk, mängijaAlustab, punktid);
    
mäng(ühiskaardid, segatudPakk, mängijaAlustab, punktid)
      