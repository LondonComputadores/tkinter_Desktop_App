
from tkinter import *
from functools import partial

janela = Tk()
janela.title('Clinica Conde')

janela['bg'] = "pink"
janela.geometry("1100x700+100+40")

'''def button_click(botao):
    print("Botao1ou2")'''

def bt_click(botao):
    print(botao["text"])

#bt1 = Button(janela, width = 20, text = "Botão1", command=button_click)
bt1 = Button(janela, width = 20, text = "Botão 1")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100, y=100)

#bt2 = Button(janela, width=20, text="Botao 2", command=button_click)
bt2 = Button(janela, width=20, text="Botao 2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=130)

janela.mainloop()