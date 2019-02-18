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
        FAST = cv2.FastFeatureDetector_create(threshold = 15)
        kp = FAST.detect(self.frame,None)
        orb = cv2.ORB_create()
        dsp = orb.compute(self.frame,kp)
        return kp,dsp

    def FLANNfeatureMatching(self,dsp1,dsp2):
        # https://docs.opencv.org/3.4.3/dc/dc3/tutorial_py_matcher.html
        # FLANN parameters
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary
        flann = cv.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(dsp1,dsp2,k=2)
        # Need to draw only good matches, so create a mask
        matchesMask = [[0,0] for i in xrange(len(matches))]
        # ratio test as per Lowe's paper
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.7*n.distance:
                matchesMask[i]=[1,0]
        print(matchesMask)
