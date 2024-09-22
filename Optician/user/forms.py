from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm, 
    AuthenticationForm, 
    PasswordResetForm,
    SetPasswordForm
)

from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)



class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



