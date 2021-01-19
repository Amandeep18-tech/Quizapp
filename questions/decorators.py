from django.contrib.auth.decorators import user_passes_test
from .models import UserProgress
from django.shortcuts import get_object_or_404
from users.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages


def does_user_has_permission(message):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user_progress = get_object_or_404(UserProgress,
                                              user=request.user)
            actual_page = request.GET.get('page', 1)

            if int(actual_page) >= user_progress.current_page:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, message)
                saved_page = reverse('question-page')
                return_next_page = f'{saved_page}?page={user_progress.current_page}'
                return HttpResponseRedirect(return_next_page)
        return wrap
    return decorator


# def does_user_has_permission(self, request, actual_page, message):
#     user_progress = get_object_or_404(UserProgress,
#                                       user=request.user)
#     if actual_page < user_progress.current_page:
#         return True
#     else:
#         return False

#     is_valid_page = user_passes_test(lambda u: True if u.is_valid_page else False,
#                                      redirect_field_name=redirect_field_name,
#                                      message=message
#                                      )
#     if view_func:
#         return actual_decorator(view_func)
#     return actual_decorator
