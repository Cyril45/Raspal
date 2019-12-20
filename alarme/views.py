"""Contains function used for views app alarme."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import FileResponse, StreamingHttpResponse
from .models import Savinvideo
from alarme.backend.alarme import Alarme
import os


modalarme = Alarme()
modalarme.start()


@login_required
def views_live(request):
    """Allow viewers to watch the live stream."""
    return StreamingHttpResponse(
        modalarme.flux.get_frame(),
        content_type="multipart/x-mixed-replace;boundary=frame"
        )


@login_required
def index(request):
    """Homepage of the website."""
    user = request.user
    data = {
        "alarme": settings.ALARME,
        'account': user
        }
    return render(request, 'alarme/index.html', data)


@login_required
def alarme(request, receiv):
    """Enable or disable alarm."""
    if receiv == "activate":
        settings.ALARME = True
        return redirect("/")
    elif receiv == "desactivate":
        settings.ALARME = False
        return redirect("/")


@login_required
def enregistrement(request):
    """Page that displays the record list."""
    return render(
        request,
        'alarme/enregistrement.html',
        {"video": Savinvideo.objects.all()}
        )


@login_required
def download(request, namefile):
    """Url that allows you to download the videos."""
    response = FileResponse(
        open(settings.MEDIA_ROOT+'/'+namefile, 'rb'),
        as_attachment=True
        )
    return response


@login_required
def view_vid(request, namefile):
    """Allow you to view the recorded videos."""
    response = FileResponse(open(settings.MEDIA_ROOT+'/'+namefile, 'rb'))
    return response


@login_required
def delete_vid(request, namefile):
    """Allow you to delete a video."""
    if request.user.is_superuser:
        ma_video = Savinvideo.objects.filter(name=namefile)
        ma_video.delete()
        os.system(
            "rm {}".format(os.path.abspath(settings.MEDIA_ROOT+'/'+namefile))
            )
        return redirect("/enregistrement")
    else:
        return redirect("/enregistrement")
