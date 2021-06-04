import Initialization as init
import Funktionen as fkt
import Pferde
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox


def abfrage_wette(pferd_auswahl, wettbetrag):
    tk.messagebox.askokcancel(title="")



class Mainmenue(tk.Frame):
    def __init__(self, parent, pferde):
        super().__init__(parent)

        self.title_font = tkFont.Font(size=13)

        self.titlelabel = tk.Label(self, text="--Hauptmenü--", width=35, font=self.title_font)
        self.titlelabel.grid(row=0, column=0)

        self.button_rennen = tk.Button(self, text="Zum Spiel", width=20,
                                  command=lambda: self.call_bet(pferde))
        self.button_rennen.grid(row=2, column=0, columnspan=2, sticky="N")

        self.button_markt = tk.Button(self, text="Pferdemarkt", width=20)
        self.button_markt.grid(row=4, column=0, columnspan=2, sticky="N")

        self.button_end = tk.Button(self, text="Spiel beenden", width=20)
        self.button_end.grid(row=6, column=0, columnspan=2, sticky="N")

        # Abstand zwischen den Buttons
        for n in range(1, 8, 2):
            self.grid_rowconfigure(n, minsize=20)

    def call_bet(self, pferde):
        # `self.master` is the window
        self.Bet = BetFrame(self.master, pferde)
        self.Bet.grid(row=0, column=0)
        self.destroy()


class BetFrame(tk.Frame):
    def __init__(self, parent, pferde):
        super().__init__(parent)

        self.title_font = tkFont.Font(size=13)

        self.label = tk.Label(text="Wette platzieren", font=self.title_font, width=20)
        self.label.grid(row=0, column=0)

        self.teilnehmer = []
        c = 0
        for n in pferde:
            self.teilnehmer.append((n.name, c))
            c += 1

        self.pferd_auswahl = tk.IntVar()
        c = 1

        for text, auswahl in self.teilnehmer:
            self.radiobutton = tk.Radiobutton(text=text)
            self.radiobutton["variable"] = self.pferd_auswahl
            self.radiobutton["value"] = auswahl
            self.radiobutton.grid(row=c, column=0, sticky="W")
            c += 1

        self.label = tk.Label(text="Wettbetrag eingeben:")
        self.label.grid(row=c, column=0, pady=(10, 0))

        self.wettbetrag_entry = tk.Entry()
        self.wettbetrag_entry.grid(row=c + 1, column=0, pady=(0, 15))

        self.wettbestätigung = tk.Button(text="Wette platzieren",
                                    command=self.abfrage)

        # print(teilnehmer[pferd_auswahl.get()][0],
        # wettbetrag_entry.get()))
        self.wettbestätigung.grid(row=c + 2, column=0)

        self.wettbetrag = self.wettbetrag_entry.get()

    def abfrage(self):
        dialog = tk.messagebox.askokcancel(title="Wette bestätigen",
                                               message="Möchtest du {0} € auf {1} setzen?"
                                               .format(self.wettbetrag_entry.get(),
                                                       self.teilnehmer[self.pferd_auswahl.get()][0]))

        if dialog is True:
            print("Das Rennen beginnt!")
            self.master.destroy()

        else:
            print("erneute Auswahl")