"""Module containing the different forms for account application."""
from django import forms


class Signin(forms.Form):
    """Contain the authentication form."""

    username = forms.CharField(
        label='Nom d\'utilsiateur',
        max_length=25,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )
    password = forms.CharField(
        label='Mot de passe',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
            )
        )


class Modif_account(forms.Form):
    """Contains the account modification form."""

    username = forms.CharField(
        label='Nom d\'utilisateur',
        max_length=25,
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
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )


class Modif_password(forms.Form):
    """Contain password modification form."""

    old_password = forms.CharField(
        label='Ancien mot de passe',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
            )
        )
    new_password = forms.CharField(
        label='Nouveau mot de passe',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
            )
        )
    new_password_compare = forms.CharField(
        label='Confirmation du nouveau mot de passe',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
            )
        )


class Retrieve_password(forms.Form):
    """Contain the password return form."""

    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            )
        )
