from tkinter import *

root = Tk()

def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

def upClick(event):
    print("Up")

def leftKey(event):
    print("LeftKeyPressed")

def rightKey(event):
    print("RightKeyPressed")

def upKey(event):
    print("UpKeyPressed")

'''def printName(event):
    print("Bem Vinda!")

#button1 = Button(root, text = "Click Here", command = printName)

#button1 = Button(root, text = "Click Here")
#button1.bind("<Button-1>", printName)

#button1.pack()'''

root.geometry("500x500")

root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", rightClick)
root.bind("<Button-3>", upClick)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)


root.mainloop()
