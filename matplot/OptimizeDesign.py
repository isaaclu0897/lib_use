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
X1, X2 = np.meshgrid(X1, X2)    # 1D X1, X2 mesh to 2D grid

# example for notebook 
eq1 = 2*X1**2 + X2**2 + X1*X2 + 4*X1 + X2
eq2 = 2*X1**2 + X2**2
eq3 = X1 * X2
eq4 = X1**2 + 2*X2**2
eq5 = X1**2/2 + X2**2 - 2*X1*X2 - 2*X1 + X2
eq6 = X1**2 + X2**2 + X1*X2 + 6*X1 - X2

F = eq1

# subject for example(still have bug)
#xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
#con1 = 4*xx - yy - 1
#con2 = 4*xx**2 + yy**2 - 1
#con3 = xx + 3
#zz = con3

#ax.plot_surface(zz, yy, xx, alpha=0.2)
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

# if you want to find the minimize.
# first, you need to differental the function.
from sympy import Symbol, solve, diff, cos
t2 = Symbol('t2')
func = cos(2*np.pi*t2)
Dfunc = diff(func, t2)
sol = solve(Dfunc, t2)
print(sol)
# [sympy 教學](https://blog.gtwang.org/useful-tools/sympy-python-library-for-symbolic-mathematics/3/)

# =============================================================================
# reference
# =============================================================================
#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#
#point  = np.array([1, 2, 3])
#normal = np.array([1, 1, 2])
#
#point2 = np.array([10, 50, 50])
#
## a plane is a*x+b*y+c*z+d=0
## [a,b,c] is the normal. Thus, we have to calculate
## d and we're set
#d = -point.dot(normal)
#
## create x,y
#xx, yy = np.meshgrid(range(10), range(10))
#
## calculate corresponding z
#z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
#
## plot the surface
#fig = plt.figure()
#ax = Axes3D(fig)
#ax.plot_surface(xx, yy, z, alpha=0.2)
#
#
##and i would like to plot this point : 
#ax.scatter(point2[0] , point2[1] , point2[2],  color='green')
#
#plt.show()
