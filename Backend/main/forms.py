from django import forms
from django.contrib.auth.models import User


class Rechercher(forms.Form):
    name = forms.CharField(label="Rechercher", max_length=200)
