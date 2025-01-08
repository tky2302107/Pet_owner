from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()

# 投稿情報モデル
class PostInfo(models.Model): # 投稿IDは自動でつく
    account_id = models.ForeignKey(User, on_delete=models.CASCADE) # アカウントID　外部キー
    post = models.CharField('post', max_length=300) # 投稿文　文字数300文字
    post_date = models.DateTimeField('post_date', max_length=12, default=timezone.now) # 投稿日時
    # 画像　保存先は、media/img/post
    image = models.ImageField(upload_to='img/post', verbose_name='画像', null=True, blank=True)
    # 動画　保存先は、media/video/post
    video = models.FileField(upload_to='video/post',  verbose_name='動画', null=True, blank=True)
    
    def __str__(self):
        return self.post
    