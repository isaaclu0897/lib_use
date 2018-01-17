# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:19:22 2017

@author: VX
"""
# 圖像
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2

x = np.linspace(-10, 10, 100) 
x1 = np.linspace(-10, 10, 5)
'''plt.fig、plt.plot 用法
plt.fig(num=編號, figsize=(長,寬))
plt.plot(x, y, color='顏色' ,linewidth=線粗, linestyle='樣式')
'''
plt.figure(num=2, figsize=(5, 8))
plt.plot(x, f(x), color='red' ,linewidth=5, linestyle='--')

# 下面演示簡易打法
plt.figure(3, (5,8))
plt.plot(x, f(x), 'g--', linewidth=10 )

# 在線上加上點，不需要分開打

# 太麻煩
plt.figure()
plt.plot(x, f(x), 'r')
plt.plot(x1, f(x1), 'bo')

# 合併後，簡易
plt.figure() 
plt.plot(x, f(x),'r', x1, f(x1), 'bo')
