from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # チャットルームの一覧作成
    path('', views.Index.as_view(), name='index'),
    # チャットルームの作成
    path('create/room', views.CreateRoom.as_view(), name='create_room'),
    # チャットルームの更新
    path('update/room/<int:pk>', views.UpdateRoom.as_view(), name='update_room'),
    # チャットルームの削除
    # path('delete/room/<int:pk>', views.DeleteRoom.as_view(), name='delete_room'),
    # チャットルームへの入室
    path('enter/room/<int:pk>', views.EnterRoom.as_view(), name='enter_room'),
    # データベース更新待機ページ
    path("create_redirect/<int:pk>",views.CreateBufferView.as_view(),name="create_buffer"),
    path("delete_redirect/<int:pk>",views.DeleteView.as_view(),name="delete_buffer"),
    path("update_redirect/<int:pk>",views.UpdateBufferView.as_view(),name="update_buffer")

    # チャットルームの作成
    # path('create/room2', views.CreateRoom2.as_view(), name='create_room2'),
    # # チャットルームの更新
    # path('update/room2/<int:pk>', views.UpdateRoom2.as_view(), name='update_room2'),
]