from windows import MainWindow
from PyQt5.QtWidgets import *
from pages import *
import sys

# Главная функция программы
def main():
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    login = Login()
    widget.addWidget(login)
    # запускаем прогу
    app.exec()


# запускаем главную функцию
# этот if защита от дебила который решит это хрень кудато импортировать
# Димон если читаешь это поставь сюда точку
if __name__ == '__main__':
    main()
# блять
# команда из ui в py переводит
# python -m PyQt5.uic.pyuic -x error.ui -o error.py
