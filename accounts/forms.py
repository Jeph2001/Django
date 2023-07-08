from django import forms
from .models import SignUp


class SignupForm(forms.ModelForm):


    class Meta:
        model = SignUp
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='User name')
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Password')





