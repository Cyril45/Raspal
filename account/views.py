"""Contains function used for views app account."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.conf import settings
from .forms import Signin, Modif_account, Modif_password, Retrieve_password
from .models import MyUser
from alarme.backend.sendmail import Sendmail


def sign_in(request):
    """Display the sign in form."""
    if request.method == 'POST':
        form = Signin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.first_connexion:
                    return redirect('/account/modif_password')
                else:
                    return redirect('/')

            else:
                error = "identifiant ou mot de passe incorrecte"
                data = {
                    'form': Signin(),
                    'error': error
                }
                return render(request, 'account/signin.html', data)
    else:
        return render(request, 'account/signin.html', {'form': Signin()})


@login_required
def my_account(request):
    """Allow the user to view their account information."""
    user = request.user
    return render(request, 'account/my_account.html', {'account': user})


@login_required
def modif_account(request):
    """Allow the user to change their account information."""
    if request.method == 'POST':
        form = Modif_account(request.POST)
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data['username']
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('/account/')
    else:
        data = {
            'username': request.user.username,
            'last_name': request.user.last_name,
            'first_name': request.user.first_name,
            'email': request.user.email,
        }
        return render(
            request,
            'account/my_account.html',
            {'form': Modif_account(data)}
            )


@login_required
def modif_password(request):
    """Allow the user to change their password."""
    if request.method == 'POST':
        form = Modif_password(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            new_password_compare = form.cleaned_data['new_password_compare']

            if check_password(old_password, user.password) and \
               new_password == new_password_compare:
                user.set_password(new_password)
                if user.first_connexion:
                    user.first_connexion = False
                user.save()
                return redirect('/account/')
            else:
                error = "L'ancien mot de passe où les nouveaux mots de passe ne correspondent pas"
                data = {
                    "error": error,
                    "form": Modif_password()
                    }
                return render(request, 'account/modif_password.html', data)
    else:
        return render(
            request,
            'account/modif_password.html',
            {'form': Modif_password()}
            )


@login_required
def delete_account(request):
    """Allow the user to delete their account."""
    user = request.user
    if user.is_superuser is False:
        user = request.user
        user.delete()
        return redirect('/')


@login_required
def sign_out(request):
    """Allow the user to disconnect."""
    logout(request)
    return redirect('/')


def retrieve_password(request):
    """Allow the user to request a return password."""
    if request.method == 'POST':
        form = Retrieve_password(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_object_or_404(MyUser, email=email)
            random_password = MyUser.objects.make_random_password(length=8)
            user.set_password(random_password)
            user.first_connexion = True
            user.save()

            subject = 'Rappel de vos identifiants d\'alarme'
            message = 'Votre nom d\'utilisateur est: {} \nVotre mot de passe à été réinitialiser avec le mot de passe suivant: {}\nUrl de connexion: http://{}:8000'.format(user, random_password, settings.ALLOWED_HOSTS[0])
            send = Sendmail()
            send.sendmail(email, subject, message)
            return redirect('/')
        else:
            data = {
                'form': Retrieve_password(),
                'error': "Une erreur est survenu merci de réessayer"
                }
            return render(request, 'account/retrieve_password.html', data)
    else:
        return render(
            request,
            'account/retrieve_password.html',
            {'form': Retrieve_password()}
            )
