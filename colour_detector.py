# create class to detect a certain colour from image; and return coordinates?
import cv2
import numpy

# TODO: add in option to calibrate colours somehow?

# README: colour detector takes 1 image as its input to current_frame
# README: once its passed the image, it processes it and each colour channel can be accessed


class ColourDetector:
    def __init__(self):
        # private video frame, should pass from the Video class
        self._video_frame = None

        # private
        # each value will have the result and the mask
        self._colour_channels = {"BASE": None, "HSV": None,
                                 "RED": None, "GREEN": None, "BLUE": None, "YELLOW": None,
                                 "GRAYSCALE": None}

    # public properties to return the private values
    @property
    def colour_channels(self):
        return self._colour_channels.keys()

    @property
    def base_channel(self):
        return self._colour_channels["BASE"]

    @property
    def hsv_channel(self):
        return self._colour_channels["HSV"]

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
    def yellow_channel(self):
        return self._colour_channels["YELLOW"]

    @property
    def grayscale_channel(self):
        return self._colour_channels["GRAYSCALE"]

    @property
    def current_frame(self):
        return self._video_frame

    # listener for frames to be passed
    # the images passed should be rgb, if any changes to the image format changed then change the cvtColor that happens
    @current_frame.setter
    def current_frame(self, frame=None):
        if not (frame is None):

            # make sure that bgr images are passed, if rgb is passed then it will cause some issues with the
            # red and blue channels being switched
            self._video_frame = frame
            self._process_frame()
        return

    def _process_frame(self) -> None:
        # self._video_frame is already an image so just need to copy and convert to colour channels
        # don't need to imread the frame as it's already an image

        # convert the image to hsv
        hsv_image = cv2.cvtColor(self._video_frame, cv2.COLOR_BGR2HSV)

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


        blue_mask = cv2.inRange(hsv_image, (100, 50, 50), (140, 255, 255))
        # bitwise_and takes 2 hsv_images as src1 and src2 incase one of them is invalid?
        self._colour_channels["BLUE"] = cv2.cvtColor(cv2.bitwise_and(hsv_image, hsv_image, mask=blue_mask), cv2.COLOR_HSV2BGR)

        green_mask = cv2.inRange(hsv_image, (40, 50, 50), (80, 255, 255))
        self._colour_channels["GREEN"] = cv2.cvtColor(cv2.bitwise_and(hsv_image, hsv_image, mask=green_mask), cv2.COLOR_HSV2BGR)

        lower_red_mask = cv2.inRange(hsv_image, (0, 50, 50), (20, 255, 255))
        upper_red_mask = cv2.inRange(hsv_image, (160, 50, 50), (179, 255, 255))
        # in hsv, the red color loops around so need 2 masks for the start and end
        red_mask = lower_red_mask + upper_red_mask
        self._colour_channels["RED"] = cv2.cvtColor(cv2.bitwise_and(hsv_image, hsv_image, mask=red_mask), cv2.COLOR_HSV2BGR)

        yellow_mask = cv2.inRange(hsv_image, (20, 50, 50), (40, 255, 255))
        self._colour_channels["YELLOW"] = cv2.cvtColor(cv2.bitwise_and(hsv_image, hsv_image, mask=yellow_mask), cv2.COLOR_HSV2BGR)

        grayscale_image = cv2.cvtColor(self._video_frame, cv2.COLOR_BGR2GRAY)
        self._colour_channels["GRAYSCALE"] = grayscale_image

        self._colour_channels["BASE"] = self._video_frame
        self._colour_channels["HSV"] = hsv_image
