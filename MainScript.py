import GUI as app
import Initialization as init
import Funktionen as fkt
import Pferde
import tkinter as tk


def main():
    pferde_teilnahme, pferde_reserve, jockey_liste, spieler_stats, teilnehmer = \
        init.initialization(Pferde.Pferd, Pferde.Jockey)

    app.startgui(pferde_teilnahme)

main()