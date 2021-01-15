from django.contrib import admin
from .models import UserProgress, MCQ, FillInTheBlanks, Questions
from users.models import Profile
admin.site.register(MCQ)
admin.site.register(Profile)
admin.site.register(FillInTheBlanks)
admin.site.register(UserProgress)
admin.site.register(Questions)
