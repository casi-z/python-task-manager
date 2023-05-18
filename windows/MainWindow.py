from PyQt6.QtWidgets import *
from PyQt6 import QtGui
class MainWindow(QMainWindow):
<<<<<<< HEAD
    def __init__(self, start_page):
        super().__init__()
        container = start_page.get_widget()
=======
    def __init__(self, page):
        super().__init__()
        container = page.get_widget()
>>>>>>> e35a1bd067afe76fae2d0ff51fcde6a3b5ce0018
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.setCentralWidget(container)
