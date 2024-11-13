from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('post/', views.PostPageView.as_view(), name='post'),
]
