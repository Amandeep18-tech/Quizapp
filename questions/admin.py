from django.contrib import admin
from .models import UserProgress, MCQ, FillInTheBlank, Question
from users.models import Profile
admin.site.register(MCQ)
admin.site.register(Profile)
admin.site.register(FillInTheBlank)
admin.site.register(UserProgress)
admin.site.register(Question)
