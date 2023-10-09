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
        inp = input("enter command > ")
        if inp == "ei": # enter image
            pass_image_to_color_detec("test.jpg")
        elif inp == "esc": # escape
            keep_looping = False
        elif inp == "red": # red channel
            success = col_detector.red_channel
        elif inp == "blue": # blue channel
            success = col_detector.blue_channel
        elif inp == "green": # green channel
            success = col_detector.green_channel
        elif inp == "base": # base channel
            success = col_detector.base_channel


if __name__ == '__main__':
    main()