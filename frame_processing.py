import cv2
import numpy as np
import scipy
import _pickle as pickle
import random
import os
#import matplotlib.pyplot as plt


class Ind_Frame_Processing():
    def __init__(self, frame):
        self.frame = frame

    def cannyEdgeDetection(self):
        edges = cv2.Canny(self.frame,100,200)
        return edges

    #TODO: Current ORB detection method is still not great because it is very innacurate. Gotta use a better one.
    def orbKeyPointDetection(self):
        orb = cv2.ORB_create(edgeThreshold=2,WTA_K=3,scoreType=2)
        kp = orb.detect(self.frame,None)
        #kp, des = orb.compute(self.frame, kp)
        return kp