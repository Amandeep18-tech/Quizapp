from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from .models import Profile
from .forms import UserRegisterForm
from questions.models import UserProgress


class SignUpView(SuccessMessageMixin, CreateView):
    """
    View for signup page
    """
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def get_success_url(self):
        return reverse('login')


class ProfileCreateView(LoginRequiredMixin, CreateView):
    """
    View to present the profile page
    """
    model = Profile
    fields = '__all__'
    template_name = 'profile.html'


class CustomLoginView(views.LoginView):
    """
    View for the login page
    """
    template_name = 'login.html'
    
    def get_success_url(self, *args, **kwargs):

        user_progress = get_object_or_404(UserProgress,
                                          user=self.request.user)

        saved_page = reverse('question-page')

        return_saved_page = f'{saved_page}?page={user_progress.current_page}'

        return return_saved_page
