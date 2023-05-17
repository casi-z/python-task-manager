from PyQt6.QtWidgets import *
import sys
from components import AppLayout

# Окно для вывода ошибок 
class ErrorPopUp(QDialog):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.setWindowTitle("Ошибка")

        main = AppLayout()

        main.render([
            QLabel(f'Ошибка:{message}'),
            
        ])
        
        
        self.setLayout(main)


# Класс генератор ошибок
class Error():
    def __init__(self, message):
        self.message = message

    def throw(this):
        errorWindow = ErrorPopUp(this.message)
        errorWindow.exec()
        