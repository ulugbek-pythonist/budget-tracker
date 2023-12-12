from django.shortcuts import render

from .models import Profile


def home(request):
    return render(request,"home.html")


def profile(request):
    inform = Profile.objects.filter(user=request.user).first()
    cont = {"profile":inform}
    return render(request,"profile.html",cont)