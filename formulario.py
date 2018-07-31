from tkinter import *

root = Tk()

label1 = Label(root, text = "Nome")
label1.grid(row = 0, column = 0, sticky = "E")
entrySpace = Entry(root)
entrySpace.grid(row = 0, column = 1)

label2 = Label(root, text = "email")
label2.grid(row = 2, column = 0, sticky = "E")
entrySpace = Entry(root)
entrySpace.grid(row = 2, column = 1)


label3 = Label(root, text = "Password")
label3.grid(row = 3, column = 0, sticky = "E")
entrySpace = Entry(root)
entrySpace.grid(row = 3, column = 1)



root.mainloop()