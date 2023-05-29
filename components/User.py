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
        self.result = False
        for string in users_table:
            
            if string[1] == self.username and string[2] == self.password:
                self.result = True

        return self.result
            
    # Добавляем юзера в базу данных
    def register(self):
        users_table = cursor.execute("""SELECT * FROM users""").fetchall()
        last_id = users_table[-1][0]
        
        cursor.execute(f"""INSERT INTO users(id, username, password) VALUES ({last_id + 1},'{self.username}', '{self.password}');""")
        database.commit()

