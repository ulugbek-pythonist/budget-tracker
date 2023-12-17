from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('wallet/',views.wallet,name="wallet"),
    path('register/',views.registration,name="register"), # type: ignore
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"), # type: ignore
]
