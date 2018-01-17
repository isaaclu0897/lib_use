# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 01:33:33 2017

@author: wei
"""

import cv2
import requests
import PIL.Image as Image
import matplotlib.pyplot as plt
import numpy


with open('kaptcha.jpg', 'wb') as f:
    res = requests.get('http://gcis.nat.gov.tw/pub/kaptcha.jpg')
    f.write(res.content)

image = plt.imread('kaptcha.jpg')
plt.imshow(image)
open_cv_img = numpy.array(image)
imgray = 
