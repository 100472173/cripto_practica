import sqlite3
from database_management import master_key
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

# a mamar
conn = sqlite3.connect('../database_management/app_database.db')

"""Definir nonce y clave para usar"""
master_key = master_key.DATA['KEY']


def master_key_encrypt(data):
    global master_key
    master_chacha = ChaCha20Poly1305(master_key)
    master_nonce = os.urandom(12)
    encrypted_key = master_chacha.encrypt(master_nonce, data, None)
    return encrypted_key, master_nonce


def master_key_decrypt(encrypted_data, nonce_data):
    global master_key
    master_chacha = ChaCha20Poly1305(master_key)
    decrypted_key = master_chacha.decrypt(nonce_data, encrypted_data, None)
    return decrypted_key


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
    (encrypted_email, encrypted_money, encrypted_name, encrypted_surname1, money_nonce, email_nonce, name_nonce,
     surname1_nonce, encrypted_key, nonce_encrypted_key) = encrypt_user_info(email, money, name, surname1)
    cursor = conn.cursor()
    sql_user_info = f"INSERT INTO user_info (USER, MONEY, EMAIL, NAME, SURNAME1) VALUES (?, ?, ?, ?, ?)"
    sql_user_data = f"INSERT INTO user_data (USER, MONEY_NONCE, EMAIL_NONCE, NAME_NONCE, SURNAME1_NONCE, KEY_USED, NONCE_MASTER_KEY) VALUES (?, ?, ?, ?, ?, ?, ?)"
    valores_user_info = [username, encrypted_money, encrypted_email, encrypted_name, encrypted_surname1]
    valores_user_data = [username, money_nonce, email_nonce, name_nonce, surname1_nonce, encrypted_key, nonce_encrypted_key]
    cursor.execute(sql_user_info, valores_user_info)
    cursor.execute(sql_user_data, valores_user_data)
    commit_changes()


def encrypt_user_info(email, money, name, surname1):
    key = os.urandom(32)
    chacha = ChaCha20Poly1305(key)
    nonce_data = [os.urandom(12) for _ in range(4)]
    money_nonce, email_nonce, name_nonce, surname1_nonce = nonce_data[0], nonce_data[1], nonce_data[2], nonce_data[3]
    encrypted_money = chacha.encrypt(money_nonce, str(money).encode('UTF-8'), None)
    encrypted_email = chacha.encrypt(email_nonce, email.encode('UTF-8'), None)
    encrypted_name = chacha.encrypt(name_nonce, name.encode('UTF-8'), None)
    encrypted_surname1 = chacha.encrypt(surname1_nonce, surname1.encode('UTF-8'), None)
    encrypted_key, nonce_encrypted_key = master_key_encrypt(key)
    return (encrypted_email, encrypted_money, encrypted_name, encrypted_surname1, money_nonce, email_nonce,
            name_nonce, surname1_nonce, encrypted_key, nonce_encrypted_key)


def search_user(username: str) -> bool:
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM usuarios WHERE nickname = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    return len(info) > 0


def delete_user(username: str):
    cursor = conn.cursor()
    if search_user(username):
        sql_statement1 = f"DELETE FROM user_data WHERE user = '{username}';"
        cursor.execute(sql_statement1)
        sql_statement2 = f"DELETE FROM user_info WHERE user = '{username}';"
        cursor.execute(sql_statement2)
        sql_statement3 = f"DELETE FROM usuarios WHERE nickname = '{username}';"
        cursor.execute(sql_statement3)
        commit_changes()
    else:
        print("Usuario no esta registrado en la base de datos")


def get_acc_money(username):
    encrypted_money = obtain_encrypted_money(username)
    money_nonce = obtain_money_nonce(username)
    mk_nonce = obtain_mk_nonce(username)
    key_used = obtain_key(username)
    key = ChaCha20Poly1305(master_key_decrypt(key_used, mk_nonce))
    money = key.decrypt(money_nonce, encrypted_money, None)
    return float(money.decode('utf-8'))


