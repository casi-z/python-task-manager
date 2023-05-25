from PyQt5.QtWidgets import *
from components import AppLayout
from components import User
from components import Error
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from components import Redirect
from pages import Register
# Qt - Библиотека для интерфейсов


class Login():
    
    def __init__(self, window):
        self.username = None
        self.password = None

        self.window = window
        window.setObjectName("Form")
        window.resize(400, 444)
        window.setStyleSheet("background: white;")
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(150, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login_input = QtWidgets.QLineEdit(window)
        self.login_input.setGeometry(QtCore.QRect(20, 130, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.login_input.setFont(font)
        self.login_input.setStyleSheet("background:#E0F8FF;\n"
"border-radius:20%;\n"
"color: rgba(0, 0, 0, 0.7);")
        self.login_input.setObjectName("login_input")
        self.password_input = QtWidgets.QLineEdit(window)
        self.password_input.setGeometry(QtCore.QRect(20, 220, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("background:#E0F8FF;\n"
"border-radius:20%;\n"
"color: rgba(0, 0, 0, 0.7);")
        self.password_input.setObjectName("password_input")
        self.login_button = QtWidgets.QPushButton(window)
        self.login_button.setGeometry(QtCore.QRect(110, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet("background: #8EDCFE;\n"
"border-radius: 20%;")
        self.login_button.setObjectName("login_button")
        self.go_to_register_button = QtWidgets.QPushButton(window)
        self.go_to_register_button.setGeometry(QtCore.QRect(60, 410, 281, 23))
        self.go_to_register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_to_register_button.setStyleSheet("background: none;\n"
"border: none;\n"
"color: blue;")
        self.go_to_register_button.setObjectName("go_to_register_button")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)




        self.login_input.textChanged.connect(self.login_handle_change)
        self.password_input.textChanged.connect(self.password_handle_change)
        self.login_button.clicked.connect(self.login_handle_click)
        self.go_to_register_button.clicked.connect(self.go_to_register_button_handle_click)




    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вход"))
        self.login_input.setText(_translate("Form", " Логин"))
        self.password_input.setText(_translate("Form", " Пароль"))
        self.login_button.setText(_translate("Form", "Войти"))
        self.go_to_register_button.setText(_translate("Form", "Еще не зарегистрированны? Создать аккаунт"))

    

    def is_form_valid(self):

        if self.username != None and self.password != None:
            return True
        else:
            return False

    def go_to_register_button_handle_click(self):
        self.window.redirect('Register')


    def login_handle_change(self, text):
        self.username = text.replace(' ', '')

    def password_handle_change(self, text):
        self.password = text.replace(' ', '')

    

    def login_handle_click(self):
        
        if self.is_form_valid() == False:
            invalid_form_error = Error('Некоректный логин или пароль')
            invalid_form_error.throw()
            return
        
        user = User(self.username, self.password)

       

        if user.is_user_exist():
            self.window.redirect('Calendar')
            print('вы вошли')
            
        else: 
            user_exist_error = Error('Некоректный логин или пароль')
            user_exist_error.throw()
    