from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('notice_list/', views.NoticeListView.as_view(), name='notice_l'),
    path('notice/<int:pk>/', views.NoticeDetailView.as_view(), name='notice_d'),

    path('mypage/follow/',views.FollowView.as_view(), name='follow'),
    path('mypage/follower/',views.Follow_erView.as_view(), name='follow_er'),
    path("hospital_list/",views.HospitalListView.as_view(), name='hospital_list'),
    path("hospital_contact/",views.HospitalContactView.as_view(), name='hospital_contact'),
    path("hospital_detail/<int:pk>/",views.HospitalDetailView.as_view(), name='hospital_detail'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('privacy_policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
    # path("403",views.E_View.as_view(),name="403"),
]