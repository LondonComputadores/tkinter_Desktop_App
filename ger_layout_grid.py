
from tkinter import *

janela = Tk()
janela.title("Row and Column")
janela ["bg"] = "pink"
janela.geometry("1100x700+100+40")

lb1 = Label(janela, text="Label 1")
lb1.grid(row=1000, column=1000)

lb2 = Label(janela, text="Label 2")
lb2.grid(row=2000, column=2000)

janela.mainloop()