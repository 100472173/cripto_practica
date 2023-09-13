import sqlite3
conn = sqlite3.connect('app_database.db')
def create():
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                        NICKNAME VARCHAR(21) NOT NULL,
                        PASSWORD VARCHAR(100) NOT NULL,	
                        PRIMARY KEY(NICKNAME)
                    );""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_info (
                        USER VARCHAR(21),
                        MONEY NUMERIC(10,2),
                        EMAIL VARCHAR(50),
                        NAME VARCHAR(30),
                        SURNAME1 VARCHAR(50),
                        SURNAME2 VARCHAR(50),
                        PRIMARY KEY(USER),
                        FOREIGN KEY(USER) references USUARIOS(NICKNAME)
                    );""") #xd