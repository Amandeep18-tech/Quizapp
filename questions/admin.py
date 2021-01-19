from django.contrib import admin
from .models import UserProgress, MCQ, FillInTheBlank, Question,AnswerGiven
from users.models import Profile
admin.site.register(MCQ)
admin.site.register(Profile)
admin.site.register(FillInTheBlank)
admin.site.register(UserProgress)
admin.site.register(Question)
admin.site.register(AnswerGiven)
