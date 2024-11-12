from django.shortcuts import render
from .models import NoticeList#,Notice
from django.views.generic import ListView,DetailView
from .forms import NoticeListForm
# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    # model = models.Index
    template_name = 'contents/my_account.html'

class NoticeList(ListView):
    template_name = "contents/nlist_test.html"# template_name = 'contents/notice_list.html'
    model = NoticeList
    
    
    nl = NoticeList.objects.all().order_by('-posted_at')#models.pyより、通知を全権取得＆日付順に整列
        
    
    def page_move(request, idid):
        id_page = get_object_or_404(NoticeList, pk=idid)
        return render(request, 'contents/n_test.html', {'post': id_page})

    # """
class Notice(ListView):
    template_name = "contents/n_test.html"# template_name = 'contents/notice.html'
    model = NoticeList

    def get_id(self):
        global idid
        idid = self.kwargs['idid']       
        return idid
    
    nl2 = NoticeList.objects.filter(id=idid)
    
class Points(TemplateView):
    template_name = 'contents/exchange_point.html'
    
class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'