from .models import UserProgress
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib import messages


def does_user_has_permission(message):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user_progress = get_object_or_404(UserProgress,
                                              user=request.user)
            actual_page = request.GET.get('page', 1)
            if user_progress.is_finished is True:
                messages.warning(request, message)
                return HttpResponseRedirect(reverse('result-page'))
            if (int(actual_page) >= user_progress.current_page):

                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, message)
                saved_page = reverse('question-page')
                return_next_page = f'{saved_page}?page={user_progress.current_page}'
                return HttpResponseRedirect(return_next_page)
        return wrap
    return decorator
