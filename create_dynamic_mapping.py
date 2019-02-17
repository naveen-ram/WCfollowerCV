import cv2
import argparse

"""
class SLAM(object):
    ## First step is to create a display
    def __init__(self, W, H):
        self.W = W
        self.H = H
        d = Display(W,H)
        d.createWindow()

SLAM(800,800)
"""

parser = argparse.ArgumentParser(description='location of video')
parser.add_argument('source', type=str, help='Location of video')
args = parser.parse_args()


cap = cv2.VideoCapture(args.source)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(480,360))
        cv2.imshow('frame',frame)
        cv2.waitKey(1)
    else:
        cv2.destroyAllWindows()
        cap.release()


#d = Display(480,360)


#d.create_window("test_vids/right.h264")
