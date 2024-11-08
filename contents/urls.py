from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('/notice', views.Notice.as_view(), name='notice'),
    path('/points', views.Points.as_view(), name='points'),
    
    path('/error404', views.AccessError.as_view(), name='accesserror'),
    path('/error500', views.ServerError.as_view(), name='servererror'),
]