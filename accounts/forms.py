from django import forms
from .models import fund

from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model 
from django.forms import ModelForm
<<<<<<< HEAD
=======
from django.utils.translation import gettext_lazy
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
# from django.contrib.auth.models import User
User = get_user_model() 


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = (
<<<<<<< HEAD
            # 'email',
            'screen_name',
        )

    def __init__(self,  screen_name=None, *args, **kwargs):# email=None,
=======
            'icon',
            'screen_name',
            "profile",
        )

    def __init__(self, screen_name=None, profile=None, *args, **kwargs):# email=None,
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        # if email:
        #     self.fields['email'].widget.attrs['value'] = email
        if screen_name:
            self.fields['screen_name'].widget.attrs['value'] = screen_name
<<<<<<< HEAD
        

    def update(self, user):
        # user.email = self.cleaned_data['email']
        user.screen_name = self.cleaned_data['screen_name']
=======
        if profile:
            self.fields['profile'].widget.attrs['value'] = profile

    def update(self, user):
        user.icon = self.cleaned_data['icon']
        user.screen_name = self.cleaned_data['screen_name']
        user.profile = self.cleaned_data['profile']
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
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
    
<<<<<<< HEAD
class PointForm(forms.ModelForm):
    # class Meta:
    #     model = User,fund
    #     fields = '__all__'
    #     # labels = {'point': 'ポイント'}
    #     labels = {"":"","":""}
    pass
=======
# class IconForm(forms.Form):
#     icon = forms.ImageField(required=False )
#     class Meta:
#         model = PostInfo # 投稿情報モデル
#         fields = ['icon']
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb

class SetUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "screen_name",
            "email",#パスワードの項目は自動的に作られるため記述しない
<<<<<<< HEAD
        )
=======
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
>>>>>>> dec7ef4fe50c4a1034a9de3bdfcf3978531943eb
