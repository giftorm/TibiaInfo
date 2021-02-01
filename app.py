import os
from tkinter import *
from tkinter.ttk import *
from tibiawiki.Creatures import Creatures

def main():
    root = Tk()
    root.title("TibiaInfo")
    icon = PhotoImage(file='icon.png')
    root.geometry("800x600")
    root.iconphoto(False, icon)

    label = Label(text="Hello , wordl!", background="red")
    label.pack()

    data = Creatures()
    creature_list = data.list()

    root.mainloop()



if __name__ == "__main__":
    main()