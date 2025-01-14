from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # 投稿
    path('posts/', views.PostPageView.as_view(), name='posts'),
    # 投稿完了
    path('posts/complete', views.PostCompletePageView.as_view(), name='posts_completed'),
    # 投稿検索
    path('posts_search/', views.PostSearchPageView.as_view(), name='posts_search'),
    # 投稿詳細閲覧
    path('posts/<int:pk>/detail', views.PostDetailPageView.as_view(), name='posts_detail'),
    # 投稿削除
    path('posts/<int:pk>/delete', views.PostDeletePageView.as_view(), name='posts_delete'),
    # 投稿削除完了
    path('posts/delete_complete', views.PostDeleteCompletePageView.as_view(), name='posts_delete_completed'),
    # 投稿履歴
    path('mypage/post_history', views.PostHistoryPageView.as_view(), name='posts_history'),
    # 投稿編集
    path('posts/<int:pk>/update', views.PostUpdatePageView.as_view(), name='posts_update'),
]
