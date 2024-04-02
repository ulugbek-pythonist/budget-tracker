from django.shortcuts import redirect, render

from .models import Account

from .forms import RegisterForm1, RegisterForm2


def registration1(request):
    form = RegisterForm1()
    if request.method == 'POST':
        form = RegisterForm1(request.POST)
        if form.is_valid():
            request.session["reg_form"] = form.cleaned_data
            return redirect("register-2")
    else:
        return render(request,"registration1.html",{"form":form})
    

def registration2(request):
    form = RegisterForm2()
    if request.method == 'POST':
        form = RegisterForm2(request.POST)
        if form.is_valid():
            account = Account.objects.create(
                first_name=request.session["reg_form"]["first_name"],
                last_name=request.session["reg_form"]["last_name"],
                age=request.session["reg_form"]["age"],
                gender=request.session["reg_form"]["gender"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            account.set_password(form.cleaned_data["password"])
            account.save()
            return redirect("home")
    else:
        return render(request,"registration2.html",{"form":form})
