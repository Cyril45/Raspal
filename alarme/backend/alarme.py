"""Main base of the alarm."""
from alarme.backend.record import Record
from alarme.backend.detect import Detect
from alarme.backend.flux import Flux
from django.conf import settings
import threading
import time


class Alarme(threading.Thread):
    """Launche the various device and alarm functionality."""

    def __init__(self):
        """Initialize devices and recording object."""
        threading.Thread.__init__(self)
        self.detector = Detect()
        self.detector.start()
        self.flux = Flux()
        self.flux.start()
        self.record = Record(self.flux)
        self.record.start()

    def run(self):
        """Loop that checks the status of the detector and starts recording if necessary."""
        while True:
            time.sleep(0.1)
            if settings.ALARME:
                if self.detector.move:
                    self.record.start_record()
                elif not self.detector.move:
                    self.record.stop_record()
            else:
                self.record.stop_record()
