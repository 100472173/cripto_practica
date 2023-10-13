import sqlite3
from database_management import db_management
from database_management import db_destroy
conn = sqlite3.connect('../database_management/app_database.db')
cursor = conn.cursor()

sql_query = f"SELECT key_used from user_info where user = 'ili37';"
cursor.execute(sql_query)
info = cursor.fetchall()
print((info[0][0]))
print(db_management.get_user_info("ili37"))
"""
sql_query = f"SELECT money from user_info where user = 'iboPSOE';"
cursor.execute(sql_query)
info = cursor.fetchall()
print(type(info[0][0]))
"""
