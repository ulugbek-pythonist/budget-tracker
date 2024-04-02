from django.urls import path

from .views import registration1, registration2

urlpatterns = [
    path("register1/",registration1,name="register-1"), # type: ignore
    path("register2/",registration2,name="register-2"), # type: ignore
]
