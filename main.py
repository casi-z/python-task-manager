from pages import SignUp
from PyQt6.QtWidgets import *
import sys

# Главная функция приложения
def main():
    app = QApplication(sys.argv)

    # открываем окно
    window = SignUp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
