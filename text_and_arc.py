from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

'''canvas.create_arc(10,10,200,80,extent = 45, style = ARC)
canvas.create_arc(10,80,200,160,extent = 90, style = ARC)

#randomRects(150)'''

canvas.create_text(150, 150, text = " CLINICA CONDE \n" "\n       Bem Vindos ", font = ("Times", 28))


root.mainloop()