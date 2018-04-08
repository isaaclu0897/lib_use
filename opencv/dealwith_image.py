#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:45:14 2018

@author: wei
"""
#%% open picture

import cv2 # 引入opencv模塊

# 讀取欲處理的圖片
im = cv2.imread('raspberry.jpg')

# 開啟所讀入的圖片
''' cv2.imshow(winname, mat)
    
    winname: 視窗名稱
    mat    : 欲開啟的圖片
'''
cv2.imshow('good', im)
#%% findContours
import cv2
im = cv2.imread('raspberry.jpg')
# 由於opencv只能處裡灰度圖，所以要先用convert成灰階
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
binary,contours,hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(255, 0, 0), 2)
cv2.imshow('im', im)

#%% threshold optimize
import cv2
im = cv2.imread('raspberry.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,235,255,0)
binary,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(255, 0, 0), 2)
cv2.imshow('im', im)
#%% kinds of thresh compare
''' 何為閾值？
所謂的二值化是一種將影像中像素進行區分並放大的手段，
通常它會分成我們感興趣的部分作為前景，以及不感興趣的部分作為背景，
我們會以某個強度當作分割的標準，而這個強度便稱作閾值(threshold)，
所以通常強度超過閾值的像素當作前景，反之則為背景。
'''
import cv2
from matplotlib import pyplot as plt

im = cv2.imread('raspberry.jpg')  
img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#%% deal with GaussianBlur
import cv2
im = cv2.imread('raspberry.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,240,255,0)
GaussianBlur = cv2.GaussianBlur(thresh, (5, 5), 0)    
binary,contours,hierarchy = cv2.findContours(GaussianBlur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(255, 0, 0), 2)
cv2.imshow('im', im)

#%% deal with GaussianBlur
import cv2
from matplotlib import pyplot as plt

im = cv2.imread('raspberry.jpg')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,240,255,0)
GaussianBlur = cv2.GaussianBlur(thresh, (5, 5), 0)
binary,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

titles = ['thresh','GaussianBlur']
images = [thresh, GaussianBlur]

im = [im, im.copy()]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
    
#for i in range(2):
#    binary,contours,hierarchy = cv2.findContours(images[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    cv2.drawContours(im[i],contours,-1,(255, 0, 0), 2)
#    plt.subplot(1,2,i+1),plt.imshow(im[i], 'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()













