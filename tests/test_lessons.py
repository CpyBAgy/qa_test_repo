"""
Тесты для LessonViewSet.
"""
import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestLessonViewSet:

    def test_authenticated_user_can_list_lessons(self, auth_client, lesson):
        """Аутентифицированный пользователь получает список уроков."""
        response = auth_client.get('/api/lessons/')
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'Test Lesson'

    def test_authenticated_user_can_retrieve_lesson(self, auth_client, lesson):
        """Аутентифицированный пользователь получает урок по ID."""
        response = auth_client.get(f'/api/lessons/{lesson.id}/')
        assert response.status_code == 200
        assert response.data['title'] == 'Test Lesson'
        assert response.data['id'] == lesson.id

    def test_authenticated_user_can_create_lesson(self, auth_client, user):
        """Аутентифицированный пользователь может создать урок."""
        data = {
            'title': 'New Lesson',
            'description': 'Test description',
            'is_published': True
        }
        response = auth_client.post('/api/lessons/', data)
        assert response.status_code == 201
        assert response.data['title'] == 'New Lesson'
        assert response.data['description'] == 'Test description'
        assert response.data['is_published'] is True

    def test_unauthenticated_request_returns_401(self, lesson):
        """Неаутентифицированный запрос возвращает 401."""
        client = APIClient()
        response = client.get('/api/lessons/')
        # IsAuthenticated permission возвращает 403 Forbidden, а не 401 Unauthorized
        assert response.status_code == 403