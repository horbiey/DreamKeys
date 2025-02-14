from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    # Відкриваємо головну сторінку
    driver.get("http://localhost")  # Змінити на правильний URL

    # Знаходимо перше оголошення у списку
    first_listing = driver.find_element(By.XPATH, "//ul/li[1]/a")  # Змінити на правильний XPath
    first_listing_title = first_listing.text  # Зберігаємо заголовок оголошення

    # Клікаємо на перше оголошення
    first_listing.click()

    time.sleep(5)

    # Перевіряємо, чи заголовок на сторінці деталей відповідає заголовку оголошення
    detail_title = driver.find_element(By.TAG_NAME, "h2").text  # Змінити на правильний тег заголовка
    assert detail_title == first_listing_title, f"Заголовок на сторінці деталей '{detail_title}' не відповідає заголовку '{first_listing_title}'"

    # Перевіряємо, чи відображається ціна
    price = driver.find_element(By.XPATH, "//p[contains(text(), 'Ціна:')]").text  # Змінити на правильний XPath
    assert price, "Ціна не відображається на сторінці деталей"

    # Перевіряємо, чи відображається опис
    description = driver.find_element(By.XPATH, "//p[contains(text(), 'Опис:')]").text  # Змінити на правильний XPath
    assert description, "Опис не відображається на сторінці деталей"

finally:
    driver.quit()