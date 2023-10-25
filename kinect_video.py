#from pykinect2 import PyKinectV2
#from pykinect2.PyKinectV2 import *
#from pykinect2 import PyKinectRuntime
import numpy
import cv2


class KinectVideo:
    def __init__(self):
        self._kinect = None

    def start(self):
        pass
        #self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

    def end(self):
        self._kinect.close()

    @property
    def frame(self):
        #colour_frame = self._kinect.get_last_color_frame()
        #colour_frame_data = self._kinect.color_frame_data
        rgb_image = self._kinect.getRGBImage()
        bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

        return bgr_image

    @property
    def depth_frame(self):
        return self._kinect.getDepthImage()

