import asyncio
import threading
import time

from colour_detector import ColourDetector
from input_handler import InputHandler
from pynput.keyboard import Key


def main():
    inp_handler = InputHandler()
    col_detector = ColourDetector()
    image = 0

    keep_looping = True

    def esc_main():
        nonlocal keep_looping
        keep_looping = False

    def pass_image_to_color_detec():
        nonlocal col_detector
        col_detector.image_to_process = image

    inp_handler.attach_func_to_keypress(Key.enter, pass_image_to_color_detec)
    inp_handler.attach_func_to_keypress(Key.esc, esc_main)

    # use while loop to keep it active and looping
    while keep_looping:
        image += 1
        time.sleep(1)


if __name__ == '__main__':
    main()