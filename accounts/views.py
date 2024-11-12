from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User

class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/logout.html'
    
class MainPage(TemplateView):
    template_name = 'main.html'
    
class ExchangePoint(TemplateView):
    template_name = 'accounts/p1.html'
    model = User
    def get_queryset(self):
        return super().get_queryset()
    
    
    
class ExchangePointComplete(TemplateView):
    template_name = 'accounts/p2.html'