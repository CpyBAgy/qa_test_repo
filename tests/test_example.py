"""
Пример теста - используйте как образец.
"""
import pytest
from model_bakery import baker


@pytest.mark.django_db
class TestExample:

    def test_user_fixture_works(self, user):
        """Проверяет, что фикстура user работает."""
        assert user.username == 'testuser'

    def test_auth_client_works(self, auth_client, user):
        """Проверяет, что аутентифицированный клиент работает."""
        # Создаём урок для этого пользователя
        baker.make('lessons.Lesson', author=user, title='Test Lesson')

        response = auth_client.get('/api/lessons/')
        assert response.status_code == 200
        assert len(response.data) == 1
