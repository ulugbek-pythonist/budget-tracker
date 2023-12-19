from django.urls import path

from . import views


urlpatterns = [
    path("weekly-expense/",views.weekly,name="weekly-expense"), # type: ignore
    path("weekly-income/",views.weekly_income,name="weekly-income"), # type: ignore
]