from django.urls import path

from .views import test_view

urlpatterns = [
    path("test-view",test_view),
]
