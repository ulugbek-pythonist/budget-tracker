from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    bio = forms.CharField(max_length=1000)
    username = forms.CharField(max_length=150)
    password = forms.PasswordInput()

    