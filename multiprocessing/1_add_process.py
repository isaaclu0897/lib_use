# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:09:50 2017

@author: VX
"""

import multiprocessing as mp
# import threading as td

def job(a, d):
    print('aaaa')
    
''' 比較
t1 = td.Thread(target=job, args=(a, b))
p1 = mp.process(target=job, args=(1, 2))
t1.start()
p1.start()
t1.join()
p1.join()
'''
if __name__=='__main__':
    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    p1.join()
    print('123')
