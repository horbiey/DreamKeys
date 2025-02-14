import mysql.connector
from mysql.connector import errorcode
import hashlib
import os
import secrets

# Функция для хэширования паролей
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Установите соединение с MySQL
try:
    connection = mysql.connector.connect(
        host="",  # Замените на ваш хост
        port=3306,   # Замените на ваш порт(скорее всего 3306)
        user="",       # Замените на вашего пользователя MySQL
        password="",       # Введите пароль для MySQL
        database="user_auth_db"
    )
    cursor = connection.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Неверный логин или пароль.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("База данных не существует.")
    else:
        print(err)
    exit()

# Создаем базу данных (если её нет)
def create_database():
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS user_auth_db")
        connection.database = "user_auth_db"
    except mysql.connector.Error as err:
        print(f"Ошибка при создании базы данных: {err}")

# Создаем таблицу пользователей (если её нет)
def create_table():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                login VARCHAR(50) NOT NULL UNIQUE,
                password_hash VARCHAR(64) NOT NULL,
                phone_number VARCHAR(15),
                token VARCHAR(64) UNIQUE
            )
        ''')
        print("Таблица пользователей создана.")
    except mysql.connector.Error as err:
        print(f"Ошибка при создании таблицы: {err}")

# Регистрация пользователя
def register_user(login, password, phone_number):
    try:
        password_hash = hash_password(password)
        token = secrets.token_hex(32)  # Генерируем токен
        cursor.execute(
            "INSERT INTO users (login, password_hash, phone_number, token) VALUES (%s, %s, %s, %s)",
            (login, password_hash, phone_number, token)
        )
        connection.commit()
        return token
    except mysql.connector.Error as err:
        return None

# Авторизация пользователя
def authenticate_user(login, password):
    try:
        password_hash = hash_password(password)
        cursor.execute(
            "SELECT id, token FROM users WHERE login = %s AND password_hash = %s",
            (login, password_hash)
        )
        user = cursor.fetchone()
        if user:
            return user[1]  # Возвращаем токен
        else:
            return None
    except mysql.connector.Error as err:
        return None

# Основная логика
if __name__ == "__main__":

    while True:
        print("\n1. Регистрация\n2. Авторизация\n3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            login = input("Введіть логін: ")
            password = input("Введіть пароль: ")
            phone_number = input("Введіть номер телефона: ")
            token = register_user(login, password, phone_number)
            if token:
                print(f"Ваш токен: {token}")

        elif choice == "2":
            login = input("Введіть логін: ")
            password = input("Введіть пароль: ")
            token = authenticate_user(login, password)
            if token:
                print(f"Ваш токен: {token}")
        else:
            print("Неверный выбор. Попробуйте снова.")

# Закрываем соединение
cursor.close()
connection.close()
