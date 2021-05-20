import GUI as app
import Initialization as init
import Funktionen as fkt
import Pferde
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Pferderennen by Martin")
    root.resizable(False, False)
    Hauptfenster = app.Mainmenue(root)
    Hauptfenster.pack()

    root.mainloop()


main()