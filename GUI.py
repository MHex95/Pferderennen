import Initialization as init
import Funktionen as fkt
import Pferde
import tkinter as tk
import tkinter.font as tkFont


def abfrage_wette(pferd_auswahl, wettbetrag):
    tk.messagebox.askokcancel(title="")




class Mainmenue(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.title_font = tkFont.Font(size=13)

        self.title = tk.Label(self, text="--Hauptmenü--", width=35, font=self.title_font)
        self.title.grid(row=0, column=0)

        self.button_rennen = tk.Button(self, text="Zum Spiel", width=20, command=self.call_race)
        self.button_rennen.grid(row=2, column=0, columnspan=2, sticky="N")

        self.button_markt = tk.Button(self, text="Pferdemarkt", width=20)
        self.button_markt.grid(row=4, column=0, columnspan=2, sticky="N")

        self.button_end = tk.Button(self, text="Spiel beenden", width=20)
        self.button_end.grid(row=6, column=0, columnspan=2, sticky="N")

        # Abstand zwischen den Buttons
        for n in range(1, 8, 2):
            self.grid_rowconfigure(n, minsize=20)

    def call_race(self):
        self.destroy()
        raceframe = tk.Toplevel

        raceframe.label = tk.Label(text="Wette platzieren", font=self.title_font, width=20)
        raceframe.label.grid(row=0, column=0)

        Teilnehmer = [("Pferd 1", 0), ("Pferd 2", 1), ("Pferd 3", 2)]

        pferd_auswahl = tk.IntVar()
        c = 1

        for text, auswahl in Teilnehmer:
            radiobutton = tk.Radiobutton(text=text)
            radiobutton["variable"] = pferd_auswahl
            radiobutton["value"] = auswahl
            radiobutton.grid(row=c, column=0)
            c += 1

        wettbetrag_entry = tk.Entry()
        wettbetrag_entry.grid(row=c+1, column=0)

        wettbestätigung = tk.Button(text="Wette platzieren",
                                    command=lambda: print(Teilnehmer[pferd_auswahl.get()][0]))
        wettbestätigung.grid(row=c+2, column=0)