from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя для тестирования
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем задачу для тестирования
        self.task = Task.objects.create(title='Test Task', description='This is a test task', assigned_to=self.user)

    def test_task_list_view(self):
        # Проверяем, что страница списка задач возвращает статус 200
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')  # Проверяем, что созданная задача отображается на странице

    def test_task_detail_view(self):
        # Проверяем, что страница детального просмотра задачи возвращает статус 200
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')  # Проверяем, что название задачи отображается на странице

    def test_task_create_view(self):
        # Проверяем, что страница создания задачи возвращает статус 200
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)

    def test_task_update_view(self):
        # Проверяем, что страница обновления задачи возвращает статус 200
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('task_update', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)

    def test_task_delete_view(self):
        # Проверяем, что задача удаляется при переходе по странице удаления
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(title='Test Task').exists())