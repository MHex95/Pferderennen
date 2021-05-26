import tkinter as tk
from tkinter import messagebox


def main():

    root = tk.Tk()
    root.title("Hauptmenü")

    mainmenue(root)

    root.mainloop()


def mainmenue(root):
    button_rennen = tk.Button(root, text="New Window", width=20,
                              command=lambda: call_window(root))
    button_rennen.pack()


def call_window(root):
    root.destroy()
    rframe = tk.Tk()

    button = tk.Button(text="Wette platzieren",
                            command=lambda: question(rframe))

    button.pack()


def question(rframe):
    dialog = tk.messagebox.askokcancel(message="Destroy Window?")


    if dialog is True:
        rframe.destroy()


main()

