import cv2
import argparse
import numpy as np
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

thisdict =	{
  "keyPoint": (0,0,255),
  "fMatch": (0,255,0)
}
counter = 0
prev_key_points = None
prev_descriptors = None
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame,(480,360))
        basic_processing = Ind_Frame_Processing(frame)
        key_points1, descriptors1 = basic_processing.FASTKeyPointDetection()
        #if counter > 0:
            #print("Hello")
#        if cap.grab():
#        ret2, frame2 = cap.retrieve()
#        if ret2 == True:
#            basic_processing_forward = Ind_Frame_Processing(frame2)
#            key_points2, descriptors2 = basic_processing_forward.FASTKeyPointDetection()
#            print(key_points2)
#            FLANNfeatureMatching(descriptors1,descriptors2)

#        TODO: we can't use drawKeypoints for another couple days due to errors
#        frame = cv2.drawKeypoints(frame,kp,color=(0,255,0), flags=0)

#        blank_frame = np.zeros((360,480,3), np.uint8)
        for marker in key_points1:
#            blank_frame = cv2.drawMarker(blank_frame, tuple(int(i) for i in marker.pt), color=(255,0,0))
            frame = cv2.circle(frame, tuple(int(i) for i in marker.pt), color=thisdict["keyPoint"],radius=3)


        cv2.imshow('frame',frame)
#        cv2.imshow('points',blank_frame)
        cv2.waitKey(1) #this is to slow down each frame
        prev_key_points = key_points1
        old_descriptors = descriptors1
        counter = counter + 1
    else:
        cv2.destroyAllWindows()
        cap.release()
