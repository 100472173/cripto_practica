import sqlite3
from database_management import db_management
conn = sqlite3.connect('app_database.db')

cursor = conn.cursor()
sql_query = f"SELECT * FROM USuarios;"
cursor.execute(sql_query)
info = cursor.fetchall()
print(info)
