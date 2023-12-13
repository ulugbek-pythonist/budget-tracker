from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

from .models import Profile, User, Wallet


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
    if request.method == 'GET':
        return render(request,"register.html")
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data["username"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            bio = form.cleaned_data["bio"]
            profil = Profile.objects.create(user=user,first_name=first_name,last_name=last_name,bio=bio)
            profil.save()
            return redirect("home")
        else:
            return render(request,"register.html")