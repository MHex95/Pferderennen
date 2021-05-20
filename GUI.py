import Initialization as init
import Funktionen as fkt
import Pferde
import tkinter as tk


class Mainmenue(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.title = tk.Label(self, text="Hauptmenü", width=35)
        self.title.grid(row=0, column=0)

        self.spacer1 = tk.Label(self, text="")
        self.spacer1.grid(row=1, column=0)

        self.button_rennen = tk.Button(self, text="Zum Spiel", width=20)
        self.button_rennen.grid(row=2, column=0, columnspan=2, sticky="N")

        self.spacer2 = tk.Label(self, text="")
        self.spacer2.grid(row=3, column=0)

        self.button_markt = tk.Button(self, text="Pferdemarkt", width=20)
        self.button_markt.grid(row=4, column=0, columnspan=2, sticky="N")

        self.spacer3 = tk.Label(self, text="")
        self.spacer3.grid(row=5, column=0)

        self.button_end = tk.Button(self, text="Spiel beenden", width=20)
        self.button_end.grid(row=6, column=0, columnspan=2, sticky="N")

        self.spacer4 = tk.Label(self, text="")
        self.spacer4.grid(row=7, column=0)

