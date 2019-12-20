"""Module containing the different forms for account application."""
from django import forms


class Creating_user(forms.Form):
    """Contain the user creation form."""

    username = forms.CharField(
        label='Nom d\'utilisateur',
        max_length=25,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )
    last_name = forms.CharField(
        label='Nom',
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )
    first_name = forms.CharField(
        label='Prénom',
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )
