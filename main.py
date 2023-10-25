import cv2

#from blob_detector import BlobDetector
#from colour_detector import ColourDetector
#from video import Video
from kinect_video import KinectVideo

def main():
    #current_video = Video()
    #current_video.start()
    current_video = KinectVideo()
    current_video.start()
    #col_detector = ColourDetector()
    #blob_detector = BlobDetector()
    #blob_detector.start()

    #print(col_detector.colour_channels)

    #def pass_image_to_color_detec():
    #    nonlocal current_video
    #    nonlocal col_detector
    #    col_detector.current_frame = current_video.frame

    #def pass_blue_to_blob_detec():
    #    nonlocal col_detector
    #    nonlocal blob_detector
    #    blob_detector.current_frame = col_detector.blue_channel


    # use while loop to keep it active and looping
    while True:
        #pass_image_to_color_detec()
        #col_detector.display_image()
        #blob_detector.display_image()
        rgb, depth = current_video.frame, current_video.depth_frame
        current_video.display_image()


        if cv2.waitKey(1) & 0xff == 27: break

    #current_video.end()
    #col_detector.end()
    #blob_detector.end()


if __name__ == '__main__':
    main()
