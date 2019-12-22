"""Main base of the detector."""
from threading import Thread
import time
from account.models import MyUser
from .sendmail import Sendmail
from django.conf import settings

if settings.TRAVIS == True:
    import sys
    import fake_rpi
    sys.modules['RPi'] = fake_rpi.RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO
    import RPi.GPIO as GPIO
else:
    import RPi.GPIO as GPIO


class Detect(Thread):
    """Launche the detector."""

    def __init__(self):
        """Initialise pin raspberry and var."""
        Thread.__init__(self)
        self.capteur = 7
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.capteur, GPIO.IN)
        time.sleep(2)
        self.move = False
        self.submit_mail = False

    def run(self):
        """Detect loop changes the status of self.move and sends an email to users."""
        while True:
            time.sleep(0.1)
            if settings.ALARME:
                if GPIO.input(self.capteur):
                    self.move = True
                    if not self.submit_mail:
                        subject = "ALARME: Détection de mouvement !"
                        message = "Il y a actuellement une activation de l'alarme\nURL de l'alarme:http://{}".format(settings.ALLOWED_HOSTS[0])
                        email = MyUser.objects.all().values_list('email')
                        email_list = [e[0] for e in email]
                        send = Sendmail()
                        send.sendmail(email_list, subject, message)
                        self.submit_mail = True
                else:
                    self.move = False
                    self.submit_mail = False
