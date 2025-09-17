import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from quiz_app.models import Quiz

@pytest.fixture
def owner():
    owner = User.objects.create_user(username="testowner", password="testpassword")
    return owner

@pytest.fixture
def quiz(owner):
    quiz = Quiz.objects.create(
        title="Test Quiz",
        description="This is a test quiz.",
        owner=owner
    )
    return quiz

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_get_quiz_success(api_client, quiz, owner):
    api_client.force_authenticate(user=owner)

    response = api_client.get(f"/api/quizzes/{quiz.id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == quiz.id
    assert response.data["title"] == quiz.title
    assert response.data["description"] == quiz.description


@pytest.mark.django_db
def test_get_quiz_unauthenticated(api_client, quiz):

    response = api_client.get(f"/api/quizzes/{quiz.id}/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_quiz_forbidden(api_client, quiz, owner):

    another_owner = User.objects.create_user(username="anotherowner", password="password")

    # Hier wird der andere Besitzer zum Authentifizieren verwendet
    api_client.force_authenticate(user=another_owner)

    response = api_client.get(f"/api/quizzes/{quiz.id}/")

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_get_quiz_not_found(api_client, owner):

    api_client.force_authenticate(user=owner)

    response = api_client.get("/api/quizzes/999/")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_quiz_server_error(api_client, owner):

    api_client.force_authenticate(user=owner)

    with pytest.raises(Exception):
        response = api_client.get("/api/quizzes/1/")
        response.raise_for_status()
