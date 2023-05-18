from windows import MainWindow
from PyQt6.QtWidgets import *
from pages import *
import sys

# Главная функция программы
def main():
    app = QApplication(sys.argv)
    signUp_page = SignUp()
    signIn_page = SignIn()
    # Создаём главное окно
    window = MainWindow(signIn_page)  # Здесь заменил SignIn_page на signIn_page
    window.show()

    # запускаем прогу
    app.exec()


# запускаем главную функцию
# этот if защита от дебила который решит это хрень кудато импортировать
# Димон если читаешь это поставь сюда точку
if __name__ == '__main__':
    main()
