import sqlite3
#a mamar
conn = sqlite3.connect('app_database.db')
def insert_new_user(username,pwd):
    cursor = conn.cursor()
    sql_query = f"INSERT INTO usuarios(nickname,password) values ('{username}','{pwd}');"
    cursor.execute(sql_query)

def search_user(username: str) -> bool:
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM usuarios WHERE nickname = '{username}';"
    cursor.execute(sql_query)
    info = cursor.fetchall()
    return len(info) > 0
def get_acc_money(username):
    cursor = conn.cursor()
    sql_query = f"SELECT money FROM user_info WHERE USER = '{username}';"
    info= cursor.fetchall()
    print(info)
def modify_money(username,new_money):
    cursor = conn.cursor()
    money = str(new_money)
    sql_statement = f"UPDATE user_info SET money = {money} WHERE nickname = '{username}';"
