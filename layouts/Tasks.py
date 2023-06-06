from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from components import Error, User, Task
from PyQt5.QtCore import Qt
class Tasks(QWidget):
    def __init__(self, Form):
        super().__init__()
        self.setWindowTitle("Todo List")

        layout = QVBoxLayout(Form)

        self.listWidget = QListWidget()

        layout.addWidget(self.listWidget)

         
        self.addButton = QPushButton("Добавить")
        self.addButton.setGeometry(QtCore.QRect(80, 140, 221, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("border-radius: 20%;\n"
"background-color: rgb(89, 211, 255);\n"
"color:#ffffffff;")
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addTask)

        self.clearButton = QPushButton("Выполнить")
        self.clearButton.clicked.connect(self.clearCompletedTasks)
        
        self.clearButton.setGeometry(QtCore.QRect(80, 140, 221, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("border-radius: 20%;\n"
"background-color: rgb(255, 17, 21);\n"
"color:#ffffffff;")
        self.clearButton.setObjectName("addButton")
        

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.addButton)
        horizontalLayout.addWidget(self.clearButton)

        layout.addLayout(horizontalLayout)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        Form.setLayout(layout)

        self.user = User('','')
        self.user.read_cookie()
        self.task_list = self.user.load_tasks()

        for task in self.task_list:
            item = QListWidgetItem(task, self.listWidget)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
    def addTask(self):
        text, ok = QInputDialog.getText(self, 'Новая задача', 'Что вы хотите сделать:')

        if ok and text and not text in self.task_list:
            item = QListWidgetItem(text, self.listWidget)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            # Добавляем в БД

            self.user.add_task(text)
            
        else:
            task_exist_error = Error('Нельзя добавлять две одинаковые задачи')
            task_exist_error.throw()

    def clearCompletedTasks(self):
        for i in reversed(range(self.listWidget.count())):
            if self.listWidget.item(i).checkState() == Qt.Checked:
                deleted_item = self.listWidget.takeItem(i)
                self.user.delete_task(deleted_item.text())
                self.user.create_report(deleted_item.text())

    def updateLabel(self):
        count = self.listWidget.count()
        checkedCount = sum(self.listWidget.item(i).checkState() == Qt.Checked for i in range(count))

        self.label.setText(f"{checkedCount}/{count} tasks completed")
        
    





#         self.task_container = QListWidget(self)

#         layout = QVBoxLayout()
#         layout.addWidget(self.task_container)
#         button = QPushButton('layout')
#         layout.addWidget(button)

#         self.setLayout(layout)
#         self.n = 0
    #     button.clicked.connect(lambda: self.add_task(f'хуй{self.n}'))
    #     self.n = self.n+1
    # def add_task(self, task_name):
    #     task_item = QListWidgetItem(task_name)
    #     self.task_container.addItem(task_item)
    #     self.n = self.n+1

# if __name__ == '__main__':
#     app = QApplication([])
#     task_container = Tasks()
#     task_container.add_task('Do laundry')
#     task_container.add_task('Buy groceries')
#     task_container.show()
#     app.exec_()