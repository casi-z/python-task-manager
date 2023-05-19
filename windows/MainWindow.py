from PyQt6.QtWidgets import *
from PyQt6 import QtGui
class MainWindow(QMainWindow):
    def __init__(self, page):
        super().__init__()
        container = page
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.setCentralWidget(container)
