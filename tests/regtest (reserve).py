from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('reg_url')  # Посилання на сторінку реєстрації

# Заповнення форми реєстрації
username = driver.find_element(By.NAME, 'username')
username.send_keys('testuser') # Замініть на ім'я користувача

email = driver.find_element(By.NAME, 'email')
email.send_keys('testuser@example.com') # Замініть на email

password = driver.find_element(By.NAME, 'password')
password.send_keys('TestPassword123') #  Замініть на пароль

# Відправка форми
password.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()