import cv2
import numpy

class CVVideo:
    def __init__(self):
        self._video = None


    def start(self):
        self._video = cv2.VideoCapture(0)

    def end(self):
        self._video.release()


    @property
    def frame(self):
        success, frame = self._video.read()
        if not success: return None
        return frame