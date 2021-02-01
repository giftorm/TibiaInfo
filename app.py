import os
import tkinter
from tkinter import ttk
from ttkthemes import ThemedStyle
from tibiawiki.Creatures import Creatures

def main():
    root = tkinter.Tk()
    root.title("TibiaInfo")
    icon = tkinter.PhotoImage(file='icon.png')


    root.geometry("800x600")
    root.iconphoto(False, icon)

    style = ThemedStyle(root)
    style.set_theme("equilux")
    root.configure(background = "#414141")
    label = tkinter.Label(text="Hello , world!")
    label.configure(background = "#414141")
    label.pack()

    data = Creatures()
    creature_list = data.list()

    root.mainloop()


if __name__ == "__main__":
    main()
