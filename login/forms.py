from django.contrib.auth.models import User
from django import forms


class UserFormLog(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserFormRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
