# create class to detect a certain colour from image; and return coordinates?
import asyncio
import threading
import time
import cv2
import numpy


class ColourDetector:
    def __init__(self):
        # private video frame, should pass from the Video class
        self._video_frame = None

        # private
        # TODO: add in orange or yellow channel
        # TODO: add in option to calibrate colours somehow?
        # each value will have the result and the mask
        self._colour_channels = {"BASE": [],
                                 "RED": [], "GREEN": [], "BLUE": [], "ORANGE": [],
                                 "GRAYSCALE": []}

    @property
    def current_frame(self):
        return self._video_frame

    # listener for frames to be passed
    @current_frame.setter
    def current_frame(self, frame):
        if not (frame is None):
            self._video_frame = frame
            self._process_frame()
        return

    # public properties to return the private values
    @property
    def colour_channels(self):
        return self._colour_channels.keys()

    @property
    def base_channel(self):
        # the specific channels refer to the public colour_channels property instead?? unsure if needed
        return self._colour_channels["BASE"]

    @property
    def red_channel(self):
        return self._colour_channels["RED"]

    @property
    def green_channel(self):
        return self._colour_channels["GREEN"]

    @property
    def blue_channel(self):
        return self._colour_channels["BLUE"]

    @property
    def orange_channel(self):
        return self._colour_channels["ORANGE"]

    @property
    def grayscale_channel(self):
        return self._colour_channels["GRAYSCALE"]

    # ProcessImage shouldn't be async as otherwise it might return variables with no value
    def _process_frame(self) -> None:
        # self._video_frame is already an image so just need to copy and convert to colour channels
        # don't need to imread the frame as it's already an image

        # convert the image to hsv
        hsv_image = cv2.cvtColor(self._video_frame, cv2.COLOR_BGR2HSV)
        #image = self._video_frame

        # for each colour:
        # get the bound for each colour by converting rgb values to hsv
        # upper bound = val + 10, lower bound = val - 10
        # to get bounds of a colour example:
            # >>> green = np.uint8([[[0,255,0 ]]])
            # >>> hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
            # >>> print( hsv_green )

        # create a mask for the wanted colour
        # get the result from the frame and the mask
        # set the result to the dictionary
        # bgr colour array = [blue, green, red]

        lower_blue = numpy.array([110, 100, 100])
        upper_blue = numpy.array([130, 255, 255])
        blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        # bitwise_and takes 2 images as src1 and src2 incase one of them is invalid?
        self._colour_channels["BLUE"] = [cv2.bitwise_and(hsv_image, hsv_image, mask=blue_mask), blue_mask]

        lower_green = numpy.array([50, 100, 100])
        upper_green = numpy.array([70, 255, 255])
        green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
        self._colour_channels["GREEN"] = [cv2.bitwise_and(hsv_image, hsv_image, mask=green_mask), green_mask]

        lower_red = numpy.array([0, 100, 100])
        upper_red = numpy.array([20, 255, 255])
        red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
        self._colour_channels["RED"] = [cv2.bitwise_and(hsv_image, hsv_image, mask=red_mask), red_mask]

        lower_black = numpy.array([0, 100, 100])
        upper_black = numpy.array([0, 255, 255])
        black_mask = cv2.inRange(hsv_image, lower_black, upper_black)
        self._colour_channels["GRAYSCALE"] = [cv2.bitwise_and(hsv_image, hsv_image, mask=black_mask), black_mask]

        self._colour_channels["BASE"] = [hsv_image, hsv_image]

    # public
    # the * makes it so that whenever the function is called, the parameter name has to be specified as well
    # allows for either image data to be passed to and rendered or a specific channel rendered
    def display_image(self, *, image=None, channel=None):
        if not (image is None):
            cv2.imshow("image", image)
        elif not (channel is None):
            cv2.imshow(channel, self._colour_channels[channel][0])
            cv2.imshow(channel + "mask", self._colour_channels[channel][1])
        else:
            print("no image or channel supplied")
            return
        cv2.waitKey(0)
        cv2.destroyAllWindows()