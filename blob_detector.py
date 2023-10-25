import cv2
import numpy


class BlobDetector:
    def __init__(self):
        self._frame = None
        self._blobs = None
        self._detector = cv2.SimpleBlobDetector()

    @property
    def current_frame(self):
        return self._frame

    @current_frame.setter
    def current_frame(self, frame):
        if not (frame is None):
            self._frame = frame
            self._process_image()


    def _process_image(self):
        blobs = self._detector.detect(self._frame)
        im_with_keypoints = cv2.drawKeypoints(self._frame, blobs, numpy.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        self._blobs = im_with_keypoints


    def display_image(self):
        cv2.imshow("blobs", self._blobs)
        cv2.waitKey(1)

    def end(self):
        cv2.destroyAllWindows()
