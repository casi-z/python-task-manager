from PyQt6.QtWidgets import *
from PyQt6 import QtGui
class MainWindow(QMainWindow):
    def __init__(self, start_page):
        super().__init__()
        container = start_page.get_widget()
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.setCentralWidget(container)
