# inherit from django forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default == required=True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # password1 is init password, password2 is confirmation


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']