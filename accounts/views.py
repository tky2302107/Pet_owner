from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,FormView
from django.contrib.auth.views import LoginView, LogoutView
from .models import fund, User
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserChangeForm
# from django.contrib.auth import get_user_model
# User = get_user_model() 


class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/logout.html'
    
class MainPage(TemplateView):
    template_name = 'main.html'
    
class ExchangePoint(TemplateView):
    template_name = 'accounts/p1.html'
    model = User

    def get(self, request, **kwargs):
        ctx = {
            'points': self.request.user.points,
        }
        print("ctx"+str(ctx))
        return self.render_to_response(ctx)
    
class ExchangePointComplete(TemplateView):
    template_name = 'accounts/p2.html'
    model = fund,User
    def get_queryset(self):
        return super().get_queryset()
    
    # def get_context_data(self, **kwargs):
        # 既存のget_context_dataをコール
    nl = fund.objects.all()
    nlint = fund.objects.filter(id=1)
    print(type(nl))
    print(type(nlint))

    # savedata = fund(id=1,points_sum=nllist+int(ExchangePoint.points))
    # savedata.save()
        
    

class MyPage(TemplateView):
    model = User
    template_name = "accounts/m_page.html"
    def get(self, request, **kwargs):
        ctx = {
            'user': self.request.user
        }
        return self.render_to_response(ctx)

class MyEdit(LoginRequiredMixin,FormView):
    models = User
    template_name = "accounts/e_page.html"
    form_class = UserChangeForm
    success_url = reverse_lazy('accounts:index')
    
    def form_valid(self, form):
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'email' : self.request.user.email,
            'screen_name' : self.request.user.screen_name,
        })
        return kwargs