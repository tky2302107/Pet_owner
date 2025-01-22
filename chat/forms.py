from urllib import request
from django import forms
from django.utils.translation import gettext_lazy
from . import models
from contents.models import FollowList
import urllib.request
User = models.User

# チャットルーム検索用のフォーム
class SearchForm(forms.Form):
    keywords = forms.CharField(
        label=gettext_lazy('キーワード'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': gettext_lazy('ルーム名を入力してください'),
            'class': 'form-control',
        }),
    )

    def get_keywords(self):
        init_keywords = ''
        keywords = init_keywords

        if self.is_valid():
            keywords = self.cleaned_data.get('keywords', init_keywords)

        return keywords

# チャットルーム作成/更新用のフォーム
class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ('name', 'description', 'participants')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': gettext_lazy('ルーム名を入力してください'),
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 10,
                'style': 'resize: none',
                'placeholder': gettext_lazy('説明を入力してください'),
                'class': 'form-control',
            }),
            'participants': forms.CheckboxSelectMultiple(attrs={
            }),
            
        }
    def __init__(self, *args, **kwargs):
        if kwargs.get("user_id"):
            self.user_id = kwargs.pop('user_id')    
        else:
            self.user_id = None
        super().__init__(*args, **kwargs)
        fl = list(FollowList.objects.filter(follow_er=self.user_id).values())
        nfl = []
        for i in range(len(fl)):
            nfl.append(int(fl[i]["follow"]))
        self.fields['participants'].queryset = User.objects.filter(is_staff=False,id__in=nfl)
        