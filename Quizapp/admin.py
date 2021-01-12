from django.contrib import admin
from .models import Exam,FillTheBlanks,UserProgress
from users.models import Profile
admin.site.register(Exam)
admin.site.register(Profile)
admin.site.register(FillTheBlanks)
admin.site.register(UserProgress)
