import time
import asyncio
from colour_detector import ColourDetector


def main():
    col_detector = ColourDetector()
    print(col_detector.colour_channels)
    print(col_detector.image_to_process)
    keep_looping = True

    def pass_image_to_color_detec(image):
        nonlocal col_detector
        col_detector.image_to_process = image

    # use while loop to keep it active and looping
    new_img = None
    while keep_looping:
        inp = input("enter command > ")
        if inp == "ei": # enter image
            pass_image_to_color_detec("test.jpg")
        elif inp == "esc": # escape
            keep_looping = False
        elif inp == "red": # red channel
            new_img = col_detector.red_channel
        elif inp == "blue": # blue channel
            new_img = col_detector.blue_channel
        elif inp == "green": # green channel
            new_img = col_detector.green_channel
        elif inp == "green2":
            col_detector.display_image(channel="GREEN")
        elif inp == "base": # base channel
            new_img = col_detector.base_channel
        elif inp == "black" or inp == "white":
            new_img = col_detector.grayscale_channel
        elif inp == "show": # show image
            col_detector.display_image(image=new_img)

        # test if gotten image
        print(new_img)


if __name__ == '__main__':
    main()