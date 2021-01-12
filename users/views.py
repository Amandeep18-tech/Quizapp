from django.contrib.auth import views
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.auth import views
from django.shortcuts import reverse
from Quizapp.models import UserProgress


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'register.html'
  success_url = 'login'
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profile.html'


class LoginView(views.LoginView):
	
	def get_success_url(self, *args, **kwargs):
		user_progress = UserProgress.objects.filter(
	    user=self.request.user).first()
		path = reverse('question-page')
		return_path = f'{path}?page={user_progress.current_page}'
		return return_path