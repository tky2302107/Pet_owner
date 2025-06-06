from django import forms
from django.forms import ModelForm
from .models import FollowList
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy
User = get_user_model()

class ClickFollowForm(ModelForm):
    class Meta:
        model=FollowList
        fields = (
            "follow",
            "follow_name",
        )
    # follow_name = forms.CharField()

class HospitalSearchForm(forms.Form):
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