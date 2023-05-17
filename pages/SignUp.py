from PyQt6.QtWidgets import *
from components import AppLayout
from components import User
from components import Error
# Qt - Библиотека для интерфейсов


class SignUp(QMainWindow):
    
    def __init__(self):

        super().__init__()

        self.setWindowTitle("Регистрация")

        main = AppLayout()

        register_button = QPushButton('Зарегаться')
        register_button.clicked.connect(self.register_handle_click)

        login_input =  QLineEdit()
        login_input.textChanged.connect(self.login_handle_change)

        password_input =  QLineEdit()
        password_input.textChanged.connect(self.password_handle_change)
        main.render([
            QLabel('Регистрация'),
            QLabel('Придумайте логин'),
            login_input,

            QLabel('Придумайте пароль'),
            password_input,
            QLabel('Повторите пароль'),
            QLineEdit(),
            register_button
            
        ])

    

        container = QWidget()
        container.setLayout(main)

        
        self.setCentralWidget(container)
        self.username = None
        self.password = None
        self.passwordRepeat = None

    

    def login_handle_change(self, text):
        self.username = text

    def password_handle_change(self, text):
        self.password = text

    def password_repeat_handle_change(self, text):
        self.passwordRepeat = text

    def register_handle_click(self):
        registration = User(self.username, self.password)
        print(registration.is_user_exist())
        if registration.is_user_exist() == False:
            print('вы зарегались')
            registration.register()
        else: 
            error = Error('Такой пользователь уже существует')
            error.throw()
    