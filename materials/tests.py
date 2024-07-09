from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


# Create your tests here.
class MaterialsTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="admin1@admin.ru")
        self.course = Course.objects.create(name="Мемология", description="хорошо")
        self.lesson = Lesson.objects.create(name="Джимми", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тестирование создания урока"""
        data = {
            "name": "Test",
            "description": "Test"
        }
        response = self.client.post(
            "/lesson/create/",
            data=data
        )
        print(response)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_retrieve(self):
        """Тестирование просмотра урока"""
        url = reverse("materials:lesson-get", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_update(self):
        """Тестирование редактирования урока"""
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        response = self.client.patch(url)
        data = {
            "name": "Test"
        }
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Test"
        )

    def test_lesson_delete(self):
        """Тестирование удаления урока"""
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        """Тестирование просмотра списка уроков"""
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.pk, 'name': self.lesson.name, 'description': '', 'preview': None, 'slug': None,
                 'course': self.course.pk, 'owner': self.user.pk}]
        }
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class SubscriptionCreateAPIViewTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="admin1@admin.ru")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name="Мемология", description="хорошо")
        self.lesson = Lesson.objects.create(name="Джимми", course=self.course, owner=self.user)
        self.url = reverse("materials:subscriptions")

    def test_create_subscription(self):
        response = self.client.post(self.url, {'course': self.course.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка успешно создана')
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_delete_subscription(self):
        Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.post(self.url, {'course': self.course.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка успешно удалена')
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_create_subscription_without_authentication(self):
        self.client.logout()
        response = self.client.post(self.url, {'course': self.course.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


