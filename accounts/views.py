from pickle import dumps, loads
from django.template.loader import render_to_string
from django.core.signing import BadSignature,SignatureExpired
from typing import Generic
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from config import settings
from .models import fund, User
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  EmailChangeForm, UserChangeForm
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from .forms import (
    PasswordChangeForm
)
from django.core.mail import send_mail
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

class NameChnge(LoginRequiredMixin,FormView):
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
    
class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:pwdone')
    template_name = 'accounts/pw.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'accounts/pwd.html'


class EmailChange(LoginRequiredMixin, FormView):
    """メールアドレスの変更"""
    template_name = 'accounts/email_change_form.html'
    form_class = EmailChangeForm

    def form_valid(self, form):
        user = self.request.user
        new_email = form.cleaned_data['email']

        # URLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(new_email),
            'user': user,
        }

        subject = render_to_string('accounts/email_template/subject.txt', context)
        message = render_to_string('accounts/email_template/message.txt', context)
        send_mail(subject, message, None, [new_email])

        return redirect('accounts:email_change_done')


class EmailChangeDone(LoginRequiredMixin, TemplateView):
    """メールアドレスの変更メールを送ったよ"""
    template_name = 'accounts/email_change_done.html'


class EmailChangeComplete(LoginRequiredMixin, TemplateView):
    """リンクを踏んだ後に呼ばれるメアド変更ビュー"""
    template_name = 'accounts/email_change_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            new_email = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            User.objects.filter(email=new_email, is_active=False).delete()
            request.user.email = new_email
            request.user.save()
            return super().get(request, **kwargs)