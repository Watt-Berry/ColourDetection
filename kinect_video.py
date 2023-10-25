from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import numpy
import cv2


class KinectVideo:
    def __init__(self):
        self._rgb_frame = None
        self._depth_frame = None

    @property
    def frame(self):
        (rgb, _) = get_video()

        rgb_image = cv2.imread(rgb)
        self._rgb_frame = rgb_image
        return cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

    @property
    def depth_frame(self):
        (depth, _) = get_depth()

        depth_image = cv2.imread(depth)
        self._depth_frame = depth_image
        return depth_image


    def display_image(self):
        cv2.imshow("rgb", self._rgb_frame)
        cv2.imshow("depth", self._depth_frame)
