from django import forms
from .models import PostInfo
 
# 投稿フォーム
class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

    