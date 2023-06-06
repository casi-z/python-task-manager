from PyQt5.QtWidgets import *
from components import *
from pages import Login
from PyQt5 import QtCore, QtGui, QtWidgets

# Qt - Библиотека для интерфейсов


class Register(QWidget):
    
    def __init__(self, window):

        super().__init__()
        self.window = window
        
        window.setWindowTitle('Регистрация')
        self.username = None
        self.password = None
        self.password_repeat = None
        
        window.setObjectName("Register")
        window.resize(426, 486)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        window.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setStyleSheet("background: #FFFFFF;")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(50, 350, 331, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 220, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.register_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.register_button.setFont(font)
        self.register_button.setStyleSheet("background-color: #8EDCFE;\n"
"border-radius: 30%;\n"
"")
        self.register_button.setObjectName("register_button")
        self.password_repeat_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_repeat_input.setGeometry(QtCore.QRect(50, 260, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.password_repeat_input.setFont(font)
        self.password_repeat_input.setStyleSheet("background-color: #E0F8FF;\n"
"border-radius: 20%;\n"
"color: rgba(0, 0, 0, 0.7);\n"

)
        self.password_repeat_input.setObjectName("password_repeat_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(50, 190, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("background-color: #E0F8FF;\n"
"border-radius: 20%;\n"
"color: rgba(0, 0, 0, 0.7);\n"

)
        self.password_input.setObjectName("password_input")
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_input.setGeometry(QtCore.QRect(50, 120, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.login_input.setFont(font)
        self.login_input.setStyleSheet("background-color: #E0F8FF;\n"
"border-radius: 20%;\n"
"color: rgba(0, 0, 0, 0.7);\n"

)
        self.login_input.setObjectName("login_input")
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

        self.login_input.setPlaceholderText('Придумайте логин')
        self.password_input.setPlaceholderText('Придумайте пароль')
        self.password_repeat_input.setPlaceholderText('Повторите пароль')

        # пошли хендлеры
        self.login_input.textChanged.connect(self.login_handle_change)
        self.password_input.textChanged.connect(self.password_handle_change)
        self.password_repeat_input.textChanged.connect(self.password_repeat_handle_change)
        self.register_button.clicked.connect(self.register_handle_click)


    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Register", "MainWindow"))
        self.label.setText(_translate("Register", "Регистрация"))
        self.register_button.setText(_translate("Register", "Зарегаться"))
       

    def is_form_valid(self):

        if self.username != None and self.password != None and self.password == self.password_repeat:
            return True
        else:
            return False

    def go_to_login_handle_click(self):
        # //Redirect(self, Login)
        print()

    def login_handle_change(self, text):
        self.username = text.replace(' ', '')

    def password_handle_change(self, text):
        self.password = text.replace(' ', '')
        

    def password_repeat_handle_change(self, text):
        self.password_repeat = text.replace(' ', '')

    def register_handle_click(self):
        
        if self.is_form_valid() == False:
            invalid_form_error = Error('Некоректный логин или пароль 1')
            invalid_form_error.throw()
            
            return
        
        new_user = User(self.username, self.password)

       

        if new_user.is_user_exist() == False:
            print('вы зарегались')
            new_user.register()
            new_user.create_cookie()
            self.window.redirect(f'StartPage(self)')
        else: 
            user_exist_error = Error('Такой пользователь уже существует 2')
            user_exist_error.throw()
    