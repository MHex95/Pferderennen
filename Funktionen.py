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

    lustige_beschreibungen = ["Bewegt sich schnell, läuft aber langsam",
                              "Zumindest ist er schön",
                              "War Champion in den 0er Jahren, hat aber die besten Zeiten hinter sich",
                              "Ein furchteinflößendes Tier, ein böser Blick und manch Gegner erstarrt",
                              "Was machen die Chinesen bloß mit ihren Tieren?!"]
    for n in marktliste:
        print()
        print(n.name)
        preise = []
        preis = (count + 1) ** 2 * 200
        preise.append(preis)
        print("Preis:", preis)
        print(lustige_beschreibungen[count])

        count += 1
