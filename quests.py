from inventar import *


# kuehlen = True
# schreiben = True


def kuehlschrank():

    time.sleep(2)
    print("")
    print("")
    print("")
    print("")
    print("Sie schauen in das Hauptfach des Kühlschranks")
    time.sleep(2)
    print("")
    print("Dieses ist leer")
    time.sleep(2)
    print("")
    while True:
        eingabe = input(
            "Möchten Sie in das Eisfach des Kühlschranks sehen?\n\n- [E]isfach öffnen\n- [N]icht öffnen\n\nEingabe:   ")
        time.sleep(3)
        if eingabe.upper() == "E":
            if "Aspirin" in medizin:
                print("")
                print("Das Eisfach ist leer.")
                time.sleep(3)
                break
            else:
                print("Im Eisfach befindet sich eine Packung Aspirin")
                medizin.append("Aspirin")
                print("")
                print("Sie packen sich die Apsirin in Ihre Medizin-Tasche")
                time.sleep(3)
                print("")
                print("Sie haben aktuell die folgende Medizin:")
                print("")
                print("==============================")
                print('\n'.join(map(str, medizin)))
                print("==============================")
                print("")
                time.sleep(5)
                print("")
                print("")
                print("")
                print("")
                break
        elif eingabe.upper() == "N":
            break
