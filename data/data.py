import sqlite3 as sql
database = sql.connect('data/database.db')
cursor = database.cursor()