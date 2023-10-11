import time
import asyncio
from colour_detector import ColourDetector
from video import Video


def main():
    current_video = Video()
    col_detector = ColourDetector()
    print(col_detector.colour_channels)
    keep_looping = True

    def pass_image_to_color_detec():
        nonlocal current_video
        nonlocal col_detector
        col_detector.current_frame = current_video.frame

    # use while loop to keep it active and looping
    new_img = None
    while keep_looping:
        pass_image_to_color_detec()

        inp = input("enter command > ")
        try:
            col_detector.display_image(channel=inp.upper())
        except:
            if inp == "esc":
                keep_looping = False


if __name__ == '__main__':
    main()