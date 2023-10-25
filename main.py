import cv2

#from blob_detector import BlobDetector
from colour_detector import ColourDetector
from display import Display
from kinect_video import KinectVideo

def main():
    display = Display()
    current_video = KinectVideo()
    col_detector = ColourDetector()

    #blob_detector = BlobDetector()
    #blob_detector.start()

    print(col_detector.colour_channels)

    def pass_image_to_color_detec():
        nonlocal current_video
        nonlocal col_detector
        col_detector.current_frame = current_video.frame

    def pass_frames_to_display():
        nonlocal display
        nonlocal col_detector
        nonlocal current_video

        display.add_channel_to_show("blue", col_detector.blue_channel)
        display.add_channel_to_show("blue", col_detector.blue_channel)
        display.add_channel_to_show("red", col_detector.red_channel)
        display.add_channel_to_show("yellow", col_detector.yellow_channel)
        display.add_channel_to_show("green", col_detector.green_channel)
        display.add_channel_to_show("kinectrgb", current_video.frame)
        display.add_channel_to_show("kinectdepth", current_video.depth_frame)

    #def pass_blue_to_blob_detec():
    #    nonlocal col_detector
    #    nonlocal blob_detector
    #    blob_detector.current_frame = col_detector.blue_channel


    # use while loop to keep it active and looping
    while True:
        pass_image_to_color_detec()
        pass_frames_to_display()

        display.display_images()

        if cv2.waitKey(1) & 0xff == 27: break

    display.end()
    #blob_detector.end()


if __name__ == '__main__':
    main()
