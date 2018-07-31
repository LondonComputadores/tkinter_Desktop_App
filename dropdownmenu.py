from tkinter import *

root = Tk()

def random():
    print("This is a statement")

mainMenu = Menu(root)
root.configure(menu = mainMenu)
subMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Arquivos", menu = subMenu)
subMenu.add_command(label = "Abrir", command = random)
subMenu.add_command(label = 'Salvar', command = random)
subMenu.add_separator()
subMenu.add_command(label = "Sair")

subMenu = Menu(subMenu)
mainMenu.add_cascade(label="Enviar", menu = subMenu)
subMenu.add_command(label = "Impressora", command = random)
subMenu.add_command(label = "E-mail", command = random)

subMenu = Menu(subMenu)
mainMenu.add_cascade(label="Pesquisar", menu = subMenu)
subMenu.add_command(label = "CID", command = random)
subMenu.add_command(label = "Pacientes", command = random)
subMenu.add_separator()
subMenu.add_command(label = "Sobre/Ajuda")

root.mainloop()
