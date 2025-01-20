from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutChk.as_view(), name='logoutchk'),
    path('logout/done/', views.LogoutPage.as_view(), name='logout'),
    path('setup/', views.SetUpView.as_view(), name='setup'),
    path('exit/', views.UserDeletePreView.as_view(), name='cleanup'),
    path('deleted/', views.UserDeleteView.as_view(), name='delete'),
    path('mypage/point/', views.ExchangePoint.as_view(), name='points'),
    path('mypage/point/done/', views.ExchangePointComplete.as_view(), name='points_fin'),
    
    # メインメニュー仮リンク
    path('menu/', views.MainPage.as_view(), name='menu'),#旧ホーム
    path('mypage/', views.MyPage.as_view(), name='mypage'),
    path('mypage/edit/', views.NameChange.as_view(), name='edit_profile'),
    path("mypage/pwchange/",views.PasswordChange.as_view(),name="pwchange"),
    path("mypage/pwchange/done/",views.PasswordChangeDone.as_view(),name="pwdone"),
    path('mypage/emchange/', views.EmailChange.as_view(), name='email_change'),
    path('mypage/emchange/done/', views.EmailChangeDone.as_view(), name='email_change_done'),
    path('mypage/emchange/complete/<str:token>/', views.EmailChangeComplete.as_view(), name='email_change_complete'),
    path('adopt/', views.AdoptListView.as_view(), name='adopt'),
    path('adopt/<int:pk>/', views.AdoptDetailView.as_view(), name='adopt_detail'),
    path('adopt/about/', views.AdoptAboutView.as_view(), name='adopt_about'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    
]