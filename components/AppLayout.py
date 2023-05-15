from PyQt6.QtWidgets import *
class AppLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

    def render(self, elements):
        for elements in elements:
            self.addWidget(elements)