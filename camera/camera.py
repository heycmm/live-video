import platform

import cv2 as cv
import numpy as np
import base64
from PIL import Image

"""
摄像头和转码base64，相当于动画片
"""


class Camera:
    def __init__(self):

        self.__cap = cv.VideoCapture(0)
        self.__JPEG_HEADER = "data:image/jpeg;base64,"

    def read(self):
        if platform.system() == 'Linux':
            self.__cap = cv.VideoCapture(10)
        else:
            self.__cap = cv.VideoCapture(0)

        ret, frame = self.__cap.read()
        r, buf = cv.imencode(".jpeg", frame)
        dat = Image.fromarray(np.uint8(buf)).tobytes()
        img_date_url = self.__JPEG_HEADER + str(base64.b64encode(dat))[2:-1]
        return img_date_url
