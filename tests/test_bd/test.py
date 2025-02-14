import unittest
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestUserAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # або інший драйвер
        cls.driver.get("http://localhost")  # URL вашого API

        # Налаштування з'єднання з базою даних
        cls.connection = mysql.connector.connect(
            host="",  # Ваш хост
            port=3306,
            user="",  # Ваш користувач
            password="",  # Ваш пароль
            database="user_auth_db"
        )
        cls.cursor = cls.connection.cursor()

    def test_register_user(self):
        driver = self.driver
        # Тест реєстрації
        driver.find_element(By.NAME, "login").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("testpassword")
        driver.find_element(By.NAME, "phone_number").send_keys("1234567890")
        driver.find_element(By.NAME, "submit").click()

        # Перевірка, чи токен згенеровано
        time.sleep(2)
        token = driver.find_element(By.ID, "token").text
        self.assertIsNotNone(token)

        # Перевірка в базі даних
        self.cursor.execute("SELECT * FROM users WHERE login = %s", ("testuser",))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)

    def test_authenticate_user(self):
        driver = self.driver
        # Тест авторизації
        driver.find_element(By.NAME, "login").send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("testpassword")
        driver.find_element(By.NAME, "submit").click()

        # Перевірка, чи токен згенеровано
        time.sleep(2)
        token = driver.find_element(By.ID, "token").text
        self.assertIsNotNone(token)

    @classmethod
    def tearDownClass(cls):
        # Закриття з'єднання з базою даних
        cls.cursor.close()
        cls.connection.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()