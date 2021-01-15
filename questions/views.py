from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import HttpResponseRedirect, reverse
from .models import  UserProgress,MCQ,FillInTheBlanks,Questions


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
            questions=Questions.objects.all()
            user_progress.user_answer = question_data
            for question in questions:
                if user_progress.user_answer == question.correct_answer:
                    user_progress.user_score += 1
        user_progress.save()
        total_count=Questions.objects.all().count()
        if total_count == user_progress.current_page:
            return HttpResponseRedirect(reverse('result-page'))
            
        else:
            question_page = reverse('question-page')
            return_next_page = f'{question_page}?page={user_progress.current_page+1}'
            return HttpResponseRedirect(return_next_page)

    def get_queryset(self, **kwargs):
        questions =Questions.objects.all()
        actual_page = self.request.GET.get('page', 1)
        user_progress = UserProgress.objects.filter(
            user=self.request.user).first()
        if actual_page==1:
            user_progress.user_score=0
        user_progress.current_page = actual_page
        user_progress.save()
        return questions

    
    def get_context_data(self, **kwargs):
        context = super(ExamListView, self).get_context_data(**kwargs)
        # questions=Questions.objects.get()
        context['mcqs']=MCQ.objects.all()
        return context
        



class ResultPageListView(LoginRequiredMixin, ListView):
    """
    View to represent user results
    """
    template_name = 'result.html'
    context_object_name = 'questions'

    def get_queryset(self, **kwargs):
        user_progress = UserProgress.objects.filter(
            user=self.request.user).first()
        questions = Questions.objects.all()
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
        total_questions =Questions.objects.all().count()
        context['user_score'] = user_score
        context['total_questions']=total_questions
        return context