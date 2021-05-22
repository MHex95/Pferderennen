import Initialization as init
import Funktionen as fkt
import Pferde
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox


def abfrage_wette(pferd_auswahl, wettbetrag):
    tk.messagebox.askokcancel(title="")


def startgui(pferde):

    root = tk.Tk()
    root.title("Hauptmenü")

    mainmenue(root, pferde)

    root.mainloop()


def mainmenue(root, pferde):
    title_font = tkFont.Font(size=13)

    title = tk.Label(root, text="--Hauptmenü--", width=35, font=title_font)
    title.grid(row=0, column=0)

    button_rennen = tk.Button(root, text="Zum Spiel", width=20,
                              command=lambda: call_race(root, pferde, title_font))
    button_rennen.grid(row=2, column=0, columnspan=2, sticky="N")

    button_markt = tk.Button(root, text="Pferdemarkt", width=20)
    button_markt.grid(row=4, column=0, columnspan=2, sticky="N")

    button_end = tk.Button(root, text="Spiel beenden", width=20)
    button_end.grid(row=6, column=0, columnspan=2, sticky="N")

    # Abstand zwischen den Buttons
    for n in range(1, 8, 2):
        root.grid_rowconfigure(n, minsize=20)


def call_race(root, pferde, title_font):
    root.destroy()
    rframe = tk.Toplevel

    rframe.label = tk.Label(text="Wette platzieren",font=title_font, width=20)
    rframe.label.grid(row=0, column=0)

    teilnehmer = []
    c = 0
    for n in pferde:
        teilnehmer.append((n.name, c))
        c += 1

    pferd_auswahl = tk.IntVar()
    c = 1

    for text, auswahl in teilnehmer:
        radiobutton = tk.Radiobutton(text=text)
        radiobutton["variable"] = pferd_auswahl
        radiobutton["value"] = auswahl
        radiobutton.grid(row=c, column=0, sticky="W")
        c += 1



    label = tk.Label(text="Wettbetrag eingeben:")
    label.grid(row=c, column=0, pady=(10, 0))

    wettbetrag_entry = tk.Entry()
    wettbetrag_entry.grid(row=c+1, column=0, pady=(0, 15))

    wettbestätigung = tk.Button(text="Wette platzieren",
                                command=lambda: abfrage(teilnehmer, pferd_auswahl, wettbetrag_entry, rframe))

                                #print(teilnehmer[pferd_auswahl.get()][0],
                                      #wettbetrag_entry.get()))
    wettbestätigung.grid(row=c+2, column=0)


def abfrage(teilnehmer, pferd_auswahl, wettbetrag_entry, rframe):
    dialog = tk.messagebox. askokcancel(title="Wette bestätigen",
                                        message="Möchtest du {0} € auf {1} setzen?"
                                        .format(wettbetrag_entry.get(),
                                        teilnehmer[pferd_auswahl.get()][0]))

    if dialog is True:
        print("Das Rennen beginnt!")

    else:
        print("erneute Auswahl")