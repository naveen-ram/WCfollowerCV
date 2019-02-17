import cv2
import numpy as np

class Ind_Frame_Processing():
    def __init__(self, frame):
        self.frame = frame

    def cannyEdgeDetection(self):
        edges = cv2.Canny(self.frame,100,200)
        return edges

    def orbKeyPointDetection(self):
        orb = cv2.ORB_create()
        kp = orb.detect(self.frame,None)
        #kp, des = orb.compute(self.frame, kp)
        return kp
