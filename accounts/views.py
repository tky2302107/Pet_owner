from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/logout.html'
    
class MainPage(TemplateView):
    template_name = 'main.html'