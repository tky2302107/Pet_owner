from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('notice_list/', views.NoticeListView.as_view(), name='notice_l'),
    path('notice/<int:pk>/', views.NoticeDetailView.as_view(), name='notice_d'),
    
    path('error403/', views.AccessError.as_view(), name='accesserror'),
    path('error404/', views.ServerError.as_view(), name='servererror'),
]