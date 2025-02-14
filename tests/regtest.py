from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://localhost/register/')  # URL сторінки реєстрації

# Заповнення форми реєстрації
username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('testuser') # Змініть на своє ім'я користувача

email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('testuser@example.com') # Змініть на свою електронну адресу 

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('password123') # Змініть на свій пароль

# Відправка форми
password_input.send_keys(Keys.RETURN)

time.sleep(3)

# Перевірка результату реєстрації
# Припустимо, що після успішної реєстрації користувач перенаправляється на домашню сторінку
assert "Ласкаво просимо" in driver.page_source  # Змініть текст на той, що відображається на вашій домашній сторінці

driver.quit()