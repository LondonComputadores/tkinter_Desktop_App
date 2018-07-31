
from tkinter import *

root = Tk()

''' Esse codigo comentado não estava incluso na aula calculator. É só teste.

def createWidgets(self):
    top=self.winfo_toplevel()

    top.rowconfigure(0, weight=1)

    top.columnconfigure(0, weight=1)

    self.rowconfigure(0, weight=1)

    self.columnconfigure(0, weight=1)

    self.quit = Button(self, text='Quit', command=self.quit)
    self.quit.grid(row=0, column=0,

    sticky=tk.N+tk.S+tk.E+tk.W)'''

equa = ""

equation = StringVar()

calculation = Label(root, textvariable = equation)

equation.set("0")

calculation.grid(columnspan = 4)

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = " "

def Clear():
    global equa
    equa = ""
    equation.set("")

BtnEqual = Button(root, text = "=", command = EqualPress)
BtnEqual.grid(row = 4, column = 1)

BtnClear = Button(root, text = "C", command = Clear)
BtnClear.grid(row = 4, column = 3)

Button0 = Button(root, text = "0", command = lambda: btnPress(0))
Button0.grid(row = 4, column = 2)

Button1 = Button(root, text = "1", command = lambda: btnPress(1))
Button1.grid(row = 3, column = 1)

Button2 = Button(root, text = "2", command = lambda: btnPress(2))
Button2.grid(row = 3, column = 2)

Button3 = Button(root, text = "3", command = lambda: btnPress(3))
Button3.grid(row = 3, column = 3)

Button4 = Button(root, text = "4", command = lambda: btnPress(4))
Button4.grid(row = 2, column = 1)

Button5 = Button(root, text = "5", command = lambda: btnPress(5))
Button5.grid(row = 2, column = 2)

Button6 = Button(root, text = "6", command = lambda: btnPress(6))
Button6.grid(row = 2, column = 3)

Button7 = Button(root, text = "7", command = lambda: btnPress(7))
Button7.grid(row = 1, column = 1)

Button8 = Button(root, text = "8", command = lambda: btnPress(8))
Button8.grid(row = 1, column = 2)

Button9 = Button(root, text = "9", command = lambda: btnPress(9))
Button9.grid(row = 1, column = 3)

BtnMinus = Button(root, text = "-", command = lambda: btnPress("-"))
BtnMinus.grid(row = 4, column = 4)

BtnPlus = Button(root, text = "+", command = lambda: btnPress("+"))
BtnPlus.grid(row = 3, column = 4)

BtnTimes = Button(root, text = "*", command = lambda: btnPress("*"))
BtnTimes.grid(row = 2, column = 4)

BtnDivision = Button(root, text = "/", command = lambda: btnPress("/"))
BtnDivision.grid(row = 1, column = 4)



root.mainloop()