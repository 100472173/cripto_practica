import sqlite3
from database_management import db_management
conn = sqlite3.connect('../database_management/app_database.db')
cursor = conn.cursor()
sql_query = f"SELECT * from user_info;"
cursor.execute(sql_query)
info = cursor.fetchall()
for row in info:
    print(row)
