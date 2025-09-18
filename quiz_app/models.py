from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Question(models.Model):
    """Model representing a question with a title, multiple options, a correct answer, and timestamps."""
    question_title = models.CharField(max_length=200)
    question_options = models.JSONField()
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Frage: {self.question_title} (Antwort: {self.answer})"

class Quiz(models.Model):
    """Model representing a quiz with a title, description, video URL, associated questions, an owner, and timestamps."""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_url = models.URLField(max_length=200)
    questions = models.ManyToManyField(Question)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return f"Quiz: {self.title} ({self.questions.count()} Fragen)"
