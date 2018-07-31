
from tkinter import *

janela = Tk()
janela.title("Clinica Conde")
janela ["bg"] = "pink"
janela.geometry("1100x700+100+40")

lb1 = Label(janela, text="horizontal", bg="light blue")
lb1.pack(side=TOP, fill=X)

lb2 = Label(janela, text="", bg="black")
lb2.pack(side=LEFT, fill=Y)

lb3 = Label(janela, text="", bg="black")
lb3.pack(side=RIGHT, fill=Y)

janela.mainloop()