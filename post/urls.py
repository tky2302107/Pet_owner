from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('post/', views.PostPageView.as_view(), name='post'),
    path('post_complete/', views.UpdatePostInfo.as_view(), name='update_post'),
]
