
from tkinter import *

janela = Tk()
janela.title('Clinica Conde')

janela['bg'] = "pink"
janela.geometry("1100x700+100+40")

'''def bt_click():
    print("Bt_click")
    num1 = int(ed1.get())
    num2 = int(ed2.get())

    lb["text"] = num1 + num2'''

def bt_click():
    print("Bt_click")
    num1 = int(ed1.get())
    num2 = int(ed2.get())

    lb["text"] = num1 + num2

ed1 = Entry(janela)
ed1.place(x=100, y=100)
ed2 = Entry(janela)
ed2.place(x=100, y=130)

bt = Button(janela, text="SOMA", width=20, command=bt_click)
bt.place(x=100, y=150)

lb = Label(janela, text="Label")
lb.place(x=100, y=200)


janela.mainloop()