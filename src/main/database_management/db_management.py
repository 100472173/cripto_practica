import sqlite3

# a mamar
conn = sqlite3.connect('app_database.db')


def insert_new_user(username, pwd):
    """falta generar el token y el salt"""
    cursor = conn.cursor()
    sql_query = f"INSERT INTO usuarios(nickname,password) values ('{username}','{pwd}');"
    cursor.execute(sql_query)
    commit_changes()


def insert_new_user_details(username, money, email, name, surname1, surname2):
    cursor = conn.cursor()
    sql_query = f"INSERT INTO user_info(user, money, email, name, surname1, surname2) values ('{username}','{money}', " \
                f"'{email}','{name}','{surname1}','{surname2}');"
    cursor.execute(sql_query)
    commit_changes()

def commit_changes():
    cursor = conn.cursor()
    sql_statement= f"commit;"
    cursor.execute(sql_statement)

def search_user(username: str) -> bool:
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM usuarios WHERE nickname = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    return len(info) > 0

def delete_user(username: str):
    cursor = conn.cursor()
    if search_user(username):
        sql_statement = f"DELETE FROM usuarios WHERE nickname = '{username}';"
        cursor.execute(sql_statement)
        commit_changes()
    else:
        print("Usuario no esta registrado en la base de datos")

def get_acc_money(username):
    cursor = conn.cursor()
    sql_query = f"SELECT money FROM user_info WHERE USER = '{username}';"
    info = cursor.fetchall()
    print(info)

def query():
    cursor = conn.cursor()
    sql_query = f"SELECT * from user_info;"
    info = cursor.fetchall()
    print(info)



def modify_money(username, new_money):
    cursor = conn.cursor()
    money = str(new_money)
    sql_statement = f"UPDATE user_info SET money = {money} WHERE nickname = '{username}';"
    commit_changes()
