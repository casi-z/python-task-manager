from pages import SignUp
from PyQt6.QtWidgets import *
import sys

# Главная функция программы
def main():
    app = QApplication(sys.argv)
    
    # Создаём главное окно
    window = SignUp()
    window.show()

    # запускаем прогу
    app.exec()

if __name__ == '__main__':
    main()
