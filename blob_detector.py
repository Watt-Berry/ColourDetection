import cv2
import numpy


class BlobDetector:
    def __init__(self):
        self._detector = cv2.SimpleBlobDetector()

        self._blobs = None


    @property
    def frame(self):
        return self._blobs

    @frame.setter
    def frame(self, img):
        self._process_image(img)

    def _process_image(self, img):
        # Detect blobs.
        blue_mask = cv2.inRange(img, (100, 50, 50), (140, 255, 255))
        keypoints = self._detector.detect(image=img, mask=blue_mask)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        self._blobs = cv2.drawKeypoints(img, keypoints, numpy.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

