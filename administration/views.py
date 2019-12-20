"""Contains function used for views app administration."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import MyUser
from .forms import Creating_user
from alarme.backend.sendmail import Sendmail
from django.conf import settings


@login_required
def index(request):
    """Homepage of the administration website."""
    user = request.user
    all_user = MyUser.objects.all()
    if user.is_superuser:
        return render(
            request,
            'administration/index.html',
            {"list_users": all_user}
            )
    return redirect('/')


@login_required
def remove_user(request, id_user):
    """Remove a user account."""
    user = request.user
    if user.is_superuser:
        user_removed = MyUser.objects.filter(id=id_user)
        user_removed.delete()
        return redirect('/administration/')
    return redirect('/')


@login_required
def creating_user(request):
    """Create a user account."""
    user = request.user
    if user.is_superuser:
        if request.method == 'POST':
            form = Creating_user(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = MyUser.objects.make_random_password(length=8)
                usercreated = MyUser.objects.create_user(
                    username,
                    email,
                    password
                    )
                usercreated.last_name = form.cleaned_data['last_name']
                usercreated.first_name = form.cleaned_data['first_name']
                usercreated.save()

                subject = 'Compte d\'alarme créer'
                message = 'Votre compte d\'alarme à été creer votre nom d\'utilisateur est: {} \nVotre mot de passe est le suivant: {}\nUrl de connexion: http://{}:8000'.format(username, password, settings.ALLOWED_HOSTS[0])
                send = Sendmail()
                send.sendmail(email, subject, message)
                return redirect('/administration/')
        else:
            return render(
                request,
                'administration/creating_user.html',
                {'form': Creating_user()}
                )
    return redirect('/')
