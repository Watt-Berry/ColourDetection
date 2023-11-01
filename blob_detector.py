import cv2
import numpy


class BlobDetector:
    def __init__(self):
        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector.Params()

        params.filterByColor = True
        params.blobColor = 255

        params.minThreshold = 10

        params.maxThreshold = 250

        params.filterByArea = True
        params.minArea = 10

        self._detector = cv2.SimpleBlobDetector.create(params)

        self._blobs = None

    @property
    def blobs(self):
        return self._blobs

    def process_image(self, img, mask):
        # Detect blobs.
        keypoints = self._detector.detect(image=img, mask=mask)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        self._blobs = cv2.drawKeypoints(mask, keypoints, numpy.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

