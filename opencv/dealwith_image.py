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
