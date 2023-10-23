"""Este codigo se usa UNICA Y EXCLUSIVAMENTE en el caso de que se desee destruir al completo la BBDD
    * No usar si no se desea llevar a cabo una accion irreversible *
"""
import sqlite3
conn = sqlite3.connect('../database_management/app_database.db')


def destroy():
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE USER_DATA;")
    cursor.execute(f"DROP TABLE USER_INFO;")
    cursor.execute(f"DROP TABLE USUARIOS;")

