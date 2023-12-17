from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import RegisterForm

from .models import Profile, Wallet


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
    pass

def add_expense(request):
    pass 