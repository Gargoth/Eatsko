from django import forms
from django.contrib.auth.models import User
from userdashboard.models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'preffered_genres']

