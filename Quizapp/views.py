from django.shortcuts import render, redirect
from Quizapp.models import Exam, FillTheBlanks, UserProgress
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
from django.core.paginator import Paginator


class ExamListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    resuls = []
    context_object_name = 'results'
    paginate_by = 1

    def get_queryset(self, **kwargs):
        mcq = Exam.objects.all()
        fill_in = FillTheBlanks.objects.all()
        results = list(chain(mcq, fill_in))
        actual_page = self.request.GET.get('page', 1)
        current_page = UserProgress.objects.filter(
            user=self.request.user).first()
        current_page.current_page = actual_page
        current_page.save()
        return results


class ResultPageListView(LoginRequiredMixin, ListView):
    template_name = 'result.html'
    context_object_name = 'results'

    def get_queryset(self, **kwargs):
        mcq = Exam.objects.all()
        fill_in = FillTheBlanks.objects.all()
        results = list(chain(mcq, fill_in))
        actual_page = 1
        user_progress = UserProgress.objects.filter(
            user=self.request.user).first()
        user_progress.current_page = actual_page
        user_progress.save()
        return results


class ScoreListView(ListView):
    model=UserProgress
    template_name='index.html'
    context_object_name='score'