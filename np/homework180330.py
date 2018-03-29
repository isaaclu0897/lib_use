# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 13:22:35 2017

@author: VX
"""
#%%
import numpy as np

# 1-1
np.zeros((3, 3))

# 1-2
A = np.array([5, 8, 10, 1, 3, 13, 15, 27, 20]).reshape((3,3));print('mat_A\n', A)
B = np.array([30, 23, 10, 7, 3, 11, 15, 27, 20]).reshape((3,3));print('mat_B\n', B)
print('mat_A + mat_B\n', A + B)
print('mat_A / mat_B\n', A / B)
print('mat_A · mat_B\n', np.dot(A, B))

# 1-3
A = [5, 8, 10, 1, 3, 13, 15, 27, 20];
a = []
b = []
c = 0
for i in A:
    a.append(i)
    c += 1
    if c >= 3:
        c = 0
        b.append(a)
        a = []
print(np.array(b))
#%%
# 2
A = np.random.randint(0, 10, size=(16, 16))
print(A, '\n', A.T)
