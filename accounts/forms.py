from django import forms
from .models import fund

from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model 
from django.forms import ModelForm
from django.utils.translation import gettext_lazy
User = get_user_model() 


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'icon',
            'screen_name',
            "profile",
        ]
        widgets = {
            'screen_name': forms.TextInput(attrs={
                'placeholder': gettext_lazy('アカウント名を入力してください'),
                'class': 'form-control',
            }),
            'profile': forms.Textarea(attrs={
                'placeholder': gettext_lazy('プロフィールを入力してください'),
                'class': 'form-control',
            }),
            
        }

    def __init__(self, icon=None, screen_name=None, profile=None, *args, **kwargs):# email=None,
        kwargs.setdefault('label_suffix', '')
        id = kwargs.pop("id")
        super().__init__(*args, **kwargs)
        print("icon:"+str(icon))
        
        print("id:"+str(id))
        
        if screen_name:
            self.fields['screen_name'].widget.attrs['value'] = screen_name
        if profile:
            self.fields['profile'].initial = profile
    def update(self, user):
        
        if self.cleaned_data['icon'] == "icon/default.png":
            print("pass")
            pass
        else:
            user.icon = self.cleaned_data['icon']
            print("b"+str(user.icon))
            
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
        widgets = {
            'screen_name': forms.TextInput(attrs={
                'placeholder': gettext_lazy('アカウント名を入力してください'),
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': gettext_lazy('メールアドレスを入力してください'),
                'class': 'form-control',
            }),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs.update({'placeholder':'パスワードを入力してください'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'パスワードを再度入力してください'})

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
"""
class FollowForm(forms.Form):
""" 