from itertools import compress, product, combinations
import random
from random import sample

mastid = ["d", "s", "c", "h"] # d = ruutu, s = poti, c = risti, h = ärtu
kaardid = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

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
print("flop on:",ühiskaardid)


#def jaga(kaardipakk):
#    for i in range(0,4,2):
#        mängijaKäsi.append(kaardipakk[i])
#        kuldkalaKäsi.append()
        