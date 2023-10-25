import cv2

from colour_detector import ColourDetector
from display import Display
from kinect_video import KinectVideo
from opencv_video import CVVideo

def main():
    # init new objects
    display = Display()
    #current_video = KinectVideo() #untested
    current_video = CVVideo() #temporary, works with laptop camera
    current_video.start()
    col_detector = ColourDetector()


    # every frame, the frame from the current video should be passed to the colour detector
    def pass_image_to_color_detec():
        nonlocal current_video
        nonlocal col_detector
        col_detector.current_frame = current_video.frame

    # every frame, the frames from the colour detector should be passed to the display to display
    def pass_frames_to_display():
        nonlocal display
        nonlocal col_detector
        nonlocal current_video

        display.add_channel_to_show("blue", col_detector.blue_channel)
        display.add_channel_to_show("red", col_detector.red_channel)
        display.add_channel_to_show("yellow", col_detector.yellow_channel)
        display.add_channel_to_show("green", col_detector.green_channel)
        display.add_channel_to_show("kinectrgb", current_video.frame)
        #display.add_channel_to_show("kinectdepth", current_video.depth_frame)

    # use while loop to keep it active and looping
    # MAINLOOP of program
    while True:

        pass_image_to_color_detec()
        pass_frames_to_display()

        # display the frames passed to it
        display.display_images()

        # checks every loop if the esc key is pressed: may need to hold down esc as the detection and press happen at
        # different times
        if cv2.waitKey(1) & 0xff == 27: break

    # disconnect the display and opencv video
    display.end()
    current_video.end()


if __name__ == '__main__':
    main()
