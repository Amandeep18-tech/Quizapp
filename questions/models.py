from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime


class Question(models.Model):
    """
    Model for storing Questions
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, null=False)
    is_mcq = models.BooleanField(default=False)
    is_fill_in_the_blanks = models.BooleanField(default=False)
    question_text = models.CharField(default="Exam Questions", max_length=100)
    user = models.ManyToManyField(User, through="AnswerGiven")

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
    choices_mcq = (
        (1, (1)),
        (2, (2)),
        (3, (3)),
        (4, (4)),
    )
    correct_answer_mcq = models.IntegerField(default=0, choices=choices_mcq)

    def __str__(self):
        return f'{self.question}'


class FillInTheBlank(models.Model):
    """
    Model for Fill in the blanks type questions
    """
    question = models.OneToOneField(
        Question, on_delete=models.PROTECT)
    correct_answer_fill_in_the_blanks = models.CharField(
        default="Correct Answer", max_length=100)

    def __str__(self):
        return f'{self.question}'


class AnswerGiven(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT)
    user_answer_fill_in_the_blanks = models.CharField(
        default="Your answer", max_length=200)
    user_answer_mcq = models.IntegerField(default=0)
    is_answer_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question}'


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
    user_time = models.DateTimeField(default=datetime.now(), blank=True)
    user_end_time = models.DateTimeField(default=datetime.now())
    is_finished = models.BooleanField(default=False)
    is_started = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Progress'
