from pickle import dumps, loads
import sqlite3
from django.db import connection
from django.template.loader import render_to_string
from django.core.signing import BadSignature,SignatureExpired
from typing import Generic
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse_lazy
<<<<<<< HEAD
from django.views.generic import TemplateView,ListView,FormView,UpdateView,CreateView,DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from config import settings
from .models import fund, User
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  EmailChangeForm, SetUpForm, UserChangeForm
=======
from django.views.generic import TemplateView,ListView,FormView,UpdateView,CreateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.sites.shortcuts import get_current_site
from config import settings
from .models import fund, User ,AdoptList
from post.models import PostInfo
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  EmailChangeForm, SetUpForm, UserChangeForm ,AdoptSearchForm
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from .forms import (
    PasswordChangeForm
)
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
<<<<<<< HEAD
# from django.contrib.auth import get_user_model
# User = get_user_model() 

=======
import datetime
from django.db.models import Q
from django.shortcuts import redirect
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb

class Index(ListView):
    template_name = 'accounts/index.html'
    model = User
    def get_queryset(self):
        return super().get_queryset()

    # def get(self, request, **kwargs):
    #     id = self.request.user.id
    #     if User.objects.get(id=id).pt_give == 1:
    #         pt = {
    #             "points":(3+int(self.request.user.points)),
    #             "pt_give":0
    #             }
    #         User.objects.filter(id=self.request.user.id).update(**pt)
    #         print("point_plus")
    #     else:
    #         print("point_pass")
    
    #     ctx={"id":id}
    #     return self.render_to_response(ctx)    

    model = PostInfo # 投稿情報モデル
    context_object_name = 'ctx' # コンテキスト名
    def get_queryset(self, **kwargs): # モデルから情報を取得
        queryset = super().get_queryset(**kwargs) # 全取得
        
        # keyword = self.request.GET.get('') # 検索ワード取得
        # if keyword is not None:
        queryset = queryset.all() # 部分一致で検索
        print(queryset)
        queryset = queryset.order_by('-post_date')[0:5] # 投稿降順で並び替え&5件まで表示
        
        # login ボーナス
        try:
            id = self.request.user.id
            if User.objects.get(id=id).pt_give == 1:
                pt = {
                    "points":(3+int(self.request.user.points)),
                    "pt_give":0
                    }
                User.objects.filter(id=self.request.user.id).update(**pt)
                print("point_plus")
            else:
                print("point_pass")
        except:
            print("not_login")
            
    
        # 元コンテキスト
        # context = User.objects.filter(id=self.request.user.id).values("icon")
            
        # print(context)
        # queryset = queryset.union(context,all=True)
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {
    #         "icon":str(self.request.user.icon)
    #     }
    #     return context
    
    
    
class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class LogoutChk(TemplateView):
    login_url = '/login/'
    template_name = 'accounts/logout.html'

class LogoutPage(LogoutView):
    login_url = '/login/'
    template_name = 'accounts/logouted.html'
    
class MainPage(TemplateView):
    template_name = 'main.html'
    
class ExchangePoint(UpdateView):
<<<<<<< HEAD
    template_name = 'accounts/p1.html'
=======
    login_url = '/login/'
    # template_name = 'accounts/p1.html'
    template_name = "contents/exchange_point.html"
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    model = User,fund

    def get(self, request, **kwargs):
        if self.request.user.points == 0:
            gobi = "です"
        else:
            gobi = "あります"


        ctx = {
            'points': self.request.user.points,
            "gobi":gobi,
        }
        print("ctx"+str(ctx))
        return self.render_to_response(ctx)
        
    success_url = reverse_lazy("accounts:points_fin")

    
    
class ExchangePointComplete(UpdateView):
<<<<<<< HEAD
    template_name = 'accounts/p2.html'
=======
    # template_name = 'accounts/p2.html'
    login_url = '/login/'
    template_name = "contents/exchange_point_complete.html"
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    model = fund
    def get_queryset(self):
        return super().get_queryset()

    def get(self, request, **kwargs):
        global new_num,ctx_points,box
        box = 0
        # sql直接操作で数値をタプルで取得
        ctx_points = int(self.request.user.points)
        cursor = sqlite3.connect("db.sqlite3").cursor()
        cursor.execute('''SELECT points_sum from accounts_fund where id=1''')
        row = list(cursor.fetchall())
<<<<<<< HEAD
        # 取得したタプルから数値だけ抽出し、intに変換する
=======
        cursor.close()
        # 取得したタプルから数値だけ抽出し、intに変換する
        print("\n!!!!!!!!!!!!!!!!!!!!!\nDB内が一部のデータがNullの場合、\nエラーが発生する場合があります。\nその場合は、DB「accounts_fund」テーブルに \nid=1, points_sum=0 \nを登録してページのリロードを行ってください。\n!!!!!!!!!!!!!!!!!!!!!\n")
        print(row[0])
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
        old_num = int(row[0][0])
        # 合計ポイントに新たなポイントを加算する
        new_num = int(old_num)+int(ctx_points)
        # if box is None:
        box = ctx_points # ctx_pointが上書きされた場合の予備データ
        print("old_num,new_num,ctx_points")
        print(old_num,new_num,ctx_points)
        ctx = {
            'your_points': self.request.user.points,
            'fund_sum': new_num,
        }
        print("ctx2"+str(ctx))
        # db更新
        data = {"points_sum":new_num}
        fund.objects.filter(pk=1).update(**data)
        uid = self.request.user.id
<<<<<<< HEAD
        data2 = {"points":0}
        User.objects.filter(pk=uid).update(**data2)
=======
        points = {"points":0}
        User.objects.filter(pk=uid).update(**points)
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
        return self.render_to_response(ctx)
    

class MyPage(TemplateView):
    model = User
<<<<<<< HEAD
    template_name = "accounts/m_page.html"
=======
    login_url = '/login/'
    # template_name = "accounts/m_page.html"
    template_name = "contents/my_account.html"
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    def get(self, request, **kwargs):
        ctx = {
            'user': self.request.user
        }
        return self.render_to_response(ctx)

class NameChange(LoginRequiredMixin,FormView):
<<<<<<< HEAD
    models = User
    template_name = "accounts/e_page.html"
    form_class = UserChangeForm
    success_url = reverse_lazy('accounts:index')
=======
    login_url = '/login/'
    models = User
    template_name = "accounts/e_page.html"
    form_class = UserChangeForm
    success_url = reverse_lazy('accounts:mypage')
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    
    def form_valid(self, form):
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            # 'email' : self.request.user.email,
            'screen_name' : self.request.user.screen_name,
<<<<<<< HEAD
=======
            'profile' : self.request.user.profile,
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
        })
        return kwargs
    
