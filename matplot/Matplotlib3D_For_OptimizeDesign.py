#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:15:08 2018

@author: wei
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 引入3D繪圖模塊
import numpy as np

# 創建3D圖框
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)

# 設定邊界
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 11)
ax.set_zlim(-50, 50)


# 添加坐標軸
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')


# 定義數學模型
X = np.arange(-2, 2, 0.1)
Y = np.arange(0, 10, 0.1)
X, Y = np.meshgrid(X, Y)
# meshgrid可以將一維的數組結合成二維的網格
F = X**2*Y + 2*X*Y - 3*Y

ax.plot_surface(X, Y, F, rstride=1, cstride=1, cmap=plt.get_cmap('jet'))
''' colormap色表
網上很多人愛用 rainbow
但我個人偏好 jet，因為它明度比較高
色表可以參考[matplotlib官方文檔](https://matplotlib.org/users/colormaps.html)
'''

ax.contourf(X, Y, F, zdir='z', offset=-50, cmap=plt.get_cmap('jet'))
ax.contourf(X, Y, F, zdir='y', offset=11, cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, F, zdir='x', offset=-3, cmap=plt.get_cmap('rainbow'))

plt.show()