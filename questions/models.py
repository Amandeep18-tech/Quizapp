from django.db import models
from django.contrib.auth.models import User


class MCQ(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_ans = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.question}'


class FillTheBlanks(models.Model):
    question = models.TextField(max_length=100)
    blank_answer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.question} '


class UserProgress(models.Model):
    class Meta:
        verbose_name_plural = 'UserProgress'
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    current_page = models.IntegerField(default=1)
    user_answer = models.CharField(null=True, max_length=100)
    score_answer = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Progress'