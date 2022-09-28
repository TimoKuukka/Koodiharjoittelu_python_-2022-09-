#!/usr/bin/env python
# Tämä on aloitusskripti

import henkilö
import vuodet



def pääfunktio():
    syntymävuosi = 1970
    aliisa = henkilö.Henkilö("Aliisa", 1980)
    bob = henkilö.Henkilö(nimi="Bob", syntymävuosi=1967)
    henkilöt = [aliisa, bob]
    
# dictionary - sanakirja

henkilötiedot = [
    {"nimi": "Aliisa", "syntymävuosi": 1980},
    {"nimi": "Bob", "syntymävuosi": 1967},
    {"nimi": "Cecilia", "syntymävuosi": 1920},
]

henkilöiden_lempivärit  = {
    "Aliisa": "musta",
    "Bob": "sininen"
    }

henkilöiden_lemmikit = {
        "Aliisa": ["Musti"],
        "Bob": ["Rekku", "Nimi2"]
    }

def henkilölistaus():
    henkilöt = []
    for ht in henkilötiedot:
        h = henkilö.Henkilö(ht["nimi"], ht["syntymävuosi"])
        henkilöt.append(h)
    

    for h in henkilöt:
        print(f"{h.nimi:10} (s. {h.syntymävuosi})")
        print(f"{h.nimi:10} on {h.ikä()} vuotta vanha.")
        lemmikit = henkilöiden_lemmikit.get(h.nimi, [])
        for lemmikki in lemmikit:
            print("lemmikki:", lemmikki)
        try:
            print("lempiväri:", henkilöiden_lempivärit[h.nimi])
        except KeyError:
            print("Ei lempiväriä tiedossa")
        print("-")

henkilölistaus()

def pääfunktio():
    i = 0
    while True:
        i += 1
        print("moi!", i)
        if i > 7:
            break
        if i > 5:
            print("iso on")

    print("---------------")
    

    print(aliisa.nimi)
    print(aliisa.syntymävuosi)

    print("kutsutaan henkilötiedot-funktiota")
    lempiväri = henkilöiden_lempivärit["Bob"]
    paluuarvo = bob.tiedot(lempiväri=lempiväri)
    print("palattiin funktiosta, paluuarvo:", paluuarvo)
    print("Joku syntymävuosi", syntymävuosi)




#pääfunktio()


# teksti = input("Anna luku: ") # input = funktio

# print(teksti) # print = funktio

# if teksti.isdigit(): # isdigit = str luokan metodi (method of str class)
#     luku = int(teksti)
# elif teksti == "yksi":
#     luku = 1
# elif teksti == "kaksi":
#     luku = 2
# else:
#     luku = 0
#     print("Ei ollut luku. Varmaan 0 käy sitten.")

# print("Luku on:", luku)

# if luku > 10:
#      print("Suurempi kuin 10")
# elif luku == 10:
#     print("Tasan 10")
# else:
#      print("Pienempi kuin 10")