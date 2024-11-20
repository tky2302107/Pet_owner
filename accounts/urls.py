from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutPage.as_view(), name='logout'),
    path('setup/', views.SetUpView.as_view(), name='setup'),
    path('mypage/point/', views.ExchangePoint.as_view(), name='points'),
    path('mypage/point/done/', views.ExchangePointComplete.as_view(), name='points_fin'),
    
    # メインメニュー仮リンク
    path('menu/', views.MainPage.as_view(), name='menu'),
    path('mypage/', views.MyPage.as_view(), name='mypage'),
    path('mypage/edit/', views.NameChnge.as_view(), name='namechange'),
    path("mypage/pwchange/",views.PasswordChange.as_view(),name="pwchange"),
    path("mypage/pwchange/done/",views.PasswordChangeDone.as_view(),name="pwdone"),
    path('mypage/emchange/', views.EmailChange.as_view(), name='email_change'),
    path('mypage/emchange/done/', views.EmailChangeDone.as_view(), name='email_change_done'),
    path('mypage/emchange/complete/<str:token>/', views.EmailChangeComplete.as_view(), name='email_change_complete'),
    path('mypage/follow/',views.Follow.as_view(), name='follow'),
    path('mypage/follower/',views.Follow_er.as_view(), name='follow_er'),
]