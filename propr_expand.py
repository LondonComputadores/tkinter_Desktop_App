from tkinter import *

janela = Tk()
janela.title("Clinica Conde")
janela ["bg"] = "pink"
janela.geometry("1100x700+100+40")


lb1 = Label(janela, text="linha1", bg="light blue")
lb1.pack(side=TOP, fill=BOTH, expand=1)

lb2 = Label(janela, text="linha2", bg="black")
lb2.pack(side=TOP, fill=BOTH, expand=1)

lb3 = Label(janela, text="linha3", bg="yellow")
lb3.pack(side=TOP, fill=BOTH, expand=1)

lb4 = Label(janela, text="linha4", bg="purple")
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela.mainloop()