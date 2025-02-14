import unittest
import requests

class TestUserAuthAPI(unittest.TestCase):

    BASE_URL = "http://localhost"  # Змініть на URL вашого API

    def test_register_user(self):
        # Тест реєстрації користувача
        payload = {
            "login": "testuser",
            "password": "testpassword",
            "phone_number": "1234567890"
        }
        response = requests.post(f"{self.BASE_URL}/register", json=payload)
        
        # Перевірка статусу відповіді
        self.assertEqual(response.status_code, 201)  # 201 Created
        self.assertIn("token", response.json())  # Перевірка наявності токена

    def test_authenticate_user(self):
        # Тест авторизації користувача
        payload = {
            "login": "testuser",
            "password": "testpassword"
        }
        response = requests.post(f"{self.BASE_URL}/authenticate", json=payload)
        
        # Перевірка статусу відповіді
        self.assertEqual(response.status_code, 200)  # 200 OK
        self.assertIn("token", response.json())  # Перевірка наявності токена

    def test_register_user_duplicate(self):
        # Тест реєстрації користувача з уже існуючим логіном
        payload = {
            "login": "testuser",
            "password": "testpassword",
            "phone_number": "1234567890"
        }
        response = requests.post(f"{self.BASE_URL}/register", json=payload)
        
        # Перевірка статусу відповіді
        self.assertEqual(response.status_code, 400)  # 400 Bad Request
        self.assertIn("error", response.json())  # Перевірка наявності повідомлення про помилку

    def test_authenticate_user_invalid(self):
        # Тест авторизації з неправильними даними
        payload = {
            "login": "invaliduser",
            "password": "wrongpassword"
        }
        response = requests.post(f"{self.BASE_URL}/authenticate", json=payload)
        
        # Перевірка статусу відповіді
        self.assertEqual(response.status_code, 401)  # 401 Unauthorized
        self.assertIn("error", response.json())  # Перевірка наявності повідомлення про помилку

if __name__ == "__main__":
    unittest.main()