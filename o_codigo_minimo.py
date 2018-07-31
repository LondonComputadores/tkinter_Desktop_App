
from tkinter import *
import tkinter as tk

janela = tk.Tk()
janela.title('Clinica Conde')

janela['bg'] = "pink"
janela.geometry("1100x700+100+40")

'''
photo = PhotoImage(file = "logo.png.png", width = 900, height = 500)
label = Label(janela, image = photo)
label.pack()
'''

def bt_click():
    print("bt_click")

    lb["text"] = "FUNFOU!"

bt = Button(janela, width = 20, text = "OK", command = bt_click)
bt.place(x = 10, y = 100)

lb = Label(janela, width = 10, height = 2, text = "Teste")
lb.place(x = 100, y = 150)

janela.mainloop()