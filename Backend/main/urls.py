from django.urls import path
from register import views as v

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/<str:name>", views.search, name="search"),
    path("item/<str:item_id>", views.item, name="item"),
    path("administration", views.administration, name="administration"),
    path("profile", views.profile, name="profile"),
    path("profile/settings", views.settings, name="settings"),
    path("panier", views.panier, name="panier"),
    path("librairie/<int:library_id>", views.librairie, name="libraire"),
    path("login/", v.login, name="login"),
    path("inscription/", v.register, name="register"),
]
