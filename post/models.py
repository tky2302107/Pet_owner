from django.db import models
from django.utils import timezone

# 投稿情報モデル
class PostInfo(models.Model): # 投稿IDは自動でつく
    account_id = models.ForeignKey('') # アカウントID　外部キー
    post = models.CharField('post', max_length=300) # 投稿文　文字数300文字
    post_date = models.DateTimeField('post_date', max_length=12, default=timezone.now) # 投稿日時
