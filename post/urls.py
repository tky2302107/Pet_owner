from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # 投稿
    path('posts/', views.PostPageView.as_view(), name='posts'),
    # 投稿完了
    path('posts/complete/', views.PostCompletePageView.as_view(), name='posts_completed'),
    # 投稿検索
    path('posts_search/', views.PostSearchPageView.as_view(), name='posts_search'),
]
