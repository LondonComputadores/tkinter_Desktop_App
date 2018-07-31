
from tkinter import *

janela = Tk()
janela.title('Clinica Conde')

janela['bg'] = "pink"
janela.geometry("1100x700+100+40")

def bt_onclik():
    print(ed.get())
    lb["text"] = ed.get()

ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=20, text="OK", command=bt_onclik)
bt.place(x=100, y=150)

lb = Label(janela, text="Label")
lb.place(x=100, y=200)

janela.mainloop()