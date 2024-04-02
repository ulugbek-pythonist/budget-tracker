from django import forms

from .models import Account


class RegisterForm1(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["first_name","last_name","age","gender"]


class RegisterForm2(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["email", "password"]