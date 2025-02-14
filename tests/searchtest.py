from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

try:
    # Відкриваємо головну сторінку
    driver.get("http://localhost")  # Змінити на правильний URL

    # Заповнюємо форму пошуку
    location_input = driver.find_element(By.ID, "location")  # Змінити на правильний ID
    location_input.send_keys("Київ")  # Введіть місто для пошуку

    rooms_input = driver.find_element(By.ID, "rooms")  # Змінити на правильний ID
    rooms_input.send_keys("Одна")  # Введіть кількість кімнат

    price_input_from = driver.find_element(By.ID, "price_from")  # Змінити на правильний ID
    price_input_from.send_keys("10000")  # Введіть мінімальну ціну

    price_input_to = driver.find_element(By.ID, "price_to")  # Змінити на правильний ID
    price_input_to.send_keys("50000")  # Введіть максимальну ціну

    area_input_from = driver.find_element(By.ID, "area_from")  # Змінити на правильний ID
    area_input_from.send_keys("30")  # Введіть мінімальну площу

    area_input_to = driver.find_element(By.ID, "area_to")  # Змінити на правильний ID
    area_input_to.send_keys("100")  # Введіть максимальну площу

    # Подаємо форму пошуку
    search_button = driver.find_element(By.XPATH, "//button[text()='Шукати']")  # Змінити на правильний текст кнопки
    search_button.click()

    time.sleep(5) 

    # Перевіряємо, чи результати пошуку відображаються
    results = driver.find_elements(By.CLASS_NAME, "card")  # Змінити на правильний клас для карток оголошень
    assert len(results) > 0, "Результати пошуку не знайдено"

    # Додаткові перевірки можна виконати тут, наприклад, перевірка заголовків оголошень
    for result in results:
        title = result.find_element(By.TAG_NAME, "h2").text  # Змінити на правильний тег заголовка
        assert "квартира" in title.lower(), f"Заголовок '{title}' не містить 'квартира'"

finally:
    # Закриваємо драйвер
    driver.quit()