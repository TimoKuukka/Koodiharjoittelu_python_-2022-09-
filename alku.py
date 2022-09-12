
# Tämä on aloitusskriptiggg

import henkilö
import vuodet



def pääfunktio():
    syntymävuosi = 1970
    aliisa = henkilö.Henkilö("Aliisa", 1980)
    bob = henkilö.Henkilö(nimi="Bob", syntymävuosi=1967)
    
    print(aliisa.nimi)
    print(aliisa.syntymävuosi)

    print("kutsutaan henkilötiedot-funktiota")
    paluuarvo = bob.tiedot(lempiväri="punainen")
    print("palattiin funktiosta, paluuarvo:", paluuarvo)
    print("Joku syntymävuosi", syntymävuosi)

    print(aliisa.ikä())




pääfunktio()


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