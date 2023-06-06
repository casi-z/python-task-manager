from windows import MainWindow
from PyQt5.QtWidgets import *
from pages import *
import sys

# Главная функция программы
def main():
    app = QApplication(sys.argv)
    
    login = Login
    window = MainWindow(login)
    window.show()
    # запускаем прогу
    app.exec()


# запускаем главную функцию
# этот if защита от дебила который решит это хрень кудато импортировать
# Димон если читаешь это поставь сюда точку
if __name__ == '__main__':
    main()
# команда из ui в py переводит
# python -m PyQt5.uic.pyuic -x Tasks.ui -o Tasks.py
