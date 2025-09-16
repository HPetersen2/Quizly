from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class IsAuthenticatedFromCookie(BasePermission):
    def has_permission(self, request, view):
        jwt_authenticator = JWTAuthentication()

        access_token = request.COOKIES.get('access_token')
        if not access_token:
            return False

        try:
            validated_token = jwt_authenticator.get_validated_token(access_token)
            user = jwt_authenticator.get_user(validated_token)

            request.user = user

            return user is not None and user.is_authenticated

        except (InvalidToken, TokenError):
            return False
        except Exception:
            return False

class IsQuizOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return request.user == obj.owner
        except AttributeError:
            return False
            
