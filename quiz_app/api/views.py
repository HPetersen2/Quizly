from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import CreateQuizSerializer
from services.quiz_service import create_quiz_from_video

class CreateQuizView(generics.CreateAPIView):
    serializer_class = CreateQuizSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        url = request.data.get('url')
        if not url:
            return Response({'error': 'URL is required.'}, status=status.HTTP_400_BAD_REQUEST)

        quiz_data = create_quiz_from_video(url)

        serializer = self.get_serializer(data=quiz_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)