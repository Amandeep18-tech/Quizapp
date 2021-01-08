from django.shortcuts import render
from Quizapp.models import Exam, UserResults, FillTheBlanks
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'index.html'
    context_object_name = 'results'
    paginate_by = 1


class ResultPageListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'result.html'
    context_object_name = 'results'


class FillInView(LoginRequiredMixin,ListView):
    model = FillTheBlanks
    template_name = 'fill_in.html'
    context_object_name = 'fill_in'
    paginate_by = 1

