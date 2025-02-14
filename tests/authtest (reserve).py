from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("login_url")  # Посилання на сторінку входу

try:

    # Заповнення форми входу
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys("user")  # Замініть на ім'я користувача
    password_input.send_keys("password")  # Замініть на пароль

    # Відправка форми
    password_input.send_keys(Keys.RETURN)
    time.sleep(5) 

    # Перевірка, чи користувач увійшов в систему
    assert "DreamKeys" in driver.title

finally:
    driver.quit()