
from django.forms import ModelForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
User = get_user_model() 


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'screen_name'
        )

    def __init__(self, email=None, screen_name=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        if email:
            self.fields['email'].widget.attrs['value'] = email
        if screen_name:
            self.fields['screen_name'].widget.attrs['value'] = screen_name
        

    def update(self, user):
        user.email = self.cleaned_data['email']
        user.screen_name = self.cleaned_data['screen_name']
        user.save()