class PasswordChange(PasswordChangeView):
<<<<<<< HEAD
=======
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    """パスワード変更ビュー"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:pwdone')
    template_name = 'accounts/pw.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'accounts/pwd.html'
<<<<<<< HEAD
=======
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb


class EmailChange(LoginRequiredMixin, FormView):
    """メールアドレスの変更"""
<<<<<<< HEAD
=======
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
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
<<<<<<< HEAD
=======
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
    template_name = 'accounts/email_change_done.html'


class EmailChangeComplete(LoginRequiredMixin, TemplateView):
    """リンクを踏んだ後に呼ばれるメアド変更ビュー"""
<<<<<<< HEAD
=======
    login_url = '/login/'
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
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
    

<<<<<<< HEAD


=======
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
class SetUpView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SetUpForm # 作成した登録用フォームを設定
    template_name = "accounts/test_sig.html" 
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        print(email,password)
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response
<<<<<<< HEAD
    

# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# class OnlyYouMixin(UserPassesTestMixin):
#     raise_exception = True

#     def test_func(self):
#         user = self.request.user
#         return user.screen_name == self.kwargs['screen_name'] or user.is_superuser

# class UserDeleteView(OnlyYouMixin, DeleteView):
    # template_name = "accounts/u_delete.html"
    # success_url = reverse_lazy("accounts:login")
    # model = User
    # slug_field = 'screen_name'
    # slug_url_kwarg = 'screen_name'

class CleanUpView(DeleteView):
   template_name = "accounts/login.html"
   def get(self, request, *args, **kwargs):
       if not request.user.is_authenticated:
           return redirect('accounts:login')
       user = request.user
       user.delete()
       return redirect('accounts:login')


=======

class UserDeletePreView(TemplateView):#ユーザー退会前
    login_url = '/login/'
    template_name = "accounts/deletechk.html"  
      
class UserDeleteView(TemplateView):#ユーザー退会
    login_url = '/login/'
    model = User        
    def get(self, request, **kwargs):
        data = {"is_active":0}
        User.objects.filter(id=self.request.user.id).update(**data)
        return redirect("accounts:login")


# class IconChangeView(UpdateView):
#     template_name=""
#     model = User
#     form_class = IconForm
#     success_url = reverse_lazy('accounts:index')
      
#     def form_valid(self, form):
#         form.instance.account_id = self.request.user
#         return super().form_valid(form)

#     def get(self, request, **kwargs):
#         icon = User.objects.filter(id=self.request.user.id).icon
#         if icon is null:
#             pass
#         else:
#             pass
class AdoptListView(ListView):
    login_url = '/login/'
    template_name = "accounts/adopt_list.html"
    model = AdoptList
    paginate_by = 10
    context_object_name = "ctx"

    # def get_queryset(self):
    #     queryset = AdoptList.objects.filter()
    #     return queryset    

    def get_queryset(self):
        queryset = AdoptList.objects.filter()
        form = AdoptSearchForm(self.request.GET or None)
        keywords = form.get_keywords().split()
        print(list(queryset.values()))
        try:
            print(keywords)
            print(1)
            for i in range(len(keywords)):
                queryset = queryset.filter(Q(detail__icontains = keywords[i]) |Q(title__icontains=keywords[i]) |Q(address__icontains=keywords[i]) |Q(place__icontains=keywords[i])|Q(species__icontains=keywords[i]))
            return queryset
        except:
            print(2)
            return queryset

        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # チャットルーム検索用のフォームを追加
        context['adopt_search_form'] = AdoptSearchForm(self.request.GET or None)

        return context

class AdoptDetailView(DetailView):
    template_name = "accounts/adopt_detail.html"
    model = AdoptList
    context_object_name = "adopt"
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
