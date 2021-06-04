import GUI as app
import Initialization as init
import Funktionen as fkt
import Pferde
import tkinter as tk


def main():
    pferde_teilnahme, pferde_reserve, jockey_liste, spieler_stats, teilnehmer = \
        init.initialization(Pferde.Pferd, Pferde.Jockey)

    root = tk.Tk()
    root.title("Pferderennen by Martin Heuer")

    hauptmenue = app.Mainmenue(root, pferde_teilnahme)
    hauptmenue.grid(row=0, column=0)

    root.mainloop()

    wettbetrag = hauptmenue.Bet.wettbetrag
    print(wettbetrag)


main()
