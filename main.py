import time

from colour_detector import ColourDetector


def main():
    col_detector = ColourDetector()
    keep_looping = True

    def pass_image_to_color_detec(image):
        nonlocal col_detector
        col_detector.image_to_process = image

    # use while loop to keep it active and looping
    while keep_looping:
        inp = input("enter command")
        if inp == "enter":
            pass_image_to_color_detec("test.jpg")
        elif inp == "esc":
            keep_looping = False


if __name__ == '__main__':
    main()