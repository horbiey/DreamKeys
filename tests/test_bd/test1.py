import unittest
import mysql.connector
from mysql.connector import errorcode
import hashlib
import os
import secrets

# Клас для автотестів бази даних
class TestDatabase(unittest.TestCase):
    # Метод для встановлення з'єднання з базою даних перед кожним автотестом
    def setUp(self):
        # Встановлюємо параметри з'єднання з базою даних
        self.host = "your_host"
        self.port = 3306
        self.user = "your_user"
        self.password = "your_password"
        self.database = "user_auth_db"

        try:
            # Встановлюємо з'єднання з базою даних
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            # Створюємо курсор для виконання запитів до бази даних
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            # Якщо виникла помилка під час встановлення з'єднання, автотест вважається невдалим
            self.fail("Failed to connect to database: {}".format(err))

    # Метод для закриття з'єднання з базою даних після кожного автотесту
    def tearDown(self):
        # Закриваємо курсор
        self.cursor.close()
        # Закриваємо з'єднання з базою даних
        self.connection.close()

    # Автотест для створення бази даних
    def test_create_database(self):
        try:
            # Виконуємо запит для створення бази даних
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS user_auth_db")
            # Встановлюємо базу даних для подальшої роботи
            self.connection.database = "user_auth_db"
        except mysql.connector.Error as err:
            # Якщо виникла помилка під час створення бази даних, автотест вважається невдалим
            self.fail("Failed to create database: {}".format(err))

    # Автотест для створення таблиці користувачів
    def test_create_table(self):
        try:
            # Виконуємо запит для створення таблиці користувачів
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    login VARCHAR(50) NOT NULL UNIQUE,
                    password_hash VARCHAR(64) NOT NULL,
                    phone_number VARCHAR(15),
                    token VARCHAR(64) UNIQUE
                )
            ''')
        except mysql.connector.Error as err:
            # Якщо виникла помилка під час створення таблиці користувачів, автотест вважається невдалим
            self.fail("Failed to create table: {}".format(err))

    # Автотест для реєстрації користувача
    def test_register_user(self):
        # Встановлюємо дані для реєстрації користувача
        login = "test_user"
        password = "test_password"
        phone_number = "1234567890"
        token = secrets.token_hex(32)

        try:
            # Виконуємо запит для реєстрації користувача
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.cursor.execute(
                "INSERT INTO users (login, password_hash, phone_number, token) VALUES (%s, %s, %s, %s)",
                (login, password_hash, phone_number, token)
            )
            # Встановлюємо зміни в базі даних
            self.connection.commit()
        except mysql.connector.Error as err:
            # Якщо виникла помилка під час реєстрації користувача, автотест вважається невдалим
            self.fail("Failed to register user: {}".format(err))

    # Автотест для автентифікації користувача
    def test_authenticate_user(self):
        # Встановлюємо дані для автентифікації користувача
        login = "test_user"
        password = "test_password"

        try:
            # Виконуємо запит для автентифікації користувача
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.cursor.execute(
                "SELECT id, token FROM users WHERE login = %s AND password_hash = %s",
                (login, password_hash)
            )
            # Отримуємо результат автентифікації
            user = self.cursor.fetchone()
            # Перевіряємо, чи успішна автентифікація
            self.assertIsNotNone(user)
        except mysql.connector.Error as err:
            # Якщо виникла помилка під час автентифікації користувача, автотест вважається невдалим
            self.fail("Failed to authenticate user: {}".format(err))

# Виконуємо автотести
if __name__ == "__main__":
    unittest.main()