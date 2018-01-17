# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 00:07:30 2017

@author: VX
"""
# 設置坐標軸
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 20)
y1 = 3 * x + 5
y2 = x ** 2 - 10

plt.figure()
plt.plot(x, y2, 'b')
plt.plot(x, y1, 'r--', linewidth=2)


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim((-5,7.5))
plt.ylim((-10,40))

new_ticks = np.linspace(-5, 7, 5)
plt.xticks(new_ticks)
a = [-10, 0, 10, 20, 40]
b = [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$']
plt.yticks(a, b)

plt.show()
    
