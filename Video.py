import cv2


class Video:
    def __init__(self):
        self._video = cv2.VideoCapture(0)

    @property
    def video(self):
        return self._video
