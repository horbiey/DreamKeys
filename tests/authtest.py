from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

try:
    # Відкриття сторінки входу
    driver.get("http://localhost/login/")  # Змініть URL на ваш локальний або тестовий

    time.sleep(2)

    # Заповнення форми входу
    username_input = driver.find_element(By.NAME, "username")  # Змініть на правильне ім'я поля
    password_input = driver.find_element(By.NAME, "password")  # Змініть на правильне ім'я поля

    username_input.send_keys("testuser")  # Введіть тестове ім'я користувача
    password_input.send_keys("password")    # Введіть тестовий пароль

    # Надсилання форми
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)

    # Перевірка успішного входу
    assert "Welcome" in driver.page_source  # Змініть на текст, який з'являється після успішного входу

    print("Тест пройдено: Успішний вхід на сайт.")

except Exception as e:
    print(f"Тест не пройдено: {e}")

finally:
    driver.quit()