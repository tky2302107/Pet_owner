from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    template_name = 'contents/my_account.html'
