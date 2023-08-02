
from abort import *
import time


waffen = ["Taschenmesser",]
schluessel = []
medizin = ["Pflaster",]


def inventarfunktion():

    while True:
        print("")
        print("")
        print("")
        print("")
        print("==============================")
        print("           Inventar")
        print("==============================")
        time.sleep(1)
        print("")
        print("")
        print("")
        print("")
        eingabe = input(
            "\n Welche Gegenstände wollen Sie prüfen??\n\n- [W]affen\n- [S]chlüssel\n- [M]edizin\n- [Z]urück zur Mission\n\nWas möchten Sie tun?:   ")
        if eingabe.upper() == "A":
            abbrechen()

        elif eingabe.upper() == "W":
            if len(waffen) == 0:
                print("")
                print("Waffen:")
                print("")
                print("==============================")
                print("Sie haben noch keine Waffen!")
                print("==============================")
                print("")
                time.sleep(5)
            else:
                print("")
                print("Sie haben aktuell die folgenden Waffen:")
                print("")
                print("==============================")
                print('\n'.join(map(str, waffen)))
                print("==============================")
                print("")
                time.sleep(5)

        elif eingabe.upper() == "S":
            if len(schluessel) == 0:
                print("")
                print("Schlüssel:")
                print("")
                print("===============================")
                print("Sie haben noch keine Schlüssel!")
                print("===============================")
                print("")
                time.sleep(5)
            else:
                print("")
                print("Sie haben aktuell die folgenden Schlüssel:")
                print("")
                print("==============================")
                print('\n'.join(map(str, schluessel)))
                print("==============================")
                print("")
                time.sleep(5)
        elif eingabe.upper() == "M":
            if len(medizin) == 0:
                print("")
                print("Medizin:")
                print("")
                print("==============================================")
                print("Sie haben noch keine medizinischen Utensilien!")
                print("==============================================")
                print("")
                time.sleep(5)
            else:
                print("")
                print("Sie haben aktuell die folgenden medizinischen Utensilien:")
                print("")
                print("==============================")
                print('\n'.join(map(str, medizin)))
                print("==============================")
                print("")
                time.sleep(5)

        elif eingabe.upper() == "Z":
            break
