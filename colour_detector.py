# create class to detect a certain colour from image; and return coordinates?
import asyncio
import threading
import time
import cv2


class ColourDetector:
    def __init__(self):
        # private but the image to process property is a public variable that returns this value,
        # used to prevent any outside code from directly altering the value
        self._rgb_image = None
        self._grayscale_image = None
        # private
        self._colour_channels = {"BASE": None,
                                 "RED": None, "GREEN": None, "BLUE": None,
                                 "GRAYSCALE": None}

    # make the received_image variable a property
    @property
    def image_to_process(self):
        return self._rgb_image or self._grayscale_image

    # add a 'listener' to the variable so that whenever a new image is passed it gets immediately processed and any
    # values are returned
    @image_to_process.setter
    def image_to_process(self, path: str):
        self._rgb_image = cv2.imread(path, flags=cv2.IMREAD_REDUCED_COLOR_2)
        self._grayscale_image = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_2)
        self._process_image()

    # public properties to return the private values
    @property
    def colour_channels(self):
        return self._colour_channels

    @property
    def base_channel(self):
        # the specific channels refer to the public colour_channels property instead?? unsure if needed
        return self.colour_channels["BASE"]

    @property
    def red_channel(self):
        return self.colour_channels["RED"]

    @property
    def green_channel(self):
        return self.colour_channels["GREEN"]

    @property
    def blue_channel(self):
        return self.colour_channels["BLUE"]

    @property
    def grayscale_channel(self):
        return self.colour_channels["GRAYSCALE"]

    # ProcessImage shouldn't be async as otherwise it might return variables with no value
    def _process_image(self) -> None:
        red_only = self._rgb_image.copy()
        # blue channel = [:, :, 0] green channel = [:, :, 1] red channel = [:, :, 2]
        # set blue and green channels to 0
        red_only[:, :, 0] = 0
        red_only[:, :, 1] = 0

        green_only = self._rgb_image.copy()
        # set blue and red channels to 0
        green_only[:, :, 0] = 0
        green_only[:, :, 2] = 0

        blue_only = self._rgb_image.copy()
        # set green and red channels to 0
        blue_only[:, :, 1] = 0
        blue_only[:, :, 2] = 0

        # set colour maps
        self._colour_channels["GRAYSCALE"] = self._grayscale_image
        self._colour_channels["BASE"] = self._rgb_image
        self._colour_channels["RED"] = red_only
        self._colour_channels["GREEN"] = green_only
        self._colour_channels["BLUE"] = blue_only

        # set the image to None just in case it may cause errors with newly passing images
        self._received_image = None

    # public
    # the * makes it so that whenever the function is called, the parameter name has to be specified as well
    # allows for either image data to be passed to and rendered or a specific channel rendered
    def display_image(self, *, image=None, channel=None):
        if not (image is None):
            cv2.imshow("image", image)
        elif not (channel is None):
            cv2.imshow(channel, self.colour_channels[channel])
        else:
            print("no image or channel supplied")
            return
        cv2.waitKey(0)
        cv2.destroyAllWindows()