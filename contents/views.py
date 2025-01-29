from urllib import request
from django import forms
from django.db.models.base import Model as Model
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from .forms import ClickFollowForm ,HospitalSearchForm
from .models import NoticeList ,FollowList,HospitalList
from accounts.models import User
from django.views.generic import ListView,DetailView,TemplateView,FormView,CreateView
from django.db.models import Q
from django.shortcuts import redirect

class Index(TemplateView):
    template_name = 'contents/my_account.html'

class AccessError(TemplateView):
    template_name = '403.html'
    
class ServerError(TemplateView):
    template_name = '404.html'

class NoticeListView(ListView):
    template_name = 'contents/notice_list.html'
    # paginate_by = 10
    context_object_name = "obj_data"
    def get_queryset(self):
        qs = NoticeList.objects.order_by("-posted_at").filter(Q(target=None)|Q(target=self.request.user.id))
        return qs
    

class NoticeDetailView(DetailView):
    template_name = 'contents/notice.html'
    model = NoticeList
    context_object_name = "obj_data"



# class PersonalNoticeListView(ListView):
#     # template_name = "contents/nlist_test.html" 
#     template_name = 'contents/personal_notice_list.html'
#     model = NoticeList
#     paginate_by = 10
    # context_object_name = "obj_data"

# class PersonalNoticeDetailView(DetailView):
#     # template_name = "contents/n_test.html"# template_name = 'contents/notice.html'
#     template_name = 'contents/notice.html'
#     model = NoticeList
#     context_object_name = "obj_data"
    
class FollowView(ListView):
    template_name = "contents/follow_list.html"
    model = FollowList
    paginate_by = 10
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
    template_name = "contents/follower_list.html"
    model = FollowList
    paginate_by = 10
    context_object_name = "erlist"

    def get_queryset(self):
        user = self.request.user
        queryset = FollowList.objects.filter(follow_er=user.id)
        return queryset    
    
class HospitalListView(ListView):
    template_name = "contents/hospital_list.html"
    model = HospitalList
    paginate_by = 10
    context_object_name = "ctx"

    
    def get_queryset(self):
        queryset = HospitalList.objects.filter()
        form = HospitalSearchForm(self.request.GET or None)
        keywords = form.get_keywords().split()

        try:
            print(keywords)
            for i in range(len(keywords)):
                queryset = queryset.filter(Q(detail__icontains = keywords[i]) |Q(name__icontains=keywords[i]) |Q(address__icontains=keywords[i]) |Q(comment__icontains=keywords[i]))

        except:
            pass
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # チャットルーム検索用のフォームを追加
        context['hospital_search_form'] = HospitalSearchForm(self.request.GET or None)

        return context

class HospitalContactView(TemplateView):
    template_name = "contents/hospital_contact.html"

class HospitalDetailView(DetailView):
    template_name = "contents/hospital_detail.html"
    model = HospitalList
    context_object_name = "hospital"
    
class PrivacyPolicyView(TemplateView):
    template_name = "contents/privacy_policy.html"

class TermsView(TemplateView):
    template_name = "contents/terms.html"
    
    
# class E_View(TemplateView):
#     template_name = "403.html"