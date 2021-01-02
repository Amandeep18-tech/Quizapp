from django.db import models
class Exam(models.Model):
    Question=models.CharField(max_length=100)
    Option1=models.CharField(max_length=100)
    Option2=models.CharField(max_length=100)
    Option3=models.CharField(max_length=100)
    Option4=models.CharField(max_length=100)
    Correct_ans=models.CharField(max_length=100)
class UserResults(models.Model):
    
    results=models.CharField(max_length=100)
    totalquestions=models.CharField(max_length=100)
    