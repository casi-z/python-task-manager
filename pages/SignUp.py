from PyQt6.QtWidgets import *
from components import AppLayout

# Qt - Библиотека для интерфейсов


class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Регистрация")

        # self.username_input = QLineEdit()
        # self.password_input = QLineEdit()
        # self.password_repeat = QLineEdit()

        main = AppLayout()

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

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)
