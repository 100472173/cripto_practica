import sqlite3
from database_management import master_key
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

# a mamar
conn = sqlite3.connect('../database_management/app_database.db')
"""Definir nonce y clave para usar"""
nonce_master = master_key.DATA['NONCE']
master_key = master_key.DATA['KEY']

def master_key_encrypt(data):
    global nonce_master, master_key
    print("Key original es",data)
    master_chacha = ChaCha20Poly1305(master_key)
    encrypted_key = master_chacha.encrypt(nonce_master, data, None)
    return encrypted_key


def master_key_decrypt(encrypted_data):
    print(encrypted_data)
    global nonce_master, master_key
    master_chacha = ChaCha20Poly1305(master_key)
    print("data es",type(encrypted_data))
    decrypted_key = master_chacha.decrypt(nonce_master, encrypted_data, None)
    print(decrypted_key)
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
    key = os.urandom(32)
    chacha = ChaCha20Poly1305(key)
    nonce_data = os.urandom(12)
    encrypted_money = chacha.encrypt(nonce_data, str(money).encode('UTF-8'), None)
    encrypted_email = chacha.encrypt(nonce_data, email.encode('UTF-8'), None)
    encrypted_name = chacha.encrypt(nonce_data, name.encode('UTF-8'), None)
    encrypted_surname1 = chacha.encrypt(nonce_data, surname1.encode('UTF-8'), None)
    encrypted_key = master_key_encrypt(key)
    cursor = conn.cursor()
    sql_query = f"INSERT INTO user_info(user, money, email, name, surname1, key_used, nonce) values (?,?,?,?,?,?,?);"
    valores_insert = [username,encrypted_money,encrypted_email,encrypted_name,encrypted_surname1,encrypted_key,nonce_data]
    cursor.execute(sql_query,valores_insert)
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
    sql_query = f"SELECT money, key_used, nonce FROM user_info WHERE USER = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    key = ChaCha20Poly1305(master_key_decrypt(info[0][1]))
    money = key.decrypt(info[0][2], info[0][0], None)
    return float(money.decode('utf-8'))

def encrypt_money(username, money):
    cursor = conn.cursor()
    sql_query = f"SELECT key_used, nonce FROM user_info WHERE USER = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    key = ChaCha20Poly1305(master_key_decrypt(info[0][0]))
    encrypted_money = key.encrypt(info[0][1], str(money).encode('UTF-8'), None)
    return encrypted_money

def query():
    cursor = conn.cursor()
    sql_query = f"SELECT * from user_info;"
    info = cursor.fetchall()
    print(info)


def modify_money(username, new_money, operation_type):
    cursor = conn.cursor()
    current_money = get_acc_money(username)
    if operation_type == "ingreso":
        money = current_money + int(new_money)
        if money > 9999999:
            money = 9999999
    elif operation_type == "retirada":
        money = current_money - int(new_money)
        if money < 0:
            money = 0
    encrypted_money = encrypt_money(username, money)
    sql_statement = f"UPDATE user_info SET money = ? WHERE user = ?;"
    update_data = [encrypted_money, username]
    cursor.execute(sql_statement,update_data)
    commit_changes()

def decrypt_user_info(username):
    cursor = conn.cursor()
    sql_query = f"SELECT money, email, name, surname1, key_used, nonce from user_info where user = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    #return info[0][0], info[0][1], info[0][2], info[0][3], info [0][4]
    key = ChaCha20Poly1305(master_key_decrypt(info[0][4]))
    money = key.decrypt(info[0][5],info[0][0], None)
    email = key.decrypt(info[0][5],info[0][1], None)
    name = key.decrypt(info[0][5],info[0][2], None)
    surname1 = key.decrypt(info[0][5],info[0][3], None)
    return money,email,name,surname1



def get_user_info(username):
    money, email, name, surname = decrypt_user_info(username)
    return float(money.decode('utf-8')), email.decode('utf-8'), name.decode('utf-8'), surname.decode('utf-8')

