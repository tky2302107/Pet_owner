from django import forms
from django.utils.translation import gettext_lazy
from . import models

User = models.User

# チャットルーム検索用のフォーム
class SearchForm(forms.Form):
    keywords = forms.CharField(
        label=gettext_lazy('keywords (split space)'),
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
            # 'participants': forms.SelectMultiple(attrs={
            #     'class': 'form-control',
            # }),
            # ↓↓↓　サンプルパターン2　↓↓↓　https://arakan-pgm-ai.hatenablog.com/entry/2019/02/18/090000#%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%92%E8%A4%87%E6%95%B0%E9%81%B8%E6%8A%9E%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%83%9C%E3%83%83%E3%82%AF%E3%82%B9%E9%81%B8%E6%8A%9E%E8%82%A2%E3%81%AF%E9%9D%99%E7%9A%84
            'participants': forms.CheckBoxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participants'].queryset = User.objects.filter(is_staff=False)