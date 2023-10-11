import cv2


class Video:
    def __init__(self):
        self._video = cv2.VideoCapture(0)

    @property
    def frame(self):
        # .read() of a video returns 2 arguments: whether it was successful, and the image
        success, frame = self._video.read()
        if not success:
            return None
        return frame