from PyQt6.QtWidgets import *
from components import AppLayout
from components import User
from components import Error
# Qt - Библиотека для интерфейсов


class Register(QWidget):
    
    def __init__(self):

        super().__init__()

        main = AppLayout()

        register_button = QPushButton('Зарегаться')
        register_button.clicked.connect(self.register_handle_click)

        login_input = QLineEdit()
        login_input.textChanged.connect(self.login_handle_change)

        password_input = QLineEdit()
        
        password_input.textChanged.connect(self.password_handle_change)
        
        password_repeat_input = QLineEdit()

        password_repeat_input.textChanged.connect(self.password_repeat_handle_change)

        main.render([
            QLabel('Регистрация'),
            QLabel('Придумайте логин'),
            login_input,

            QLabel('Придумайте пароль'),
            password_input,
            QLabel('Повторите пароль'),
            password_repeat_input,
            register_button
            
        ])

        
        self.setLayout(main)
        
        self.username = None
        self.password = None
        self.password_repeat = None

    def is_form_valid(self):

        if self.username != None and self.password != None and self.password == self.password_repeat:
            return True
        else:
            return False

    def login_handle_change(self, text):
        self.username = text

    def password_handle_change(self, text):
        self.password = text

    def password_repeat_handle_change(self, text):
        self.password_repeat = text

    def register_handle_click(self):
        
        if self.is_form_valid() == False:
            invalid_form_error = Error('Некоректный логин или пароль 1')
            invalid_form_error.throw()
            print(self.username, self.password, self.password_repeat)
            return
        
        new_user = User(self.username, self.password)

       

        if new_user.is_user_exist() == False:
            print('вы зарегались')
            new_user.register()
        else: 
            user_exist_error = Error('Такой пользователь уже существует 2')
            user_exist_error.throw()
    