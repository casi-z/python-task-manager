from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from pages import Login, Calendar_Month, Register, Calendar_Days

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        
       
        self.setWindowTitle('self.ui.title')
    
    def redirect(self, target):
        
      
        self.ui = eval(target)
        print(self.ui)
