import numpy as np
import cv2
import time
import random
import collections
from PIL import Image
import os
import urllib.request
from tensorflow.keras.models import load_model


class StopSignDetector(object):
    def __init__(self, min_score, max_reverse_count=0, reverse_throttle=-0.5, debug=False):
        self.last_5_scores = collections.deque(np.zeros(5), maxlen=5)

        #self.STOP_SIGN_CLASS_ID = 12
        self.min_score = min_score
        self.debug = debug
        self.model_name = 'liftModel'
        self.model = load_model('models/lightweight_cnn_model-2-2.h5')

        # reverse throttle related
        self.max_reverse_count = max_reverse_count
        self.reverse_count = max_reverse_count
        self.reverse_throttle = reverse_throttle
        self.is_reversing = False

    def convertImageArrayToPILImage(self, img_arr):
        img = np.array(img_arr)
        return img

    def detect_elevator_door (self, img_arr):
        # Model inference
        img = np.array(img_arr)
        bimage = np.expand_dims(img, axis=0)
        prediction = self.model.predict(bimage)[0][0]
        return prediction >= 0.5


    def run(self, img_arr, throttle, debug=False):
        if img_arr is None:
            return throttle, img_arr
        if self.detect_elevator_door(img_arr):
            #self.is_reversing = True
            #self.reverse_count += 1
            print('lift')
            return self.reverse_throttle, img_arr
        else:
            print('faaakkk')
            self.is_reversing = False
            self.reverse_count = 0
            return throttle, img_arr



