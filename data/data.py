import sqlite3 as sql
#  подключаемся в базу данных
database = sql.connect('data/database.db')
cursor = database.cursor()