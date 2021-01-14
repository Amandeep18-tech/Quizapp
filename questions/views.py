from django.views.generic import ListView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
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
        print("Hello")
        post_data = {
            "user_answer": request.POST.get('user_answer')
        }
        question_data = " "
        question_data = post_data['user_answer']
        user_progress = UserProgress.objects.get(
            user=self.request.user)
        print(question_data)
        # mcq = MCQ.objects.all()
        user_progress.user_answer = question_data
        # if user_progress.user_answer == mcq.correct_ans:
        #     user_progress.user_score += 1
        #     print("hello")
        user_progress.save()

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
        questions = list(chain(mcq, fill_in_the_blanks))
        actual_page = 1
        user_progress = UserProgress.objects.filter(
            user=self.request.user).first()
        user_progress.current_page = actual_page
        user_progress.save()
        return questions





