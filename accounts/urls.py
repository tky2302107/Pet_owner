from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.LogoutPage.as_view(), name='logout'),
    path('point/', views.ExchangePoint.as_view(), name='points'),
    path('point_fin/<int:points>', views.ExchangePointComplete.as_view(), name='points_fin'),
    
    # メインメニュー仮リンク
    path('menu/', views.MainPage.as_view(), name='menu'),
    path('mypage/', views.MyPage.as_view(), name='mypage'),
    path('mypage/edit/', views.MyEdit.as_view(), name='myedit'),

]