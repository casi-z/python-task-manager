from data.data import cursor, database
import json
import sqlite3 as sql
#  подключаемся в базу данных

# Курсор это функция для принимания sql запросов

# класс user используется для регистрации и запросов в бд
# прочитайте пж чё такое класс конструктор метод и свойство 

class User():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.users_table = cursor.execute("""SELECT * FROM users""").fetchall()

    # Проверяет зарегистрирован ли юзер
    def is_user_exist(self):
        
        for string in self.users_table:
            
            if string[1] == self.username and string[2] == self.password:
                return True
            
        return False
                
    def create_cookie(self):

        with open("cookie.json", "w") as cookie_file:
            cookie_file.write("""{"username": "%s", "password": "%s"}"""%(self.username, self.password))

    def read_cookie(self):

        with open("cookie.json", "r") as cookie_file:

            user_info = json.loads(cookie_file.read())
            self.username = user_info['username']
            self.password = user_info['password']
            
    def register(self):

        users_table = cursor.execute("""SELECT * FROM users""").fetchall()
        last_user_id = users_table[-1][0] if len(users_table) > 0 else 0
        
        cursor.execute(f"""INSERT INTO users(id, username, password) VALUES ({last_user_id + 1},'{self.username}', '{self.password}');""")
        database.commit()

    def load_tasks(self):

        self.task_table = cursor.execute(f"""SELECT * FROM tasks WHERE username == '{self.username}'""").fetchall()
        self.task_list = []
        for task in self.task_table:

            self.task_list.append(task[2])

        return self.task_list
    
    def add_task(self, task_name):

        self.task_table = cursor.execute(f"""SELECT * FROM tasks WHERE username == '{self.username}'""").fetchall()
        last_task_id = self.task_table[-1][0] if len(self.task_table) > 0 else 0
        
        cursor.execute(f"""INSERT INTO tasks(username, name) VALUES ('{self.username}', '{task_name}');""")
        database.commit()
