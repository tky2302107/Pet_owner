# from typing import Any
# from django.db.models.query import QuerySet
from django.db.models.base import Model as Model
from django.urls import reverse_lazy
# from django.db.models.query import QuerySet
# from django.urls import reverse_lazy

# from .forms import ClickFollowForm
# from django.shortcuts import render
# from django.urls import reverse
from .models import NoticeList ,FollowList
from django.views.generic import ListView,DetailView,TemplateView,FormView,CreateView
# from .forms import NoticeListForm
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    # model = models.Index
    template_name = 'contents/my_account.html'

class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'

class NoticeListView(ListView):
    template_name = "contents/nlist_test.html"# template_name = 'contents/notice_list.html'
    model = NoticeList
    paginate_by = 10
    context_object_name = "obj_data"

class NoticeDetailView(DetailView):
    template_name = "contents/n_test.html"# template_name = 'contents/notice.html'
    model = NoticeList
    context_object_name = "obj_data"
    
class FollowView(ListView):
    template_name = "contents/test_f.html"
    model = FollowList
    paginate_by = 10
    context_object_name = "flist"
    
    def get_queryset(self):
        #  super().get_queryset(),
        user = self.request.user
        queryset = FollowList.objects.filter(follow=user.id)
        return queryset


class Follow_erView(ListView):
    template_name = "contents/test_er.html"
    model = FollowList
    paginate_by = 10
    context_object_name = "erlist"

    def get_queryset(self):
            #  super().get_queryset(),
            user = self.request.user
            queryset = FollowList.objects.filter(follow_er=user.id)
            return queryset    
    
class ClickFollowView(TemplateView):#CreateView):
    template_name= "accounts/index.html"
    # template_name = "contents/test_cf.html"
    # form_class = ClickFollowForm
    # success_url = reverse_lazy("accounts:index")