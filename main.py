import cv2

from colour_detector import ColourDetector
from display import Display
from videos import CVVideo, KinectVideo
from blob_detector import BlobDetector

def main():
    # init new objects
    display = Display()
    #current_video = KinectVideo() #untested
    current_video = CVVideo(1280, 720) #temporary, works with laptop camera
    col_detector = ColourDetector()
    blob_detector = BlobDetector()

    # every frame, the frame from the current video should be passed to the colour detector
    # every frame, pass the video frame to the colour detector then to the blob detector
    def pass_frame_to_detectors():
        nonlocal current_video
        nonlocal col_detector, blob_detector
        col_detector.process_image(current_video.frame)
        blob_detector.process_image(img=col_detector.blue_mask)


    # every frame, the frames from the colour detector should be passed to the display to display
    def pass_frames_to_display():
        nonlocal display
        nonlocal col_detector
        nonlocal current_video
        nonlocal blob_detector

        display.add_channel_to_show("blue", col_detector.blue_channel)
        #display.add_channel_to_show("tracking", obj_tracker.object)
        #display.add_channel_to_show("red", col_detector.red_channel)
        #display.add_channel_to_show("yellow", col_detector.yellow_channel)
        #display.add_channel_to_show("green", col_detector.green_channel)

        #display.add_channel_to_show("kinectrgb", current_video.frame)
        #display.add_channel_to_show("kinectdepth", current_video.depth_frame)

        display.add_channel_to_show("blobs", blob_detector.blobs)

    # start the video capture
    current_video.start()

    # use while loop to keep it active and looping
    # MAINLOOP of program
    while True:
        pass_frame_to_detectors()
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
