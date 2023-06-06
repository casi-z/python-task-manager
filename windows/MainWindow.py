from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from pages import Login, Register, StartPage

class MainWindow(QMainWindow):
    
    def __init__(self, page):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.setWindowTitle('Вход')
        self.ui = page(self)
        
    
    def redirect(self, target):
        self.ui = eval(target)
        
