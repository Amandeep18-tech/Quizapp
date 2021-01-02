from django.contrib import admin
from .models import Exam
from users.models import Profile
admin.site.register(Exam)
admin.site.register(Profile)