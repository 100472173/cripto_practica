import sqlite3
from database_management import db_management
from database_management import db_destroy
conn = sqlite3.connect('../database_management/app_database.db')
cursor = conn.cursor()



sql_query = f"SELECT * from user_data;"
cursor.execute(sql_query)
info = cursor.fetchall()
print(info)

