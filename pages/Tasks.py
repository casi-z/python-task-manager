from PyQt5.QtWidgets import *

class TaskList(QWidget):
    def __init__(self):
        super().__init__()

        self.task_list = QListWidget(self)

        layout = QVBoxLayout()
        layout.addWidget(self.task_list)
        button = QPushButton('layout')
        layout.addWidget(button)

        self.setLayout(layout)
        self.n = 0
        button.clicked.connect(lambda: self.add_task(f'хуй{self.n}'))
        self.n = self.n+1
    def add_task(self, task_name):
        task_item = QListWidgetItem(task_name)
        self.task_list.addItem(task_item)
        self.n = self.n+1

if __name__ == '__main__':
    app = QApplication([])
    task_list = TaskList()
    task_list.add_task('Do laundry')
    task_list.add_task('Buy groceries')
    task_list.show()
    app.exec_()