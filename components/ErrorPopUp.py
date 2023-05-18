from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize
from components import AppLayout
from PyQt6 import QtGui

# Окно для вывода ошибок 
class ErrorPopUp(QDialog):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.setWindowTitle("Ошибка")
        
        self.setWindowIcon(QtGui.QIcon('icons/error.png'))
        main = AppLayout()

        main.render([
            QLabel(f'Ошибка:{message}'),
            
        ])
        self.setFixedSize(QSize(400, 150))
        
        self.setLayout(main)

# Класс генератор ошибок
class Error():
    def __init__(self, message):
        self.message = message

    def throw(this):
        errorWindow = ErrorPopUp(this.message)
        errorWindow.exec()
        