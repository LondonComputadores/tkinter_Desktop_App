
from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Do u know what I mean?")

answer = tkinter.messagebox.askquestion("Question 1 ", "Are u human?")

if answer == "yes":
    tkinter.messagebox.showinfo("Congrats!", "Thank God! It's great to know!")

if answer == "no":
    tkinter.messagebox.showinfo("Aliens", "Ur an Alien")

root.mainloop()