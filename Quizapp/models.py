from django.db import models


class Exam(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_ans = models.CharField(max_length=100)


class UserResults(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    results = models.CharField(max_length=100)

class FillTheBlanks(models.Model):
    question=models.TextField(max_length=100)
    user_answer=models.TextField(max_length=100,null=True)
    blank_answer=models.CharField(max_length=100)
    
