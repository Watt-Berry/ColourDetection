import cv2
import numpy as np

class CVVideo:
    def __init__(self, width, height):
        self._video = None
        self._w, self._h = width, height #temporary arguments, only used when starting and setting the resolution

    def start(self):
        # the int parameter passed to VideoCapture specifies the camera to use
        # you can connect more cameras through usb and use them instead by changing the int
        self._video = cv2.VideoCapture(0)
        self._set_resolution()

    # the VIDEO CAPTURE should be resized instead of the display
    # this is because changing the video capture will ensure an appropriate resolution
    # however changing the resolution of the display will upscale the image and make it look lower res
    def _set_resolution(self):
        self._video.set(3, self._w)
        self._video.set(4, self._h)

    def end(self):
        # disconnect video
        self._video.release()

    @property
    def frame(self):
        success, frame = self._video.read()
        if not success: return None
        return frame



#from freenect import sync_get_depth as get_depth, sync_get_video as get_video
# TODO: test if this is working in main, on the raspberry pi

class KinectVideo:

    @property
    def frame(self):
        #(rgb, _) = get_video()
        #return cv2.imread(rgb)
        return None

    @property
    def depth_frame(self):
        #(depth, _) = get_depth()
        #return cv2.imread(depth)
        return None