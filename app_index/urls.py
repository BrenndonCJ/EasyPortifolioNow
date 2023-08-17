from django.urls import path
from .views import *

urlpatterns = [
    path("", view=IndexView.as_view(), name="index"),
]
