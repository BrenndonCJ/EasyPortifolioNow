from django.urls import path
from .views import *

urlpatterns = [
    path("", view=CreatePageView.as_view(), name="createpage"),
]
