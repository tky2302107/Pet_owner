from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('notice_list/', views.NoticeList.as_view(), name='notice_list'),
    path('notice/<int:pk>/',views.NoticeDetail.as_view()),#,name='notice'
    
    path('error403/', views.AccessError.as_view(), name='accesserror'),
    path('error404/', views.ServerError.as_view(), name='servererror'),
]