# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 21:33:30 2017

@author: VX
"""
# 基本用法
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2

x1 = np.linspace(-10, 10, 6) # 在-10到10之間生成6個數據點，分成5等分

x2 = np.arange(-10, 11, 4)  # 每4產生一數據點，把線段分成5等分"注意11，range含下、不含上"

# 產生圖像
plt.figure()
plt.plot(x1, f(x1), 'r')

plt.figure()
plt.plot(x2, f(x2), 'g')

#plt.show()

