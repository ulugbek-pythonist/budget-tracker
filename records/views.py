from datetime import date, timedelta
from django.shortcuts import render

from app.models import Expense, Income

# Create your views here.


def weekly(request):
    expenses = Expense.objects.filter(wallet=request.user.wallet).all()
    return render(request,"weekly-expense.html",{"expenses":expenses})

def weekly_income(request):
    incomes = Income.objects.filter(wallet=request.user.wallet).all()
    return render(request,"weekly-income.html",{"incomes":incomes})