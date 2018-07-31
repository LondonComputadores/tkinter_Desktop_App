
from tkinter import *

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
canvas.create_rectangle(20, 20, 100, 250)
canvas.create_line(100,50, 50, 50)
canvas.create_polygon(25, 35, 55, 36, 41, 51)

def createRect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill = "Blue")

createRect(50, 50, 200, 270)

root.mainloop()