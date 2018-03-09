#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:47:15 2018

@author: wei
"""

# tensors
import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 4).reshape(3, 1)
c = np.dot(a, b)
np.vdot(a, b)

d = np.arange(1, 10)
e = np.arange(1, 10)
np.dot(d, e)
np.vdot(d, e)
