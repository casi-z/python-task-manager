import sqlite3 as sql
database = sql.connect('data/database.db')
cursor = database.cursor()
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def is_user_exist(self):
        users_table = cursor.execute("""SELECT * FROM users""").fetchall()

        for string in users_table:
            
            if string[1] == self.username and string[2] == self.password:
                # print(
                #     f'{self.username} : {string[1]}',
                #     f'{self.password} : {string[2]}',

                # )
                return True
            else:
                # print(
                #     f'{self.username} : {string[1]}',
                #     f'{self.password} : {string[2]}',

                # )
                return False
    def register(self):
        cursor.execute(f"""INSERT users(name, password) 
            VALUES ('{self.username}', '{self.password}');
        """)
                

