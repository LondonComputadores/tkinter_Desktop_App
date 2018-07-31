from tkinter import *

janela = Tk()
janela.title("Clinica Conde - Atendimento Ginecológico e Obstétrico")
janela ["bg"] = "pink"
janela.geometry("1100x700+100+40")

lb1= Label(janela, text="Espaço", width="10", height=6, bg="green", fg="black")
lb2= Label(janela, text="Espaço", width="10", height=6, bg="grey", fg="black")
lb3= Label(janela, text="Espaço", width="10", height=6, bg="brown", fg="black")
lb4= Label(janela, text="Espaço", width="10", height=6, bg="purple", fg="black")

lb5= Label(janela, text="Espaço", height=3, bg="white", fg="black")
lb6= Label(janela, text="Espaço", width="5", bg="yellow", fg="black")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=0, column=1)
lb4.grid(row=1, column=1)

lb5.grid(row=2, column=0, columnspan=2, sticky=W+E)
lb6.grid(row=0, column=2, rowspan=2, sticky=N+S)




janela.mainloop()