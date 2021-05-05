from django.urls import path
from ownerapp import views

urlpatterns = [
    path("ologin/", views.ologin , name = "ologin"),
]


