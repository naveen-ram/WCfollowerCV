import cv2
import numpy as np
import scipy
import _pickle as pickle
import random
import os
import time
#import matplotlib.pyplot as plt


class Ind_Frame_Processing():
    def __init__(self, frame):
        self.frame = frame

    def cannyEdgeDetection(self):
        edges = cv2.Canny(self.frame,100,200)
        return edges

    #TODO: Current ORB detection method is still not great because it is very innacurate. Gotta use a better one.
    def orbKeyPointDetection(self):
        orb = cv2.ORB_create()
        kp = orb.detect(self.frame,None)
        #kp, des = orb.compute(self.frame, kp)
        return kp

    def FASTKeyPointDetection(self):
#        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        FAST = cv2.FastFeatureDetector_create()
        kp = FAST.detect(self.frame,None)
        orb = cv2.ORB_create()
        dsp = orb.compute(self.frame,kp)
        return kp,dsp
