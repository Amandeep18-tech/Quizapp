from .models import UserProgress
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib import messages
from datetime import datetime


def does_user_has_permission():
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user_progress = get_object_or_404(UserProgress,
                                              user=request.user)
            actual_page = request.GET.get('page', 1)

            if user_progress.user_end_time < \
                    datetime.now(user_progress.user_end_time.tzinfo):
                message = 'No access to the quiz app as Time Over. One attempt per user!'
                messages.warning(request, message)
                return HttpResponseRedirect(reverse('result-page'))

            if user_progress.is_finished is True:
                message = 'No acccess to the questions anymore. You have already attempted all questions'
                messages.warning(request, message)
                return HttpResponseRedirect(reverse('result-page'))

            if (int(actual_page) >= user_progress.current_page):
                return view_func(request, *args, **kwargs)

            if (int(actual_page) < user_progress.current_page):
                message = 'No access to the previous page'
                messages.warning(request, message)
                saved_page = reverse('question-page')
                return_next_page = f'{saved_page}?page={user_progress.current_page}'
                return HttpResponseRedirect(return_next_page)
        return wrap
    return decorator


def does_user_has_permission_for_result_page():
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user_progress = get_object_or_404(UserProgress,
                                              user=request.user)
            actual_page = request.GET.get('page', 1)
            if user_progress.user_end_time < \
                    datetime.now(user_progress.user_end_time.tzinfo):
                user_progress.current_page = 1
                user_progress.is_finished = True

            if user_progress.is_finished is False:
                message = 'No access to the result page! Please finish quiz first'
                messages.warning(request, message)
                saved_page = reverse('question-page')
                return_next_page = f'{saved_page}?page={user_progress.current_page}'
                return HttpResponseRedirect(return_next_page)
            else:
                return view_func(request, *args, **kwargs)
        return wrap
    return decorator
#End1111
