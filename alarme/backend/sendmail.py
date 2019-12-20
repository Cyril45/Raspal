"""Main base of the video flow."""
from django.core.mail import send_mail
from django.conf import settings


class Sendmail():
    """Email sending class."""

    def sendmail(self, email_list, subject, message):
        """Allow to send an email."""
        email_from = settings.EMAIL_HOST_USER
        if isinstance(email_list, list) is False:
            email_list = [email_list]
        send_mail(subject, message, email_from, email_list)
