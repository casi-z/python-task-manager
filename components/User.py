from data.data import cursor, database
import json
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
            print(self.username)

    def register(self):
        users_table = cursor.execute("""SELECT * FROM users""").fetchall()
        last_id = users_table[-1][0]
        
        cursor.execute(f"""INSERT INTO users(id, username, password) VALUES ({last_id + 1},'{self.username}', '{self.password}');""")
        database.commit()

n = User('','')
n.read_cookie()