def obtain_encrypted_money(username):
    cursor = conn.cursor()
    query_money = f"SELECT money FROM user_info WHERE USER = '{username}';"
    cursor.execute(query_money)
    info = cursor.fetchall()
    obtained_money = info[0][0]
    return obtained_money


def obtain_money_nonce(username):
    cursor = conn.cursor()
    query_money = f"SELECT money_nonce FROM user_data WHERE USER = '{username}';"
    cursor.execute(query_money)
    info = cursor.fetchall()
    obtained_money = info[0][0]
    return obtained_money


def obtain_key(username):
    cursor = conn.cursor()
    query_money = f"SELECT key_used FROM user_data WHERE USER = '{username}';"
    cursor.execute(query_money)
    info = cursor.fetchall()
    obtained_key = info[0][0]
    return obtained_key


def obtain_mk_nonce(username):
    cursor = conn.cursor()
    query_money = f"SELECT nonce_master_key FROM user_data WHERE USER = '{username}';"
    cursor.execute(query_money)
    info = cursor.fetchall()
    obtained_nonce_mk = info[0][0]
    return obtained_nonce_mk


def encrypt_money(username, money):
    key_used = obtain_key(username)
    mk_nonce = obtain_mk_nonce(username)
    nonce = os.urandom(12)
    key = ChaCha20Poly1305(master_key_decrypt(key_used, mk_nonce))
    encrypted_money = key.encrypt(nonce, str(money).encode('UTF-8'), None)
    return encrypted_money, nonce


def modify_money(username, new_money, operation_type):
    current_money = get_acc_money(username)
    money = set_new_money(current_money, new_money, operation_type)
    encrypted_money, nonce_money = encrypt_money(username, money)
    update_money(encrypted_money, username)
    update_nonce(nonce_money,username)


def set_new_money(current_money, new_money, operation_type):
    if operation_type == "ingreso":
        money = current_money + round(float(new_money),2)
        if money > 9999999:
            money = 9999999
    elif operation_type == "retirada":
        money = current_money - round(float(new_money),2)
        if money < 0:
            money = 0
    else:
        money = 0
    return money


def update_money(encrypted_money, username):
    cursor = conn.cursor()
    sql_statement = f"UPDATE user_info SET money = ? WHERE user = ?;"
    update_data = [encrypted_money, username]
    cursor.execute(sql_statement, update_data)
    commit_changes()


def update_nonce(new_nonce, username):
    cursor = conn.cursor()
    sql_statement = f"UPDATE user_data SET money_nonce = ? WHERE user = ?;"
    update_data = [new_nonce, username]
    cursor.execute(sql_statement, update_data)
    commit_changes()


def _decrypt_user_info(username):
    encrypted_money, encrypted_email, encrypted_name, encrypted_surname1 = obtain_user_info(username)
    money_nonce, email_nonce, name_nonce, surname1_nonce = obtain_user_nonces(username)
    key_used = obtain_key(username)
    mk_nonce = obtain_mk_nonce(username)
    key = ChaCha20Poly1305(master_key_decrypt(key_used, mk_nonce))
    money = key.decrypt(money_nonce, encrypted_money, None)
    email = key.decrypt(email_nonce, encrypted_email, None)
    name = key.decrypt(name_nonce, encrypted_name, None)
    surname1 = key.decrypt(surname1_nonce, encrypted_surname1, None)
    return money, email, name, surname1


def obtain_user_info(username):
    cursor = conn.cursor()
    sql_query = f"SELECT money, email, name, surname1 from user_info where user = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    return info[0][0], info[0][1], info[0][2], info[0][3]


def obtain_user_nonces(username):
    cursor = conn.cursor()
    sql_query = f"SELECT money_nonce, email_nonce, name_nonce, surname1_nonce from user_data where user = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    return info[0][0], info[0][1], info[0][2], info[0][3]


def get_user_info(username):
    money, email, name, surname = _decrypt_user_info(username)
    return float(money.decode('utf-8')), email.decode('utf-8'), name.decode('utf-8'), surname.decode('utf-8')


def commit_changes():
    cursor = conn.cursor()
    sql_statement = f"commit;"
    cursor.execute(sql_statement)
