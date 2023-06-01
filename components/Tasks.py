from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from components import Error
class Tasks(QWidget):
    def __init__(self, Form):
        super().__init__()
        
        Form.setObjectName("Form")
        Form.resize(400, 452)
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 360, 341, 41))
        self.textEdit.setObjectName("textEdit")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(130, 410, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: #8EDCFE\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 255)\n"
"}")
        self.addButton.setObjectName("pushButton")
        self.task_container = QtWidgets.QListWidget(Form)
        self.task_container.setGeometry(QtCore.QRect(25, 61, 351, 291))
        self.task_container.setObjectName("listWidget")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

        # Вызываю метод по клику на кнопку
        # Передаю аргументом введённый текст
        self.addButton.clicked.connect(lambda: self.add_task(self.textEdit.toPlainText()))
       
        self.task_list = []
        for task in self.task_list:
            task_item = QListWidgetItem(task)
            self.task_container.addItem(task_item)
    def add_task(self, task_name):
   
        task_item = QListWidgetItem(task_name)
        if not task_name in self.task_list:
            self.task_list.append(task_name)
            self.task_container.addItem(task_item)
        else:
            task_exist_error = Error('Нельзя добавлять две одинаковые задачи')
            task_exist_error.throw()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "СПИСОК ЗАДАЧ"))
        self.addButton.setText(_translate("Form", "Добавить задачу"))





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