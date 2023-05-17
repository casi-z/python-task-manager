from data.data import cursor, database
# Курсор это функция для принимания sql запросов

# класс user используется для регистрации и запросов в бд
# прочитайте пж чё такое класс конструктор метод и свойство 
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    # Проверяет зарегистрирован ли юзер
    def is_user_exist(self):
        users_table = cursor.execute("""SELECT * FROM users""").fetchall()
        print(users_table)
        for string in users_table:
            
            if string[1] == self.username and string[2] == self.password:
                return True
            else:
                return False
    
    # Добавляем юзера в базу данных
    def register(self):
        cursor.execute(f"""INSERT INTO users(username, password) VALUES ('{self.username}', '{self.password}');""")
        database.commit()
                

