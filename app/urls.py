from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('profile/wallet/',views.wallet,name="wallet"),
    path('register/',views.registration,name="register"), # type: ignore
    path("profile/logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"), # type: ignore
    path("profile/wallet/add-income/",views.add_income,name="add-income"), # type: ignore
    path("profile/wallet/add-expense/",views.add_expense,name="add-expense"), # type: ignore
]
