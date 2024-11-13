from django import forms
from .models import PostInfo
 
# 投稿フォーム
class UploadForm(forms.ModelForm):
    class Meta:
        model = PostInfo
        fields = ['post', 'image']
        labels = {
            'post': '本文',
            'image': '画像',
        }
        error_message = {
            'post': {
                'required': '何も入力されていません',
            },
        }
    