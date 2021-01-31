import tkinter
from tibiawiki import Creatures

def main():
    window = tkinter.Tk()

    label = tkinter.Label(text="Hello , wordl!", background="red")
    label.pack()

    data = Creatures.Creatures()
    creature_list = data.list()

    window.mainloop()



if __name__ == "__main__":
    main()