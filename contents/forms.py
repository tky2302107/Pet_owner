from django import forms
from django.forms import ModelForm
from .models import FollowList
from django.contrib.auth import get_user_model
User = get_user_model()

class ClickFollowForm(ModelForm):
    class Meta:
        model=FollowList
        fields = (
            "follow",
            "follow_name",
        )
    # follow_name = forms.CharField()

class FollowDisableForm(forms.Form):
    click = forms.CharField(
        label='forms',
        max_length=100,
        required=True,
    )

# class FollowDisable(forms.Input):
#     class Meta:
#             fie

