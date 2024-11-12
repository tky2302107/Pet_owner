from django.shortcuts import render
from .models import NoticeList
from django.views.generic import ListView,DetailView

# Create your views here.
from django.views.generic import TemplateView
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    # model = models.Index
    template_name = 'contents/my_account.html'

class NoticeList(ListView):
    # template_name = 'contents/notice_list.html'
    template_name = "contents/list_test.html"
    model = NoticeList
    nl = NoticeList.objects.all().order_by('-posted_at')#models.pyより、通知を全権取得＆日付順に整列
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        print(context)
        return context
    
    
    
class Points(TemplateView):
    template_name = 'contents/exchange_point.html'
    
class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'