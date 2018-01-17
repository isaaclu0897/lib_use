# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 23:19:44 2017

@author: VX
"""

import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(-100,100,50)
x = np.arange(-100,100,15)
y1 = 2 * x +1
y2 = x ** 2

plt.figure(num=1)
plt.plot(x, y1)
plt.plot(x, y2)

plt.figure(num=3, figsize=(4, 3))
plt.plot(x, y1, 'm4')

plt.figure(5)
plt.plot(x, y2, color='red', linewidth=5, linestyle='--')

plt.xlim((-150, 150))
plt.ylim((-1000, 11000))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
newticks = np.linspace(-100, 100, 5)
plt.xticks(newticks)
plt.yticks([300, 700, 1000, 1500],
           [r'$a\ \alpha$', r'$b$', r'$c\ e$', 'd']) 

plt.figure(num=7)
x = np.arange(0, 5, 0.001)
y = np.sin(x)
plt.plot(x, y)

plt.figure()
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, 'ro')
plt.axis([0, 6, -10, 20])

plt.figure()
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, 'bs')
plt.axis([0, 6, -10, 20])

plt.figure()
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, 'bs-')
plt.axis([0, 6, -10, 20])

plt.figure()
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, 'g^')
plt.axis([0, 6, -10, 20])

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.8, 5.6, 1)

plt.figure(11)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'g--')
plt.plot(t3, np.cos(2*np.pi*t3), 'r^')