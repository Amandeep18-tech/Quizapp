from django.db import models
from django.contrib.auth.models import User
import uuid


class Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,null=False)
    is_mcq = models.BooleanField(default=False)
    is_fill_in_the_blanks = models.BooleanField(default=False)
    questions = models.CharField(default="Exam Questions", max_length=100)
    correct_answer = models.CharField(default="Correct Answer", max_length=100)

    def __str__(self):
        return f'{self.questions}'


class MCQ(models.Model):
    questions = models.OneToOneField(
        Questions, on_delete=models.PROTECT)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.questions}'


class FillInTheBlanks(models.Model):
    questions = models.OneToOneField(
        Questions, on_delete=models.PROTECT)
    blank_answer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.questions}'


class UserProgress(models.Model):
    class Meta:
        verbose_name_plural = 'UserProgress'
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    current_page = models.IntegerField(default=1)
    user_answer = models.CharField(default="Your answer", max_length=300)
    user_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Progress'
