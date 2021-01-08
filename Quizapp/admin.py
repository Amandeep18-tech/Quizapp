from django.contrib import admin
from .models import Exam,UserResults,FillTheBlanks
from users.models import Profile
admin.site.register(Exam)
admin.site.register(Profile)
admin.site.register(UserResults)
admin.site.register(FillTheBlanks)