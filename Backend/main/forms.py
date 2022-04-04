from django import forms
from django.contrib.auth.models import User

from Backend.main.models import LibraryUserProfile


class Rechercher(forms.Form):
    name = forms.CharField(label="Rechercher", max_length=200)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = LibraryUserProfile
        fields = ('date_birth', 'adresse_postale')
