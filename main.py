from colour_detector import ColourDetector
from input_handler import InputHandler
from pynput.keyboard import Key


def main():
    col_detector = ColourDetector()
    inp_handler = InputHandler()

    keep_looping = True

    def esc_main():
        nonlocal keep_looping
        keep_looping = False

    def switch_col_detec(): col_detector.keep_running = not col_detector.keep_running
    inp_handler.attach_func_to_keypress(Key.enter, switch_col_detec)
    inp_handler.attach_func_to_keypress(Key.esc, esc_main)

    # use while loop to keep it active and looping
    while keep_looping:
        pass


if __name__ == '__main__':
    main()