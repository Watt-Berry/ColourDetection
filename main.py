import time
import asyncio
from colour_detector import ColourDetector
from video import Video


def main():
    current_video = Video()
    current_video.start()
    col_detector = ColourDetector()
    print(col_detector.colour_channels)
    keep_looping = True

    def pass_image_to_color_detec():
        nonlocal current_video
        nonlocal col_detector
        col_detector.current_frame = current_video.frame

    # use while loop to keep it active and looping
    new_img = None
    i = 0
    while i < 2_000:
        pass_image_to_color_detec()
        col_detector.display_image()

        i += 1

    current_video.end()


if __name__ == '__main__':
    main()
