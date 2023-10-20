import sqlite3

conn = sqlite3.connect('../database_management/app_database.db')


def create():
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                        NICKNAME VARCHAR(21),
                        PWD_TOKEN VARCHAR(100) NOT NULL,
                        SALT VARCHAR(100) NOT NULL,
                        PRIMARY KEY(NICKNAME)
                    );""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_data (
                        USER VARCHAR(21),
                        MONEY_NONCE VARCHAR(100) NOT NULL,
                        EMAIL_NONCE VARCHAR(100) NOT NULL,
                        NAME_NONCE VARCHAR(100) NOT NULL,
                        SURNAME1_NONCE VARCHAR(100) NOT NULL,
                        KEY_USED VARCHAR(100) NOT NULL,
                        NONCE_MASTER_KEY VARCHAR(100) NOT NULL,
                        PRIMARY KEY(USER),
                        FOREIGN KEY(USER) references USUARIOS(NICKNAME) ON DELETE CASCADE
                    );""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_info (
                        USER VARCHAR(21),
                        MONEY NUMERIC(10,2),
                        EMAIL VARCHAR(50),
                        NAME VARCHAR(30),
                        SURNAME1 VARCHAR(50),
                        PRIMARY KEY(USER),
                        FOREIGN KEY(USER) references USUARIOS(NICKNAME) ON DELETE CASCADE
                    );""")


