from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy

# Create your models here.
# 編集　フォロー　フォロワー　ポイント　投稿履歴
# class Index(UserManager):
#     use_in_migrations = True
#     def get_queryset(self):
        
class NoticeList(models.Model):
    posted_at = models.DateTimeField(
        verbose_name="日時",
        auto_now_add=True
    )
    title = models.CharField(
        verbose_name="タイトル",
        max_length=30,
        default=""
    )
    
    NoticeList = models.TextField(
        verbose_name="本文"
    )
    def __str__(self):
        return self.title
    
# class Notice(models.Model):
#     posted_at = models.DateTimeField(
#         verbose_name="日時",
#         auto_now_add=True
#     )
#     title = models.CharField(
#         verbose_name="タイトル",
#         max_length=30,
#         default=""
#     )
    
#     NoticeList = models.TextField(
#         verbose_name="本文"
#     )
#     def __str__(self):
#         return self.title