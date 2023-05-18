from PyQt6.QtWidgets import *
from components import *
from pages import *
from pages import *


# Qt - Библиотека для интерфейсов


class SignIn(QWidget):
    
    def __init__(self):

        super().__init__()

        self.widget = self

        main = AppLayout()
        
        go_to_register_button = QPushButton('Создать аккаунт')
        go_to_register_button.clicked.connect(self.go_to_register_button_handle_click)

        login_button = QPushButton('Войти')

        login_button.clicked.connect(self.login_handle_click)

        login_input = QLineEdit()
        login_input.textChanged.connect(self.login_handle_change)

        password_input = QLineEdit()
        
        password_input.textChanged.connect(self.password_handle_change)
        
       
        main.render([

            QLabel('Вход'),
            go_to_register_button,
            QLabel('Введите логин'),
            login_input,

            QLabel('Введите пароль'),
            password_input,

            login_button
            
        ])

        
        self.setLayout(main)
        
        self.username = None
        self.password = None
        

    def get_widget(self):
        return self.widget

    def is_form_valid(self):

        if self.username != None and self.password != None:
            return True
        else:
            return False

    def go_to_register_button_handle_click(self):
        Redirect(self, SignUp)

    def login_handle_change(self, text):
        self.username = text

    def password_handle_change(self, text):
        self.password = text

    

    def login_handle_click(self):
        
        if self.is_form_valid() == False:
            invalid_form_error = Error('Некоректный логин или пароль')
            invalid_form_error.throw()
            return
        
        user = User(self.username, self.password)

       

        if user.is_user_exist():
            print('Вход выполнен')
            
        else: 
            user_exist_error = Error('Некоректный логин или пароль')
            user_exist_error.throw()
    