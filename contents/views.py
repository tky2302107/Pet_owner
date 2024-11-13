from django.shortcuts import render
from .models import NoticeList
from django.views.generic import ListView
from .forms import NoticeListForm
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    # model = models.Index
    template_name = 'contents/my_account.html'

class NoticeList(ListView):
    template_name = "contents/nlist_test.html"# template_name = 'contents/notice_list.html'
    model = NoticeList
    
    
    
        
    # def get_queryset(self, **kwargs):
    #     queryset = super().get_queryset(**kwargs) # Article.objects.all() と同じ結果

    #     # is_publishedがTrueのものに絞り、titleをキーに並び変える
    #     queryset = queryset.filter().order_by('-id')

    #     return queryset
    def get_queryset(self):
        return super().get_queryset()
    
    nl = NoticeList.objects.all().order_by('-id')#models.pyより、通知を全権取得＆日付順に整列
    
    def page_move(request, idid):# ページ遷移用
        id_page = get_object_or_404(NoticeList, pk=idid)
        return render(request, 'contents/n_test.html', {'post': id_page})

    # """
class Notice_(TemplateView):
    template_name = "contents/n_test.html"# template_name = 'contents/notice.html'
    model = NoticeList

    # def get_queryset(self):
    #     idid = self.kwargs['idid']
    #     nl2 = NoticeList.object.filter(id=idid)
        
        
    #     return nl2
    # nl = 
    print("a")
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs) # Article.objects.all() と同じ結果

        # GETリクエストパラメータにkeywordがあれば、それでフィルタする
        keyword = self.request.GET.get('idid')
        if keyword is not None:
            queryset = queryset.filter(title__contains=keyword)

        # is_publishedがTrueのものに絞り、titleをキーに並び変える
        queryset = queryset.filter()
        print("\n")
        print(queryset)
        print("b")
        return queryset
    print("c")

    # queryset = 

    
class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'