from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    template_name = 'contents/my_account.html'

class Notice(TemplateView):
    template_name = 'contents/notice_list.html'
    
class Points(TemplateView):
    template_name = 'contents/exchange_point.html'
    
class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'