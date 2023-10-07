import cv2


class Camera:
    def __init__(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            img = cv2.imread(frame, 1)
            cv2.imshow("preview", img)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break

        cv2.destroyWindow("preview")
        vc.release()