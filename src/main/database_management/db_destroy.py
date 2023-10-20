import sqlite3
conn = sqlite3.connect('../database_management/app_database.db')


def destroy():
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE USER_DATA;")
    cursor.execute(f"DROP TABLE USER_INFO;")
    cursor.execute(f"DROP TABLE USUARIOS;")

