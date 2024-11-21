# from typing import Any
# from django.db.models.query import QuerySet
# from urllib import request
from urllib import request
from django import forms
from django.db.models.base import Model as Model
from django.urls import reverse_lazy
# from django.db.models.query import QuerySet
# from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import ClickFollowForm
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
    
class ClickFollowView(FormView):#CreateView):
    # template_name= "accounts/index.html"
    template_name = "contents/test_cf.html"
    form_class = ClickFollowForm
    success_url = reverse_lazy("accounts:index")

    # form = ClickFollowForm()
    # if request.method == 'POST': # POSTの時だけ処理する
    #     form = forms.FormSample(request.POST) # POSTで送信した値をform変数に格納
    #     if form.is_valid(): # formの値が正当な時(バリデーションチェックを走らせる)
    #         print(type(form)) # <class 'basicapp.forms.FormSample'>
    #         print(type(form.data['follow_name'])) # 名前に入力した値を取得できる(str)

    # if request.method == "POST":
    #     form = ClickFollowForm(request.POST)
    #     # form_validをオーバーライドする
    #     if form.is_valid():
    #         introduction = f"私の名前は{form.cleaned_data['name']}です。年齢は{form.cleaned_data['age']}歳です。"
    #         context = {'form': form, 'intro': introduction}
    #         return render(request, template_name, context)
    # else:
    #     form = ClickFollowForm()
    #     return render(request, template_name, {"form": form})
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)