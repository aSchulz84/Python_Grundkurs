from inventar import *
from quests import *


def raum1():

    while True:
        time.sleep(2)
        print("")
        print("")
        print("")
        print("")
        print("     Sie befinden sich in")
        print("==============================")
        print("            RAUM 1")
        print("==============================")
        time.sleep(2)
        print("")
        print("")
        print("")
        print("")
        print("Wie Sie sehen, befinden sich hier ein Kühlschrank und ein Schreibtisch.")
        time.sleep(2)
        print("")
        eingabe = input(
            "Was möchten Sie als nächstes tun?\n\n- Den [K]ühlschrank öffnen\n- Die [S]chreibtisch Schublade öffnen\n- [Z]urück in den Flur gehen\n\nEingabe:   ")
        if eingabe.upper() == "K":
            kuehlschrank()
        elif eingabe.upper() == "S":
            print("Hier wird schreibtisch() Funktion eingepflegt")
            raum1()  # Die beiden Zeilen dienen als Platzhalter
        elif eingabe.upper() == "Z":
            break
