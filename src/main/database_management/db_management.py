import sqlite3
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

# a mamar
conn = sqlite3.connect('../database_management/app_database.db')


def generate_token(pwd):
    salt = os.urandom(16)
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2 ** 14,
        r=8,
        p=1,
    )
    token = kdf.derive(bytes(pwd, 'UTF-8'))
    return token, salt


def get_token_salt(username):
    cursor = conn.cursor()
    sql_query = f"SELECT pwd_token, salt FROM usuarios WHERE nickname = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    return (info[0][0]), (info[0][1])


def verify_user_password(username, pwd):
    pwd_token, salt = get_token_salt(username)
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2 ** 14,
        r=8,
        p=1,
    )
    kdf.verify(bytes(pwd, 'ASCII'), pwd_token)


def insert_new_user(username, pwd):
    cursor = conn.cursor()
    token, salt = generate_token(pwd)
    sql_query = f"INSERT INTO usuarios(nickname,pwd_token,salt) values (?,?,?);"
    valores_insert = [username, token, salt]
    cursor.execute(sql_query, valores_insert)
    commit_changes()


def insert_new_user_details(username: str, money: float, email: str, name: str, surname1: str) -> None:
    cursor = conn.cursor()
    sql_query = f"INSERT INTO user_info(user, money, email, name, surname1) values ('{username}','{money}', " \
                f"'{email}','{name}','{surname1}');"
    cursor.execute(sql_query)
    commit_changes()


def commit_changes():
    cursor = conn.cursor()
    sql_statement = f"commit;"
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


def modify_money(username, new_money, operation_type):
    cursor = conn.cursor()
    sql_query = f"SELECT money from user_info where user = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    current_money = info[0][0]
    if operation_type == "ingreso":
        money = current_money + int(new_money)
        if money > 9999999:
            money = 9999999
    elif operation_type == "retirada":
        money = current_money - int(new_money)
        if money < 0:
            money = 0
    sql_statement = f"UPDATE user_info SET money = {money} WHERE user = '{username}';"
    cursor.execute(sql_statement)
    commit_changes()


def get_user_info(username):
    cursor = conn.cursor()
    sql_query = f"SELECT money, email, name, surname1 from user_info where user = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    return info[0][0], info[0][1], info[0][2], info[0][3]
