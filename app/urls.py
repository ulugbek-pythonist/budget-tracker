from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('wallet/',views.wallet,name="wallet"),
    path('register/',views.registration,name="register"),
]
