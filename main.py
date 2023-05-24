from windows import MainWindow
from PyQt5.QtWidgets import *
from pages import *
import sys

# Главная функция программы
def main():
    app = QApplication(sys.argv)
    register_page = Register
    login_page = Login
    calendar_page = Calendar
    # Создаём главное окно
    window = MainWindow(login_page)  # Здесь заменил Login_page на Login_page
    window.show()

    # запускаем прогу
    app.exec()


# запускаем главную функцию
# этот if защита от дебила который решит это хрень кудато импортировать
# Димон если читаешь это поставь сюда точку
if __name__ == '__main__':
    main()
<<<<<<< HEAD
# python -m PyQt5.uic.pyuic -x zakladki.ui -o zakladki.py
=======
# python -m PyQt5.uic.pyuic -x calendar-day.ui -o calendar-day.py
# бля
>>>>>>> a37f30b6691dd5fcc493d31162d52509eaf277e2
