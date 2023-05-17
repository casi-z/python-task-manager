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

# запускаем главную функцию
# этот if защита от дебила который решит это хрень кудато импортировать
# Димон если читаешь это поставь сюда точку
if __name__ == '__main__':
    main()
