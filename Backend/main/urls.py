from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("bookList", views.bookList, name="bookList"),
    path("bookPage", views.bookPage, name="bookPage"),
    path("administration", views.administration, name="administration"),
]
