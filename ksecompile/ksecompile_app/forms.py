from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=14, widget=forms.TextInput(attrs={'class': 'authorization__form-input'}))
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=14, widget=forms.TextInput(attrs={'class': 'authorization__form-input'}))
    password1 = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))
    password2 = forms.CharField(label='Confirm password', max_length=128, widget=forms.PasswordInput(attrs={'class': 'authorization__form-input'}))
    email = forms.EmailField(label='Email', max_length=320, widget=forms.EmailInput(attrs={'class': 'authorization__form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')