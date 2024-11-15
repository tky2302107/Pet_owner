from django import forms
from .models import PostInfo
 
# 投稿フォーム
class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.Textarea) # 投稿文
    image = forms.ImageField(required=False) # 画像
    video = forms.FileField(required=False) # 動画

    # メタクラス
    class Meta:
        model = PostInfo # 投稿情報モデル
        fields = ['post', 'image', 'video']