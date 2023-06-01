from PyQt5.QtWidgets import *
from components import AppLayout
from components import User
from components import Error
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from components import Redirect
from pages import Register
from PyQt5.uic import loadUi
# Qt - Библиотека для интерфейсов


class Login():
    
    def __init__(self):
        self.username = None
        self.password = None
        loadUi("Login.ui", self)




        self.login_input.textChanged.connect(self.login_handle_change)
        self.password_input.textChanged.connect(self.password_handle_change)
        self.login_button.clicked.connect(self.login_handle_click)
        self.go_to_register_button.clicked.connect(self.go_to_register_button_handle_click)

    

    def is_form_valid(self):

        if self.username != None and self.password != None:
            return True
        else:
            return False

    def go_to_register_button_handle_click(self):
        self.window.redirect('Register(self)')


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
            # редирект 
            self.window.redirect(f'Calendar_Month(self)')
            user.create_cookie()
            user.read_cookie()
            
        else: 
            user_exist_error = Error('Некоректный логин или пароль')
            user_exist_error.throw()
    