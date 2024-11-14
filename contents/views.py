from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import NoticeList
from django.views.generic import ListView,DetailView,TemplateView
from .forms import NoticeListForm
from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    # model = models.Index
    template_name = 'contents/my_account.html'

class NoticeList(ListView):
    template_name = "contents/nlist_test.html"# template_name = 'contents/notice_list.html'
    model = NoticeList
    def get_queryset(self):
        return super().get_queryset()
    
    nl = NoticeList.objects.all().order_by('-id')#models.pyより、通知を全権取得＆日付順に整列
    
    def page_move(request, idid):# ページ遷移用
        id_page = get_object_or_404(NoticeList, pk=idid)
        return render(request, 'contents/n_test.html', {'post': id_page})

class NoticeDetail(DetailView):
    template_name = "contents/n_test.html"# template_name = 'contents/notice.html'
    model = NoticeList


class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'