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


def pferd_kaufen():
    # Pferde werden vorgestellt
    print("\n1: Quirrly Whirly")
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
            print("Dieses Pferd ist leider nicht verkäuflich")


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


def initialization(Pferd, Jockey):

    kontostand = 100
    level = 1
    erfahrung = 0
    spieler = Jockey("Spieler", level)

    spieler_stats = {"Spieler": spieler, "Level": level, "Erfahrung": erfahrung, "Balance": kontostand}

    pferde_liste = []
    jockey_liste = []

    # Pferde an den Start bringen
    jockey_eins = Jockey("Stefan Superschnell", 9)
    pferd_eins = Pferd(1, "Red Thunder", 9, jockey_eins)
    pferde_liste.append(pferd_eins)
    jockey_liste.append(jockey_eins)

    jockey_zwei = Jockey("Sebastian Sporenhart", 8)
    pferd_zwei = Pferd(2, "Brutus", 7, jockey_zwei)
    pferde_liste.append(pferd_zwei)
    jockey_liste.append(jockey_zwei)

    jockey_drei = Jockey("Peter Pusteblume", 4)
    pferd_drei = Pferd(3, "Mister Hüh", 6, jockey_drei)
    pferde_liste.append(pferd_drei)
    jockey_liste.append(jockey_drei)

    jockey_vier = Jockey("Holger Hinkelstein", 2)
    pferd_vier = Pferd(4, "Entchen", 4, jockey_vier)
    pferde_liste.append(pferd_vier)
    jockey_liste.append(jockey_vier)

    jockey_fünf = Jockey("Bernd Blindfisch", 1)
    pferd_fünf = Pferd(5, "Ist das etwa ein Stein?!", 1, jockey_fünf)
    pferde_liste.append(pferd_fünf)
    jockey_liste.append(jockey_fünf)

    return pferde_liste, jockey_liste, spieler_stats
