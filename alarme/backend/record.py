"""Main base of the record."""
import threading
from alarme.models import Savinvideo
import datetime as dt
from django.conf import settings
import time
import cv2
import os


class Record(threading.Thread):
    """Launche the recording."""

    def __init__(self, flux):
        """Initialize var and retrieves the flux object."""
        threading.Thread.__init__(self)
        self.flux = flux
        self.recording = False
        self.launched = True

    def run(self):
        """Record launch loop."""
        while self.launched:
            time.sleep(0.1)
            if self.recording:
                filename = dt.datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
                framerates = int(self.flux.video.get(5))
                resolution = (
                    int(self.flux.video.get(3)),
                    int(self.flux.video.get(4))
                    )
                video_type = cv2.VideoWriter_fourcc(*'MPEG')
                out = cv2.VideoWriter(
                    settings.MEDIA_ROOT+'/'+filename+'.avi',
                    video_type,
                    framerates,
                    resolution
                    )
                self.recording = True
                while self.recording:
                    time.sleep(0.01)
                    out.write(self.flux.frame)
                out.release()
                command = "ffmpeg -i {}.avi {}.mp4".format(
                    settings.MEDIA_ROOT+'/'+filename,
                    settings.MEDIA_ROOT+'/'+filename
                    )
                os.system(command)
                os.system("rm {}.avi".format(settings.MEDIA_ROOT+'/'+filename))
                Savinvideo.objects.create(name=filename+'.mp4')

    def start_record(self):
        """Allow you to start the recording."""
        self.recording = True

    def stop_record(self):
        """Allow you to stop the recording."""
        self.recording = False
