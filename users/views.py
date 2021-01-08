from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'register.html'
  success_url = 'login'
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profile.html'
