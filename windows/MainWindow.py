from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from pages import Login, Calendar_Month, Register
class MainWindow(QMainWindow):
    
    def __init__(self, page):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.ui = page(self)
       
        self.setWindowTitle('self.ui.title')
    
    def redirect(self, target):
        self.ui = eval(target)
