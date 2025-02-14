from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

try:
    # Відкриваємо сторінку подачі оголошення
    driver.get("http://localhost/listings/new/")  # Змінити на правильний URL

    # Заповнюємо форму
    title_input = driver.find_element(By.ID, "title")
    title_input.send_keys("Тестове оголошення")

    # Завантажуємо зображення
    photos_input = driver.find_element(By.ID, "photos")
    photos_input.send_keys("/path/to/photo1.jpg")  # Змінити на правильний шлях до зображення
    photos_input.send_keys("/path/to/photo2.jpg")  # Змінити на правильний шлях до зображення

    description_input = driver.find_element(By.ID, "description")
    description_input.send_keys("Опис тестового оголошення")

    location_input = driver.find_element(By.ID, "location")
    location_input.send_keys("Київ, 01001")

    # Заповнюємо контактні дані
    contact_name_input = driver.find_element(By.ID, "contact-name")
    contact_name_input.send_keys("Тестовий Контакт")

    phone_input = driver.find_element(By.ID, "phone")
    phone_input.send_keys("123456789")

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("test@example.com")

    # Подаємо форму
    submit_button = driver.find_element(By.XPATH, "//button[text()='Опублікувати оголошення']")
    submit_button.click()

    time.sleep(5) 

    # Перевіряємо, чи оголошення було успішно подано
    success_message = driver.find_element(By.XPATH, "//h2[contains(text(), 'Оголошення успішно подано')]")
    assert success_message.is_displayed()

finally:
    driver.quit()