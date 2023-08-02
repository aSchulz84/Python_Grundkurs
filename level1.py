from abort import *
from inventar import *
from raum1 import *


def level1():
    spiel_laueft = True

    while spiel_laueft:
        time.sleep(2)
        print("")
        print("")
        print("")
        print("")
        print("    Sie befinden sich auf")
        print("==============================")
        print("            DECK 4")
        print("==============================")
        time.sleep(2)
        print("")
        print("")
        print("")
        print("")
        print("Sie sehen vor sich einen Flur, von welchem aus 4 Räume abgehen.")
        print("")

        eingabe = input(
            "Was möchsten Sie als nächstes tun?\n\n- In Raum [1] gehen\n- In Raum [2] gehen\n- In Raum [3] gehen\n- In Raum [4] gehen\n- Ihr [I]nventar anzeigen lassen\n- Die Mission [A]bbrechen\n\nWas möchten Sie tun?:   ")
        if eingabe.upper() == "A":
            abbrechen()  # funktioniert noch nicht wie gewünscht

        elif eingabe.upper() == "1":
            raum1()

        elif eingabe.upper() == "2":
            print("Hier wird raum2 Funktion eingepflegt")
            level1()  # Die beiden Zeilen dienen als Platzhalter

        elif eingabe.upper() == "3":
            print("Hier wird raum3 Funktion eingepflegt")
            level1()  # Die beiden Zeilen dienen als Platzhalter

        elif eingabe.upper() == "4":
            print("Hier wird raum4 Funktion eingepflegt")
            level1()  # Die beiden Zeilen dienen als Platzhalter

        elif eingabe.upper() == "I":
            inventarfunktion()


spiel_läuft = False
