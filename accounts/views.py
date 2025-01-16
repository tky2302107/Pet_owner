from pickle import dumps, loads
import sqlite3
from django.db import connection
from django.template.loader import render_to_string
from django.core.signing import BadSignature,SignatureExpired
from typing import Generic
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,ListView,FormView,UpdateView,CreateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.sites.shortcuts import get_current_site
from config import settings
from .models import fund, User ,AdoptList
from post.models import PostInfo
from contents.models import FollowList
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import  EmailChangeForm, SetUpForm, UserChangeForm ,AdoptSearchForm
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from .forms import (
    PasswordChangeForm
)
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
import datetime
from django.db.models import Q
from django.shortcuts import redirect

class Index(ListView):
    template_name = 'accounts/index.html'
    model = User
    def get_queryset(self,**kwargs):
        
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

    def get_context_data(self):
        context = super().get_context_data()
        context["myid"] = self.request.user.id
        print(context)
        return context
    
    
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
    login_url = '/login/'
    # template_name = 'accounts/p1.html'
    template_name = "contents/exchange_point.html"
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
    # template_name = 'accounts/p2.html'
    login_url = '/login/'
    template_name = "contents/exchange_point_complete.html"
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
        cursor.close()
        # 取得したタプルから数値だけ抽出し、intに変換する
        print("\n!!!!!!!!!!!!!!!!!!!!!\nDB内が一部のデータがNullの場合、\nエラーが発生する場合があります。\nその場合は、DB「accounts_fund」テーブルに \nid=1, points_sum=0 \nを登録してページのリロードを行ってください。\n!!!!!!!!!!!!!!!!!!!!!\n")
        print(row[0])
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
        points = {"points":0}
        User.objects.filter(pk=uid).update(**points)
        return self.render_to_response(ctx)
    

class MyPage(TemplateView):
    model = User
    login_url = '/login/'
    # template_name = "accounts/m_page.html"
    template_name = "contents/my_account.html"
    def get(self, request, **kwargs):
        ctx = {
            'user': self.request.user
        }
        return self.render_to_response(ctx)

class NameChange(LoginRequiredMixin,FormView):
    login_url = '/login/'
    models = User
    template_name = "accounts/user_edit.html"
    form_class = UserChangeForm
    success_url = reverse_lazy('accounts:mypage')
    
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
            'profile' : self.request.user.profile,
        })
        return kwargs
    
class PasswordChange(PasswordChangeView):
    login_url = '/login/'
    """パスワード変更ビュー"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:pwdone')
    template_name = 'accounts/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'accounts/password_change_done.html'
    login_url = '/login/'


class EmailChange(LoginRequiredMixin, FormView):
    """メールアドレスの変更"""
    login_url = '/login/'
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
    login_url = '/login/'
    template_name = 'accounts/email_change_done.html'


class EmailChangeComplete(LoginRequiredMixin, TemplateView):
    """リンクを踏んだ後に呼ばれるメアド変更ビュー"""
    login_url = '/login/'
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
    

class SetUpView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SetUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html" 
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

class UserDeletePreView(TemplateView):#ユーザー退会前
    login_url = '/login/'
    template_name = "accounts/user_delete.html"  
      
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

class AdoptAboutView(TemplateView):
    template_name = "accounts/adopt_about.html"


class UserDetailView(DetailView):
    template_name = "accounts/user_detail.html"
    model = User,FollowList
    context_object_name = "user"
    # fl = list(FollowList.objects.filter(id=2))[0]
    def get(self,request, **kwargs):
        try:
            fl = list(FollowList.objects.filter(follow_er=int(self.kwargs["pk"]),follow=self.request.user.id).values())[0]
        except:
            fl = None
        u = list(User.objects.filter(id=int(self.kwargs["pk"])).values())[0]
        self.kwargs["id"] = u["id"]
        self.kwargs["name"] = u["screen_name"]
        self.kwargs["profile"] = u["profile"]
        self.kwargs["email"] = u["email"]
        self.kwargs["myid"] = self.request.user.id
        if fl is None:# 0は未フォロー1はフォロー済
            self.kwargs["follow_tf"] = 0
        else:
            self.kwargs["follow_tf"] = 1
        return render(request,'accounts/user_detail.html',self.kwargs)

    def post(self, request, *args, **kwargs):
        uid= request.POST["uid"]
        uuser=User.objects.get(id=uid)
        u = list(User.objects.filter(id=int(self.kwargs["pk"])).values())[0]
        self.kwargs["id"] = u["id"]
        self.kwargs["name"] = u["screen_name"]
        self.kwargs["profile"] = u["profile"]
        self.kwargs["email"] = u["email"]
        self.kwargs["myid"] = self.request.user.id
        fl = FollowList(
            follow_er=int(uid),
            follow_er_name=str(uuser.screen_name),
            follow=int(self.request.user.id),
            follow_name=str(self.request.user.screen_name)
            )
        fl.save()
        return render(request,'accounts/user_detail.html',self.kwargs)

    def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            context["myid"] = self.request.user.id
            print(context)
            return context



    # print(fl)
    # def get_context_data(self, **kwargs):
        
    #     # int(self.kwargs["pk"])

    #     context = super().get_context_data(**kwargs)
    #     # context["user"] = 
        
    #     return object
    
        
        
        
    # def get_object(self,**kwargs):
    #     object = User.objects.get(id=self.kwargs["pk"])
    #     # object_a = FollowList.objects.filter(follow=self.kwargs["pk"],follow_er=self.request.user.id)
    #     # print("\"\"\""+str(object_a[0][0]))
    #     # object.FollowList_set.
    #     id=self.kwargs["pk"]
    #     print(id)
    #     print("type:"+str(type(object)))
    #     print(str(object))
    #     return object
