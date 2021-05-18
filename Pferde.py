from random import randint
from math import sqrt


class Konto:
    def __init__(self, kontostand):
        self.kontostand = kontostand


class Jockey:
    def __init__(self, name, können):
        self.name = name
        self.können = können

    def zeige_jockey(self):
        print("Der Name des Jockeys:", self.name)


class Pferd:
    def __init__(self, startnummer, name, schnelligkeit, jockey):
        self.startnummer = startnummer
        self.name = name
        self.schnelligkeit = schnelligkeit
        self.jockey = jockey
        self.glück = None
        self.pech = None
        self.zeit = None

    def __str__(self):
        return "{0}: {1:.2f}".format(self.name, self.zeit)

    def berechne_quote(self, jockey):
        quote = 155 / (self.schnelligkeit + jockey.können) ** 1.5
        print("Quote: 1:{0:.2f}".format(quote))
        return quote

    def zeige_daten(self):
        print("\nPferd Nummer", self.startnummer, ":")
        print("Der Name des Pferdes: ", self.name)
        Jockey.zeige_jockey(self.jockey)
        self.berechne_quote(self.jockey)
        self.glück = randint(0, 20)
        self.pech = randint(0, 20)
        if self.glück > 16:
            print("------------------")
            print("{0} scheint heute gut drauf zu sein!".format(self.name))

    def rennen(self):
        strecke = 2500
        geschwindigkeit = (self.schnelligkeit + self.jockey.können) * 2 + 2 * self.glück + 2 * self.pech
        self.zeit = strecke / geschwindigkeit
        #print("Zeit {0}: {1:.2f}".format(self.name, self.zeit))
        return self.zeit

    def siegerehrung(self, reihenfolge, auswahl_pferd, betrag, wettkonto):
        if self == reihenfolge[0]:
            sieger = self.startnummer
            print("\nDer Sieger ist Pferd Nummer: {0}, '{1}'".format(self.startnummer, self.name))
            input()

            if auswahl_pferd == sieger:
                gewinn = betrag * self.berechne_quote(self.jockey)
                print("\nGewonnen! Sie erhalten {0:.2f} €".format(gewinn))
                wettkonto.kontostand += gewinn

                print("Kontostand: {0:.2f}".format(wettkonto.kontostand))

            else:
                print("Kontostand: {0:.2f}".format(wettkonto.kontostand))

            if sieger == 6:
                print("Ihr Pferd Gewinnt")
                wettkonto.kontostand += 500
                print("Kontostand: {0:.2f}".format(wettkonto.kontostand))
