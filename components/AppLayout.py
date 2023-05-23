from PyQt5.QtWidgets import *

# Класс заменитель обычного лайяута 
# Наследование классов (записывание родителя в скобки) ахрененный способ добавления новых функций в библиотеку
class AppLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

    def render(self, elements):
        for elements in elements:
            self.addWidget(elements)

    def renderLayout(self, elements):
        for elements in elements:
            self.addLayout(elements)