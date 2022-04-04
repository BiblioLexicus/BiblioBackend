from django import forms

name = 'Prénom'
lastName = 'Nom'
address = 'address'
# maybe not necessary, ajouté le tout dans views normal
"""
class InscriptionForm(forms.Form):
    firstName = forms.CharField(name, max_length= 150)
    lastName = forms.CharField(lastName, max_length=150)
    birthDate = forms.DateInput()
    email = forms.EmailField()
    password = forms.PasswordInput()
    address = forms.CharField(address, max_length=)
"""