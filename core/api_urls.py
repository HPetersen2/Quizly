from django.urls import path, include

"""Defines URL patterns that include routes from the authentication and quiz app APIs."""
urlpatterns = [
    path('', include('auth_app.api.urls')),
    path('', include('quiz_app.api.urls')),
]
