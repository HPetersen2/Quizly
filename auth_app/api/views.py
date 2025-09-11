from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            data = {
                'username': saved_account.username,
                'email': saved_account.email,
                'user_id': saved_account.pk
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello World'})
    
class CookieTokenObtainView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get("refresh")
        access = response.data.get("access")

        response.set_cookie(
            key="access_token",
            value=access,
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        response.set_cookie(
            key="refresh_token",
            value=refresh,
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        response.data = { 'message': 'Login successfully!'}
        return response
    
class CookieRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token is None:
            return Response(
                {"detail": "Refresh token not found!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        serializer = self.get_serializer(data={"refresh":refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response(
                {"detail": "Refresh token invalid!"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        
        access_token = serializer.validated_data.get("access")

        response = Response({"message": "Access Token refreshed"})
        response.set_cookie(
            key="access_token",
            value=access,
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        return response
    
class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        refresh = serializer.validated_data["refresh"]
        access = serializer.validated_data["access"]

        response = Response({"message": "Login successful!"}, status=status.HTTP_200_OK)

        response.set_cookie(
            key="access_token",
            value=str(access),
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        return response