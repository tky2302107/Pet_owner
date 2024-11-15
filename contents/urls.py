from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path(r'notice_list/', views.NoticeList.as_view(), name='notice_list'),
    path(r'notice/<int:pk>/', views.NoticeDetailView.as_view(), name='notice_d'),
    
    path(r'error403/', views.AccessError.as_view(), name='accesserror'),
    path(r'error404/', views.ServerError.as_view(), name='servererror'),
]