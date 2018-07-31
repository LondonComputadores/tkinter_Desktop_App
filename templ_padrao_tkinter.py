
from tkinter import *
from functools import partial
import tkinter as tk

janela = tk.Tk()

photo = PhotoImage(file="logo.png", width=1200, height=720)
label=Label(janela, image=photo)
label.pack()

janela.title("Clinica Conde - Atendimento")
janela ["bg"] = "pink"
janela.geometry("1100x700+100+40")

def bt_click(botao):
    print(botao["text"])

#bt1 = Button(janela, width = 20, text = "Botão1", command=button_click)
bt1 = Button(janela, width = 20, text = "Diagnósticos")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100, y=200)

#bt2 = Button(janela, width=20, text="Botao 2", command=button_click)
bt2 = Button(janela, width=20, text="Histórico")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=230)

def random():
    print("This is a statement")

mainMenu = Menu(janela)
janela.configure(menu = mainMenu)
subMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Arquivos", menu = subMenu)
subMenu.add_command(label = "Abrir", command = random)
subMenu.add_command(label = 'Salvar', command = random)
subMenu.add_separator()
subMenu.add_command(label = "Sair")

subMenu = Menu(subMenu)
mainMenu.add_cascade(label="Enviar", menu = subMenu)
subMenu.add_command(label = "Impressora", command = random)
subMenu.add_command(label = "E-mail", command = random)

subMenu = Menu(subMenu)
mainMenu.add_cascade(label="Pesquisar", menu = subMenu)
subMenu.add_command(label = "CID", command = random)
subMenu.add_command(label = "Pacientes", command = random)
subMenu.add_separator()

def bt_onclik():
    print(ed.get())
    lb["text"] = ed.get()

ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=20, text="OK", command=bt_onclik)
bt.place(x=100, y=150)

lb = Label(janela, text="Nº Do Prontuário:", bg="white")
lb.place(x=100, y=70)


janela.mainloop()