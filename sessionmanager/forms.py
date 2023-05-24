from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    CHOICES = [('User','User'),('Business Owner','Business Owner')]
    account_type=forms.CharField(label='Account Type', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'account_type']
