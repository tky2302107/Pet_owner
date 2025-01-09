from django import forms
from .models import fund

from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model 
from django.forms import ModelForm
from django.utils.translation import gettext_lazy
# from django.contrib.auth.models import User
User = get_user_model() 


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'icon',
            'screen_name',
            "profile",
        )

    def __init__(self, screen_name=None, profile=None, *args, **kwargs):# email=None,
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        # if email:
        #     self.fields['email'].widget.attrs['value'] = email
        if screen_name:
            self.fields['screen_name'].widget.attrs['value'] = screen_name
        if profile:
            self.fields['profile'].widget.attrs['value'] = profile

    def update(self, user):
        user.icon = self.cleaned_data['icon']
        user.screen_name = self.cleaned_data['screen_name']
        user.profile = self.cleaned_data['profile']
        user.save()

class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class EmailChangeForm(ModelForm):
    """メールアドレス変更フォーム"""

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email
    
# class IconForm(forms.Form):
#     icon = forms.ImageField(required=False )
#     class Meta:
#         model = PostInfo # 投稿情報モデル
#         fields = ['icon']

class SetUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "screen_name",
            "email",#パスワードの項目は自動的に作られるため記述しない
        )

class AdoptSearchForm(forms.Form):
    keywords = forms.CharField(
        label=gettext_lazy('keywords (split space)'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': gettext_lazy('キーワードを入力してください'),
            'class': 'form-control',
        }),
    )

    def get_keywords(self):
        init_keywords = ''
        keywords = init_keywords

        if self.is_valid():
            keywords = self.cleaned_data.get('keywords', init_keywords)

        return keywords
