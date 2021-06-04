import tkinter as tk
from tkinter import messagebox


class MainMenue(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.button_rennen = tk.Button(self, text="New Window", width=20,
                                       command=self.call_bet)
        self.button_rennen.pack()

    def call_bet(self):
        # `self.master` is the window
        Bet = BetFrame(self.master)
        Bet.pack()
        self.destroy()


class BetFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # You need to tell the button that its master should be this BetFrame
        # If you don't it will assume you mean the window so
        # `self.destroy()` isn't going to destroy the button.
        self.button = tk.Button(self, text="Wette platzieren", command=self.question)
        self.button.pack()

    def question(self):
        dialog = tk.messagebox.askokcancel(message="Destroy Window?")

        if dialog is True:
            self.destroy()

def main():
    root = tk.Tk()

    Menue = MainMenue(root)
    Menue.pack()

    root.mainloop()


main()

