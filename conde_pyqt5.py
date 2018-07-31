
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import tkinter as tk

'''

def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidgets()
    window.setWindowTitle("Clinica Conde")
    window.setGeometry(50,50,500,500)
    window.show()
    sys.exc_info(app.exec_())
window()

'''

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Atendimento - Clínica Conde"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.setWindowIcon(QtGui.QIcon("logo.png"))

        self.inthatWindow()

    def inthatWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


