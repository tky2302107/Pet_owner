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
    id = models.AutoField(primary_key=True)
    posted_at = models.DateTimeField(
        verbose_name="日時",
        auto_now_add=True
    )
    title = models.CharField(
        verbose_name="タイトル",
        max_length=30,
        default=""
    )
    
    text = models.TextField(
        verbose_name="本文"
    )
    # def __str__(self):
    #     return self.title
    
    def __str__(self) -> str:
        return f"{self.title}"
    
class FollowList(models.Model):
    id = models.AutoField(primary_key=True)
    ## フォローした人 ##
    follow = models.IntegerField(
        gettext_lazy("アカウントID"),
        null=False,
    )
    follow_name = models.CharField(
        gettext_lazy("アカウント名"),
        null=False,
        max_length=128,
        default='',
        blank=True,
    )
    ## フォローされた人 ##
    follow_er = models.IntegerField(
        gettext_lazy("アカウントID"),
        null=False,
    )
    follow_er_name = models.CharField(
        gettext_lazy("アカウント名"),
        null=False,
        max_length=128,
        default='',
        blank=True,
    )

class HospitalList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        gettext_lazy("病院名"),
        null=False,
        max_length=30,
        default='',
        blank=False,
    )
    address = models.CharField(
        gettext_lazy("住所"),
        null=False,
        max_length=50,
        default='',
        blank=False,
    )
    detail = models.CharField(
        gettext_lazy("詳細"),
        null=False,
        max_length=128,
        default='',
        blank=False,
    )
    hp = models.URLField(
        gettext_lazy("ホームページ"),
        null=True,
        max_length=300,
        default='',
        blank=True,
    )
    comment = models.CharField(
        gettext_lazy("コメント"),
        null=False,
        max_length=300,
        default='',
        blank=True,
    )
    image = models.ImageField(
        null=True,#後でfalseにする
        upload_to=None, 
        height_field=None, 
        width_field=None, 
        max_length=None
    )