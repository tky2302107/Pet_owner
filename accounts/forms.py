from django import forms
from .models import fund

from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model
from django.forms import ModelForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
User = get_user_model() 


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = (
            # 'email',
            'screen_name',
        )

    def __init__(self,  screen_name=None, *args, **kwargs):# email=None,
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        # if email:
        #     self.fields['email'].widget.attrs['value'] = email
        if screen_name:
            self.fields['screen_name'].widget.attrs['value'] = screen_name
        

    def update(self, user):
        # user.email = self.cleaned_data['email']
        user.screen_name = self.cleaned_data['screen_name']
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
    
class PointForm(forms.ModelForm):
    # class Meta:
    #     model = User,fund
    #     fields = '__all__'
    #     # labels = {'point': 'ポイント'}
    #     labels = {"":"","":""}
    pass

class SetUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "screen_name",
            "email",
            # "password",
        )