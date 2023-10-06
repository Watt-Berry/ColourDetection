from colour_detector import ColourDetector
from input_handler import InputHandler
from pynput.keyboard import Key


def main():
    col_detector = ColourDetector()
    inp_handler = InputHandler()

    keep_looping = True
    def esc_main(flag): flag = False
    def set_col_detec(val): col_detector.keep_running = val
    inp_handler.attach_func_to_keypress(Key.enter, set_col_detec(True))
    inp_handler.attach_func_to_keypress(Key.esc, set_col_detec(False))
    inp_handler.attach_func_to_keypress('q', esc_main(keep_looping))

    while keep_looping:
        pass


if __name__ == '__main__':
    main()