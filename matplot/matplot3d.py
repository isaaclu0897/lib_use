#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:36:56 2018

@author: wei
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # import 3D module

# create 3D figure
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d') 
ax = Axes3D(fig)

# set boundry 
#ax.set_xlim(-3, 3) 
#ax.set_ylim(-1, 11) 
#ax.set_zlim(-50, 50) 
 
# set label 
ax.set_xlabel('x axis') 
ax.set_ylabel('y axis') 
ax.set_zlabel('z axis') 

# set X1, X2 array of value
X1 = np.arange(-10, 10, 1)
X2 = np.arange(-10, 10, 1)
X1, X2 = np.meshgrid(X1, X2)    # X1, X2 mesh to grid  
F = 2*X1**2 + X2**2 + X1*X2 + 4*X1 + X2

ax.plot_surface(X1, X2, F, rstride=1, cstride=1, cmap=plt.get_cmap('jet'))
''' colormap色表 
網上很多人愛用 rainbow 
但我個人偏好 jet，因為它明度比較高 
色表可以參考[matplotlib官方文檔](https://matplotlib.org/users/colormaps.html) 
''' 
# mapping 3D curve to X, Y, Z plane
#ax.contourf(X1, X2, F, zdir='z', offset=-50, cmap=plt.get_cmap('jet')) 
#ax.contourf(X1, X2, F, zdir='y', offset=11, cmap=plt.get_cmap('rainbow')) 
#ax.contourf(X1, X2, F, zdir='x', offset=-3, cmap=plt.get_cmap('rainbow')) 

plt.show()


