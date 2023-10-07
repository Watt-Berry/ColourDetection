import asyncio
import time

from colour_detector import ColourDetector
from input_handler import InputHandler
from pynput.keyboard import Key


async def main():
    inp_handler = InputHandler()
    col_detector = ColourDetector()

    keep_looping = True

    def esc_main():
        nonlocal keep_looping
        keep_looping = False

    def switch_col_detec(): col_detector.keep_running = not col_detector.keep_running
    def switch_inp_handl(): inp_handler.keep_running = not inp_handler.keep_running
    switch_inp_handl()
    inp_handler.attach_func_to_keypress("enter", switch_col_detec)
    inp_handler.attach_func_to_keypress(Key.esc, esc_main)

    # use while loop to keep it active and looping
    while keep_looping:
        pass


if __name__ == '__main__':
    asyncio.run(main())