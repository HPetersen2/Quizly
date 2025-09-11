from django.urls import path
from .views import RegistrationView, CookieTokenObtainView, CookieRefreshView, TokenBlacklistView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register-view'),
    path('login/', CookieTokenObtainView.as_view(), name='login-view'),
    path('logout/', TokenBlacklistView.as_view(), name='token-blacklist'),
    path('token/refresh/', CookieRefreshView.as_view(), name='token-refresh'),
]
