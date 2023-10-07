# create class to detect a certain colour from image and return coordinates
import asyncio
import threading
import time


class ColourDetector:
    def __init__(self):
        # public so any outside code should be able to add an image to it
        self._received_image = None
        self._loop_i = 1

    # make the received_image variable a property
    @property
    def image_to_process(self):
        return self._received_image

    # add a 'listener' to the variable so that whenever a new image is passed it gets immediately processed and any
    # values are returned
    @image_to_process.setter
    def image_to_process(self, value: int):
        self._received_image = value
        print(self._loop_i)
        self._loop_i += 1

        self._process_image()

    # ProcessImage shouldn't be async as otherwise it might return variables with no value
    # should return maps of the image outlining each specific colour
    def _process_image(self) -> None:
        # get colour maps
        self._received_image = None
        print("processed image")