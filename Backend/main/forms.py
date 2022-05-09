from django import forms


class Rechercher(forms.Form):
    name = forms.CharField(label="Rechercher", max_length=200)
