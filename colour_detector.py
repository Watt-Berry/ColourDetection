# create class to detect a certain colour from image and return coordinates
import time

import cv2


class ColourDetector:
    def __init__(self):
        # private but the image to process property is a public variable that returns this value,
        # used to prevent any outside code from directly altering the value
        self._received_image = None

        # private
        self._colour_channels = {"BASE": None, "RED": None, "GREEN": None, "BLUE": None}

    # make the received_image variable a property
    @property
    def image_to_process(self):
        return self._received_image

    # add a 'listener' to the variable so that whenever a new image is passed it gets immediately processed and any
    # values are returned
    @image_to_process.setter
    def image_to_process(self, value: str):
        self._received_image = cv2.imread(value, flags=cv2.IMREAD_REDUCED_COLOR_2)
        self._process_image()

    @property
    def colour_channels(self):
        return self._colour_channels

    @colour_channels.getter
    def base_channel(self):
        try:
            cv2.imshow("base", self._colour_channels["BASE"])
            cv2.waitKey(0)
            cv2.destroyWindow("base")
            return True
        except: return False

    @colour_channels.getter
    def red_channel(self):
        try:
            cv2.imshow("red", self._colour_channels["RED"])
            cv2.waitKey(0)
            cv2.destroyWindow("red")
            return True
        except: return False


    @colour_channels.getter
    def green_channel(self):
        try:
            cv2.imshow("green", self._colour_channels["GREEN"])
            cv2.waitKey(0)
            cv2.destroyWindow("green")
            return True
        except: return False

    @colour_channels.getter
    def blue_channel(self):
        try:
            cv2.imshow("blue", self._colour_channels["BLUE"])
            cv2.waitKey(0)
            cv2.destroyWindow("blue")
            return True
        except: return False

    # ProcessImage shouldn't be async as otherwise it might return variables with no value
    # should return maps of the image outlining each specific colour
    def _process_image(self) -> None:
        print("image received is", self._received_image)

        red_only = self._received_image.copy()
        # blue channel = [:, :, 0] green channel = [:, :, 1] red channel = [:, :, 2]
        # set blue and green channels to 0
        red_only[:, :, 0] = 0
        red_only[:, :, 1] = 0

        green_only = self._received_image.copy()
        # set blue and red channels to 0
        green_only[:, :, 0] = 0
        green_only[:, :, 2] = 0

        blue_only = self._received_image.copy()
        # set green and red channels to 0
        blue_only[:, :, 1] = 0
        blue_only[:, :, 2] = 0

        self._colour_channels["BASE"] = self._received_image
        self._colour_channels["RED"] = red_only
        self._colour_channels["GREEN"] = green_only
        self._colour_channels["BLUE"] = blue_only

        # get colour maps
        self._received_image = None
        print("processed image")
