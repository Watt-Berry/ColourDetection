# create class to detect a certain colour from image; and return coordinates?
import cv2
import numpy

# TODO: add in option to calibrate colours somehow?


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
    # the images passed should be in BGR format
    @current_frame.setter
    def current_frame(self, frame=None):
        if not (frame is None):
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
        self._colour_channels["BLUE"] = blue_mask

        green_mask = cv2.inRange(hsv_image, (40, 50, 50), (80, 255, 255))
        self._colour_channels["GREEN"] = green_mask

        lower_red_mask = cv2.inRange(hsv_image, (0, 50, 50), (20, 255, 255))
        upper_red_mask = cv2.inRange(hsv_image, (160, 50, 50), (179, 255, 255))
        # in hsv, the red color loops around so need 2 masks for the start and end
        red_mask = lower_red_mask + upper_red_mask
        self._colour_channels["RED"] = red_mask

        yellow_mask = cv2.inRange(hsv_image, (20, 50, 50), (40, 255, 255))
        self._colour_channels["YELLOW"] = yellow_mask

        grayscale_image = cv2.cvtColor(self._video_frame, cv2.COLOR_BGR2GRAY)
        self._colour_channels["GRAYSCALE"] = grayscale_image

        self._colour_channels["BASE"] = self._video_frame
        self._colour_channels["HSV"] = hsv_image

    # public
    # the * makes it so that whenever the function is called, the parameter name has to be specified as well
    # allows for either image data to be passed to and rendered or a specific channel rendered
    def display_image(self, *, image=None, channel=None):
        if not (image is None):
            cv2.imshow("image", image)
        elif not (channel is None):
            cv2.imshow(channel, self._colour_channels[channel])
        else:
            cv2.imshow("base", self._colour_channels["BASE"])
            #cv2.imshow("hsv", self._colour_channels["HSV"])
            cv2.imshow("red", self._colour_channels["RED"])
            cv2.imshow("blue", self._colour_channels["BLUE"])
            cv2.imshow("green", self._colour_channels["GREEN"])
            cv2.imshow("yellow", self._colour_channels["YELLOW"])
            #cv2.imshow("gray", self._colour_channels["GRAYSCALE"])
        # waits 1 millisecond then nothing, makes it so that the image is updated every time this method is called
        cv2.waitKey(1)

    def end(self):
        cv2.destroyAllWindows()
