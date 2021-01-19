from django.db import models
from django.contrib.auth.models import User
import uuid


class Question(models.Model):
    """
    Model for storing Questions
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, null=False)
    is_mcq = models.BooleanField(default=False)
    is_fill_in_the_blanks = models.BooleanField(default=False)
    question_text = models.CharField(default="Exam Questions", max_length=100)
    correct_answer = models.CharField(default="Correct Answer", max_length=100)

    def __str__(self):
        return f'{self.question_text}'


class MCQ(models.Model):
    """
    Model for MCQ Questions
    """
    question = models.OneToOneField(
        Question, on_delete=models.PROTECT)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.question}'


class FillInTheBlank(models.Model):
    """
    Model for Fill in the blanks type questions
    """
    question = models.OneToOneField(
        Question, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.question}'


class AnswerGiven(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    answer = models.CharField(default="Your answer", max_length=200)

    def __str__(self):
        return f'{self.answer}'


class UserProgress(models.Model):
    """
    Model for saving User data in each question
    """

    class Meta:
        verbose_name_plural = 'UserProgress'

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    current_page = models.IntegerField(default=1)
    user_score = models.IntegerField(default=0)
    user_answer = models.ManyToManyField(AnswerGiven)
    
    def __str__(self):
        return f'{self.user.username} Progress'
