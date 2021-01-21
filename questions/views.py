from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.shortcuts import HttpResponseRedirect, reverse, render
from .models import UserProgress, MCQ, Question, AnswerGiven, UserCountdownTimer
from .decorators import does_user_has_permission


@method_decorator(does_user_has_permission(message='No access'), name='dispatch')
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
        question_data = self.request.POST.get('user_answer', None)
        user_progress = get_object_or_404(UserProgress,
                                          user=self.request.user)
        answer_given = AnswerGiven.objects.create(
            user=self.request.user, answer=question_data)

        answer_given.save()
        user_progress.user_answer.add(answer_given)

        if question_data is not None:
            questions = Question.objects.all()

            for question in questions:
                if question_data == question.correct_answer:
                    user_progress.user_score += 1
        user_progress.save()
        total_count = Question.objects.all().count()

        if total_count == user_progress.current_page:
            return HttpResponseRedirect(reverse('result-page'))

        else:
            question_page = reverse('question-page')
            return_next_page = f'{question_page}?page={user_progress.current_page+1}'
            return HttpResponseRedirect(return_next_page)

    def get_queryset(self, **kwargs):
        questions = Question.objects.all().order_by('question_text')
        actual_page = self.request.GET.get('page', 1)
        user_progress = get_object_or_404(UserProgress,
                                          user=self.request.user)
        if actual_page == 1:
            user_progress.user_score = 0

        user_progress.current_page = actual_page
        user_progress.save()

        return questions

    # @ cache_control(no_cache=True, must_revalidate=False, no_store=True)
    def get_context_data(self, **kwargs):
        context = super(ExamListView, self).get_context_data(**kwargs)
        # questions=Questions.objects.get()
        doomsday_timer = UserCountdownTimer.objects.create(
            duration_in_minutes=5,
            state=UserCountdownTimer.STATE.RUNNING,
        )
        doomsday_timer = UserCountdownTimer.objects.first()
        remaining_minutes = doomsday_timer.remaining_time_in_minutes()
        print(remaining_minutes)
        context['mcqs'] = MCQ.objects.all()
        context['remaining_minutes'] = doomsday_timer.remaining_time()
        actual_page = self.request.GET.get('page', 1)
        user_progress = get_object_or_404(UserProgress,
                                          user=self.request.user)
        if int(actual_page) < user_progress.current_page:
            return HttpResponseRedirect(reverse('previous-page'))
        return context


class ResultPageListView(LoginRequiredMixin, ListView):
    """
    View to represent user results
    """
    template_name = 'result.html'
    context_object_name = 'questions'

    def get_queryset(self, **kwargs):
        questions = Question.objects.all()
        actual_page = 1
        user_progress = get_object_or_404(UserProgress,
                                          user=self.request.user)
        user_progress.current_page = actual_page

        user_progress.save()
        return questions

    def get_context_data(self, **kwargs):
        context = super(ResultPageListView, self).get_context_data(**kwargs)
        user_progress = get_object_or_404(UserProgress,
                                          user=self.request.user)
        user_score = user_progress.user_score
        total_questions = Question.objects.all().count()
        user_answers = user_progress.user_answers
        context['user_score'] = user_score
        context['total_questions'] = total_questions
        context['user_answers'] = user_answers
        return context
