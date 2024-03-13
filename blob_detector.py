import cv2
import numpy as np

class BlobDetector:
    def __init__(self):
        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector.Params()

        params.filterByColor = True
        params.blobColor = 255

        params.filterByArea = True
        params.minArea = 1_000
        params.maxArea = 10_000_000

        self._detector = cv2.SimpleBlobDetector.create(params)

        self._blobs = None

    @property
    def blobs(self):
        return self._blobs

    # the image passed should be the mask as the mask is white/black
    def process_image(self, img):
        # Detect blobs.
        keypoints = self._detector.detect(image=img)

        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        self._blobs = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

