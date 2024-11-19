import numpy as np
import cv2
import time
import random
import collections
from PIL import Image
import os
import urllib.request


class ElevatorDoorDetector(object):
    def __init__(self, min_score, show_bounding_box, max_reverse_count=0, reverse_throttle=-0.5, debug=False):
        self.last_5_scores = collections.deque(np.zeros(5), maxlen=5)

        #self.STOP_SIGN_CLASS_ID = 12
        self.min_score = min_score
        self.show_bounding_box = show_bounding_box
        self.debug = debug

        # reverse throttle related
        self.max_reverse_count = max_reverse_count
        self.reverse_count = max_reverse_count
        self.reverse_throttle = reverse_throttle
        self.is_reversing = False

    def convertImageArrayToPILImage(self, img_arr):
        img = Image.fromarray(img_arr.astype('uint8'), 'RGB')

        return img
    

    def detect_elevator_door (self, img_arr):
        return None


    def run(self, img_arr, throttle, debug=False):
        if img_arr is None:
            return throttle, img_arr
        if self.reverse_count < self.max_reverse_count:
            self.is_reversing = True
            self.reverse_count += 1
            return self.reverse_throttle, img_arr
        else:
            self.is_reversing = False
            self.reverse_count = 0
            return throttle, img_arr