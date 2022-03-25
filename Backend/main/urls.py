from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/<str:name>", views.search, name="search"),
    path("item/<str:id>", views.item, name="item"),
    path("administration", views.administration, name="administration"),
    path("profile", views.profile, name="profile"),
    path("profile/settings", views.settings, name="settings"),
    path("panier", views.panier, name="panier"),
    path("librairie/<int:id>", views.librairie, name="libraire"),
]
