from tkinter import *

janela = Tk()
janela.title("Clinica Conde - Atendimento Ginecológico e Obstétrico")
janela ["bg"] = "pink"
janela.geometry("1100x700+100+40")

lb1= Label(janela, text="Espaço", width="10", height=3, bg="black", fg="yellow")
lbHorizontal = Label(janela, text="horizontal", bg="white")
lbVertical = Label(janela, text="vertical", bg="purple")

lb1.grid(row= 0, column= 0)
lbHorizontal.grid(row=1, column=0, sticky=W)
lbVertical.grid(row=0, column=1, sticky=N)


janela.mainloop()