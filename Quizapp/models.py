from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_ans = models.CharField(max_length=100)


class FillTheBlanks(models.Model):
    question=models.TextField(max_length=100)
    blank_answer=models.CharField(max_length=100)
    

class UserProgress(models.Model):
    class Meta:
        verbose_name_plural='UserProgress'    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions=models.ManyToManyField(Exam)
    current_page=models.IntegerField(default=1)
    user_answer=models.CharField(null=True,max_length=100)
    score_answer=models.IntegerField(default=0)