from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import ExpenseForm, IncomeForm, RegisterForm

from .models import Expense, Income, Profile, Wallet


def home(request):
    return render(request,"home.html")

@login_required
def profile(request):
    inform = Profile.objects.filter(user=request.user).first()
    cont = {"profile":inform}
    return render(request,"profile.html",cont)


@login_required
def wallet(request):
    money = Wallet.objects.filter(owner=request.user).first()
    cont = {"wallet":money}
    return render(request,"wallet.html",cont)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("home")
    else:
        form = RegisterForm()
        return render(request,"register.html",{"form":form})

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data["source"]
            amount = form.cleaned_data["amount"]
            income = Income.objects.create(wallet=request.user.wallet,source=source,amount=amount)
            income.save()
            hamyon = Wallet.objects.filter(owner=request.user).first()
            messages.success(request,message=f"${amount} added to wallet!")
            hamyon.income(amount)
            hamyon.save()
            return redirect("wallet")
        else:
            return redirect("wallet")
    else:
        form = IncomeForm()
        return render(request,"add-income.html",{"form":form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data["destination"]
            amount = form.cleaned_data["amount"]
            expense = Expense.objects.create(wallet=request.user.wallet,destination=source,amount=amount)
            expense.save()
            hamyon = Wallet.objects.filter(owner=request.user).first()
            state = hamyon.expense(amount)
            hamyon.save()
            if not state:
                messages.warning(request,message="Not enough money in wallet")
            return redirect("wallet")
        else:
            return redirect("wallet")
    else:
        form = ExpenseForm()
        return render(request,"add-expense.html",{"form":form})
    pass 