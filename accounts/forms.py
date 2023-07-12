from django import forms
from .models import SignUp, KeepReset


class SignupForm(forms.ModelForm):


    class Meta:
        model = SignUp
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='User name')
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Password')


class ResetForm(forms.Form):
    email_address = forms.CharField(max_length=100, label='Email')
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Password')


class KeepResetForm(forms.ModelForm):


    class Meta:
        model = KeepReset
        fields = "__all__"
#     password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Password')
#     confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Confirm Password')







