from urllib import request
from django import forms
from django.db.models.base import Model as Model
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from .forms import ClickFollowForm
from .models import NoticeList ,FollowList 
from accounts.models import User
from django.views.generic import ListView,DetailView,TemplateView,FormView,CreateView

class Index(TemplateView):
    template_name = 'contents/my_account.html'

class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'

class NoticeListView(ListView):
    # template_name = "contents/nlist_test.html" 
    template_name = 'contents/notice_list.html'
    model = NoticeList
    paginate_by = 10
    context_object_name = "obj_data"

class NoticeDetailView(DetailView):
    # template_name = "contents/n_test.html"# template_name = 'contents/notice.html'
    template_name = 'contents/notice.html'
    model = NoticeList
    context_object_name = "obj_data"
    
class FollowView(ListView):
    template_name = "contents/test_f.html"
    model = FollowList
    paginate_by = 10
    # form_class = FollowDisableForm
    context_object_name = "flist"
    
    def get_queryset(self):
        user = self.request.user
        queryset = FollowList.objects.filter(follow=user.id)#.values_list("follow_name").order_by("follow_name").distinct()
        return queryset
    
    def post(self, request, *args, **kwargs):
        id= request.POST["uid"]
        print("uid"+str(id))
        print("mid"+str(self.request.user.id))
        a = FollowList.objects.filter(
            follow_er=int(id),
            follow=int(self.request.user.id)
            ).delete()
        print("db:"+str(a))
        return redirect(reverse('contents:follow'))


class Follow_erView(ListView):
    template_name = "contents/test_er.html"
    model = FollowList
    paginate_by = 10
    context_object_name = "erlist"

    def get_queryset(self):
        user = self.request.user
        queryset = FollowList.objects.filter(follow_er=user.id)#.values_list("follow_er_name").order_by("follow_er_name").distinct()
        return queryset    
    
class ClickFollowView(TemplateView):
    template_name = "contents/test_cf.html"
    success_url = reverse_lazy("accounts:index")
    model = FollowList,User

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["follow_list"] = FollowList.objects.filter(follow_er=user.id).values("follow_er")
        return context

    def post(self, request, *args, **kwargs):
        id= request.POST["uid"]
        uuser=User.objects.get(id=id)#get(id=id)
        print("u:id"+str(id))
        print("u:name"+str(uuser.screen_name))
        print("m:id"+str(self.request.user.id))
        print("m:name"+str(self.request.user.screen_name))
        fl = FollowList(
            follow_er=int(id),
            follow_er_name=str(uuser.screen_name),
            follow=int(self.request.user.id),
            follow_name=str(self.request.user.screen_name)
            )
        print("db:"+str(fl))
        fl.save()
        return redirect(reverse('contents:test_follow'))
    

class HospitalListView(TemplateView):
    template_name = "contents/hospital_list.html"
    