"""Main base of the video flow."""
import cv2
import threading
import time


class Flux(threading.Thread):
    """Launch the flow."""

    def __init__(self):
        """Launch the camera and first image playback."""
        threading.Thread.__init__(self)
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()

    def run(self):
        """Image update loop."""
        while True:
            time.sleep(0.01)  
            (self.grabbed, self.frame) = self.video.read()

    def get_frame(self):
        """Retrieve a readable image for html5 img tag."""
        while True:
            time.sleep(0.01)
            ret, jpeg = cv2.imencode('.jpg', self.frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() +
                   b'\r\n')
