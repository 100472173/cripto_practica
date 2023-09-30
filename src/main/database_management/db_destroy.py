import sqlite3
conn = sqlite3.connect('../database_management/app_database.db')
def destroy():
    conn.execute(f"DROP TABLE USUARIOS;")
    conn.execute(f"DROP TABLE USER_INFO;")