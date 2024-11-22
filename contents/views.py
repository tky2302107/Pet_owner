# from typing import Any
# from django.db.models.query import QuerySet
# from urllib import request
from urllib import request
from django import forms
from django.db.models.base import Model as Model
from django.urls import reverse, reverse_lazy
# from django.db.models.query import QuerySet
# from django.urls import reverse_lazy
from django.shortcuts import redirect, render

# from Pet_owner.accounts.models import User
from .forms import ClickFollowForm ,FollowDisableForm
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
    form_class = FollowDisableForm
    context_object_name = "flist"
    
    def get_queryset(self):
        user = self.request.user
        queryset = FollowList.objects.filter(follow=user.id)
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
            #  super().get_queryset(),
            user = self.request.user
            queryset = FollowList.objects.filter(follow_er=user.id)
            return queryset    
    
class ClickFollowView(FormView):#CreateView):
    template_name = "contents/test_cf.html"
    form_class = ClickFollowForm
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'message': "Hello World! from View!!",
    #     }
        # return render(request, 'contents:test_f.html', context)
    
    def post(self, request, *args, **kwargs):
            context = {
                'message': "POST method OK!!",
            }
            print("uid:"+str(request.POST["uid"]))
            
            try:
                return render(request, 'contents:test_f.html', context)
            except:
                 return redirect('contents:test_f.html')
            

# class FollowDisableForm():
#     def followlist_new(request ,self):
#         form = FollowDisableForm(request.POST or None)
#         # user = User()
#         if form.is_valid():
#             # followlist = FollowList()
#             # followlist.title = 

#             return redirect('followlist:followlist_list')
#         return render(request, 'followlist/followlist_new.html', {'form': form})