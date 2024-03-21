import cv2

from colour_detector import ColourDetector
from display import Display
from videos import CVVideo, KinectVideo
from blob_detector import BlobDetector

from motor_controller import MotorController


# get rgb and depth frame from kinect
def get_frames(kinect_vid: KinectVideo):
    return [kinect_vid.frame, kinect_vid.depth_frame]


# find white and yellow objects in the frames
def get_objects(col_detec: ColourDetector, frame):
    col_detec.process_image(frame)
    return [ col_detec.yellow_channel, col_detec.grayscale_channel]

# get blobs from frame
def find_objects(blob_detec: BlobDetector, frame):
    blob_detec.process_image(frame)
    return blob_detec.blobs

# get distance to blobs from frame
def get_distance(kinect_vid: KinectVideo, frame):
    return kinect_vid.get_distance(frame)

# TODO: calculate distance and direction to object from frame
def get_directions(frame):
    return None


def main():
    # init display, kinect video, colour detector, blob detector
    display = Display()
    current_video = KinectVideo()
    col_detector = ColourDetector()
    blob_detector = BlobDetector()
    motor_control = MotorController()

    while True:
        # check if motor controller has reached its destination
        if motor_control.reached_destination():
            # if reached destination then look for more items
            frames = get_frames(current_video)
            objects_frames = get_objects(col_detector, frames[0])
            display.add_channel_to_show("objects", objects_frames)
            all_objects = {}
            for frame in objects_frames:
                points = find_objects(blob_detector, frame)
                distances = get_distance(current_video, points)
                all_objects[distances] = points

            # get the shortest distance from the list of all objects
            if not all_objects: continue
            shortest_distance_frame = all_objects[min(all_objects.keys())]
            directions = get_directions(shortest_distance_frame)

            # TODO: move motor controller based on directions

        else: pass

        display.display_images()
        if cv2.waitKey(1) & 0xff == 27: break


    display.end()
    current_video.end()


if __name__ == '__main__':
    main()
