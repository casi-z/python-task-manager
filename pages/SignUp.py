from PyQt6.QtWidgets import *
from components import AppLayout

# Qt - Библиотека для интерфейсов

# Создаём окно с регистрацией
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Регистрация")

        main = AppLayout()

        # Создаём элементы (поля, надписи)
        main.render([
            QLabel('Регистрация'),
            QLabel('Придумайте логин'),
            QLineEdit(),
            QLabel('Придумайте пароль'),
            QLineEdit(),
            QLabel('Повторите пароль'),
            QLineEdit(),
            QPushButton('Зарегаться')
            
        ])

        container = QWidget()
        container.setLayout(main)

        self.setCentralWidget(container)
