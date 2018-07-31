from tkinter import *

root = Tk()

theLabel= Label(root, text="Clinica Conde")
theLabel.pack()
theLabel= Label(root, text="Atendimento de Pacientes")
theLabel.pack()

topFrame = Frame(root)

topFrame.pack()

botFrame = Frame(root)

botFrame.pack(side=BOTTOM)



theButton = Button(None, text = "Cadastrar", fg = "Black", bg = "Grey")
theButton.pack(fill = X)

Button1 = Button(topFrame, text = "Particular", fg = "Blue")
Button1.pack(side=LEFT)

Button2 = Button(topFrame, text = "Convenio", fg = "Blue")
Button2.pack(side=LEFT)

Button3 = Button(botFrame, text = "Consulta", fg = "Red")
Button3.pack(side=RIGHT, fill = Y)

Button4 = Button(botFrame, text = "Retorno", fg = "Brown")
Button4.pack(side=RIGHT)


root.mainloop()