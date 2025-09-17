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
        
class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get('access_token')
        if not access_token:
            return None

        request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'

        return super().authenticate(request)

class IsQuizOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            print("Benutzer nicht authentifiziert in has_object_permission")
        if request.user != obj.owner:
            print(f"Benutzer {request.user} ist nicht Besitzer von {obj}")
        return request.user == obj.owner
            
