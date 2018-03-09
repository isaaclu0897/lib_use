#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:45:14 2018

@author: wei
"""
#開啟圖片

import cv2 # 引入opencv模塊

# 讀取欲處理的圖片
im = cv2.imread('girl.png')

# 開啟所讀入的圖片
''' cv2.imshow(winname, mat)
    
    winname: 視窗名稱
    mat    : 欲開啟的圖片
'''
cv2.imshow('good', im) 