from tkinter import *

janela = Tk()
janela.title("Clinica Conde")
janela ["bg"] = "pink"
janela.geometry("1100x700+100+40")

lb1 = Label(janela, text= "Login: ")
lb2 = Label(janela, text= "Senha: ")

ed1 = Entry(janela,)
ed2 = Entry(janela,)

bt1 = Button(janela, text= "Confirmar")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=1)

janela.mainloop()