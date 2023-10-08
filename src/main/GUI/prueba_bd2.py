import sqlite3
from database_management import db_management
conn = sqlite3.connect('../database_management/app_database.db')
cursor = conn.cursor()
sql_query = f"SELECT * from user_info;"
cursor.execute(sql_query)
info = cursor.fetchall()
for row in info:
    print(row)
sql_query = f"SELECT money from user_info where user = 'iboPSOE';"
cursor.execute(sql_query)
info = cursor.fetchall()
print(type(info[0][0]))
