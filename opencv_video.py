import cv2
import numpy

class CVVideo:
    def __init__(self):
        self._video = None

    def start(self):
        # the int parameter passed to VideoCapture specifies the camera to use
        # you can connect more cameras through usb and use them instead by changing the int
        self._video = cv2.VideoCapture(0)

    def end(self):
        # disconnect video
        self._video.release()

    @property
    def frame(self):
        success, frame = self._video.read()
        if not success: return None
        return frame