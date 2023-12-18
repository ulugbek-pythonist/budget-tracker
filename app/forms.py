from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Expense, Income, User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
    

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ["source","amount"]


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["destination","amount"]