from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, reverse, render
from .models import MCQ, FillTheBlanks, UserProgress


class ExamListView(LoginRequiredMixin, ListView):
    """

    view to represent all the questions in the database
    """
    template_name = 'index.html'
    context_object_name = 'questions'
    paginate_by = 1

    def post(self, request, *args, **kwargs):
        """
        Post the user answer
        """
        post_data = {
            "user_answer": request.POST.get('user_answer')
        }
        
        question_data = " "
        question_data = self.request.POST.get('user_answer',None)
        user_progress = UserProgress.objects.get(
            user=self.request.user)
        if question_data is not None:
            mcq = MCQ.objects.all()
            fill_in_the_blanks = FillTheBlanks.objects.all()
            user_progress.user_answer = question_data
            for fill_in_the_blank in fill_in_the_blanks:
                if user_progress.user_answer == fill_in_the_blank.blank_answer:
                    user_progress.user_score += 1
            for mcq in mcq:
                if user_progress.user_answer == mcq.correct_ans:
                    user_progress.user_score += 1
        user_progress.save()
        mcq_count = MCQ.objects.all().count()
        fill_in_the_blanks_count = FillTheBlanks.objects.all().count()
        total_count = mcq_count+fill_in_the_blanks_count
        if total_count == user_progress.current_page:
            return HttpResponseRedirect(reverse('result-page'))
            
        else:
            question_page = reverse('question-page')
            return_next_page = f'{question_page}?page={user_progress.current_page+1}'
            return HttpResponseRedirect(return_next_page)

    def get_queryset(self, **kwargs):
        mcq = MCQ.objects.all()
        fill_in_the_blanks = FillTheBlanks.objects.all()
        questions = list(chain(mcq, fill_in_the_blanks))
        actual_page = self.request.GET.get('page', 1)
        user_progress = UserProgress.objects.filter(
            user=self.request.user).first()
        user_progress.current_page = actual_page
        user_progress.save()
        return questions


class ResultPageListView(LoginRequiredMixin, ListView):
    """
    View to represent user results
    """
    template_name = 'result.html'
    context_object_name = 'questions'

    def get_queryset(self, **kwargs):
        mcq = MCQ.objects.all()
        fill_in_the_blanks = FillTheBlanks.objects.all()
        user_progress = UserProgress.objects.filter(
            user=self.request.user).first()
        questions = list(chain(mcq, fill_in_the_blanks))
        actual_page = 1
        user_progress = UserProgress.objects.filter(
            user=self.request.user).first()
        user_progress.current_page = actual_page
        user_progress.save()
        return questions
   
    
    def get_context_data(self, **kwargs):
        context = super(ResultPageListView, self).get_context_data(**kwargs)
        user_progress= UserProgress.objects.get(
            user=self.request.user)
        user_score=user_progress.user_score
        mcq_count = MCQ.objects.all().count()
        fill_in_the_blanks_count = FillTheBlanks.objects.all().count()
        total_questions = mcq_count+fill_in_the_blanks_count
        context['user_score'] = user_score
        context['total_questions']=total_questions
        return context