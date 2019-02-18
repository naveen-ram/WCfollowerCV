import cv2
import argparse
from frame_processing import Ind_Frame_Processing

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
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame,(480,360))
        basic_processing = Ind_Frame_Processing(frame)
        key_points, descriptors = basic_processing.FASTKeyPointDetection()

#TODO: we can't use drawKeypoints for another couple days due to errors
#        frame = cv2.drawKeypoints(frame,kp,color=(0,255,0), flags=0)
        for marker in key_points:
        	frame = cv2.drawMarker(frame, tuple(int(i) for i in marker.pt), color=(0, 255, 0))
        cv2.imshow('frame',frame)
        cv2.waitKey(1) #this is to slow down each frame
    else:
        cv2.destroyAllWindows()
        cap.release()


#d = Display(480,360)


#d.create_window("test_vids/right.h264")
