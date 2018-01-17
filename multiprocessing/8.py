# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:06:02 2017

@author: VX
"""

from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()