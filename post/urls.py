from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('posts/', views.PostPageView.as_view(), name='posts'),
    path('posts/complete/', views.PostCompletePageView.as_view(), name='posts_completed'),
    path('posts_search/', views.PostSearchPageView.as_view(), name='posts_search'),
]
