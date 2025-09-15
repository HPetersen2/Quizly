from django.db import models

class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_options = models.JSONField()
    answer = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Frage: {self.question_title} (Antwort: {self.answer})"

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_url = models.URLField(max_length=200)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"Quiz: {self.title} ({self.questions.count()} Fragen)"
