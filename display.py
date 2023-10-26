import cv2
import numpy


class Display:
    def __init__(self):
        self.channels = dict()

    def add_channel_to_show(self, name, image):
        self.channels[name] = image

    def display_images(self):
        for name in self.channels.keys():
            cv2.imshow(name, self.channels[name])
            self.channels[name] = None
        # waitKey(1) displays for 1 millisecond then gets updated by the next image passed to it
        cv2.waitKey(1)

    def end(self):
        cv2.destroyAllWindows()