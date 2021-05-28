import tkinter as tk
from tkinter import messagebox


def main():

    root = tk.Tk()
    root.title("Hauptmenü")

    Menue = MainMenue(root)
    Menue.pack()

    root.mainloop()


class MainMenue(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.button_rennen = tk.Button(self, text="New Window", width=20, command=lambda: call_bet(self))
        self.button_rennen.pack()

        def call_bet(root):
            root.destroy()
            broot = tk.Tk()

            Bet = BetFrame(broot)
            Bet.pack()


class BetFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.button = tk.Button(text="Wette platzieren",
                           command=lambda: question(self))

        self.button.pack()


        def question(rframe):
            dialog = tk.messagebox.askokcancel(message="Destroy Window?")

            if dialog is True:
                rframe.destroy()


main()

