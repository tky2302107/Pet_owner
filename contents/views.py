from django.shortcuts import render
from . import models
from django.views.generic import ListView,DetailView

# Create your views here.
from django.views.generic import TemplateView
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    # model = models.Index
    template_name = 'contents/my_account.html'

class NoticeList(TemplateView , ListView):
    template_name = 'contents/notice_list.html'
    # model = models.NoticeList
    # nl = models.NoticeList.objects.get()
    
    
class Points(TemplateView):
    template_name = 'contents/exchange_point.html'
    
class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'