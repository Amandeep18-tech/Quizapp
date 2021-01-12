from django.contrib import admin
from .models import MCQ, FillTheBlanks, UserProgress
from users.models import Profile
admin.site.register(MCQ)
admin.site.register(Profile)
admin.site.register(FillTheBlanks)
admin.site.register(UserProgress)
