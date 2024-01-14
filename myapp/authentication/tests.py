from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTests(TestCase):

    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login_view(self):
        # Проверяем, что страница входа возвращает код 200
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Проверяем, что аутентификация происходит успешно
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # 302 - перенаправление после успешной аутентификации
        self.assertTrue(self.client.session['_auth_user_id'])

    def test_logout_view(self):
        # Входим в систему
        self.client.login(username='testuser', password='testpassword')

        # Проверяем, что страница выхода возвращает код 200
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)

        # Проверяем, что выход из системы происходит успешно
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # 302 - перенаправление после успешного выхода из системы
        self.assertFalse(self.client.session.get('_auth_user_id'))
