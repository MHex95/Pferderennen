def pferd_auswählen(pferde):
    while True:
        try:
            nummer_pferd = int(input("\nAuf welches Pferd wird gesetzt?: "))

        except ValueError:
            print("Eingabe ungültig!")
            continue

        if nummer_pferd > len(pferde) or nummer_pferd < 1:
            print("Dieses Pferd gibt es nicht!")

        else:
            break

    return nummer_pferd


def wetteinsatz(kontostand):
    while True:
        try:
            print("Ihr Kontostand: {0:.2f}".format(kontostand))
            betrag = float(input("Der Wetteinsatz: "))

        except ValueError:
            print("Eingabe ungültig!")
            continue

        if betrag > kontostand:
            print("So viel Geld besitzen Sie nicht!")

        else:
            return betrag


def pferdemarkt(marktliste):
    count = 0
    for n in marktliste:
        print("\n", n.name)
        preise = []
        preis = (count + 1) ** 2 * 200
        preise.append(preis)
        print(preis)
        print("irgendwas lustiges")

        count += 1


    # Pferde werden vorgestellt
    '''print("\n1: Quirrly Whirly")
    preis1 = 200
    print("Preis: {0} €".format(preis1))
    print("Bewegt sich schnell, läuft aber langsam")

    print("\n2: Ross Anthony")
    preis2 = 1000
    print("Preis: {0} €".format(preis2))
    print("Zumindest ist er schön")

    print("\n3: Grand Grey")
    preis3 = 5000
    print("Preis: {0} €".format(preis3))
    print("War Champion in den 0er Jahren, hat die besten Zeiten hinter sich")

    print("\n4: Streitross")
    preis4 = 10000
    print("Preis: {0} €".format(preis4))
    print("Ein furchteinflößendes Tier, ein böser Blick und manch Gegner erstarrt")

    print("\n5: Chinesisches Pferd")
    preis5 = 100000
    print("Preis: {0}".format(preis5))
    print("Was machen die Chinesen bloß mit ihren Tieren?!")

    print("\nzum Abbrechen 0 wählen")

    while True:
        try:
            kauf_wahl = int(input("\nwelches Pferd möchten Sie kaufen? "))

        except ValueError:
            print("Ungültige Eingabe!")
            continue

        if 5 >= kauf_wahl >= 0:
            return kauf_wahl
        else:
            print("Dieses Pferd ist leider nicht verkäuflich")'''


def menu():
    # Ausgabe des Menüs:
    #
    while True:
        print("\n---------------------")
        print("Menü:")
        print("(Z)um Rennen")
        print("(P)ferdemarkt")
        print("(B)eenden")

    # Gewünschten Menüpunkt abfragen
    #
        auswahl = input("Deine Wahl: ")

        if auswahl == 'z' or auswahl == 'Z' or auswahl == 'b' or auswahl == 'B' or auswahl == 'p' or auswahl == 'P':
            return auswahl

        else:
            print('ungültige Eingabe')

