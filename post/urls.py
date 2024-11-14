from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('post/', views.PostPageView.as_view(), name='post'),
    path('post_search/', views.PostSearchPageView.as_view(), name='post_search'),
]
