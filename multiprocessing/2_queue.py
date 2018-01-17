# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:14:34 2017

@author: VX
"""

import multiprocessing as mp
# import threading as td

def job(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res) # queue
    
''' 比較
t1 = td.Thread(target=job, args=(a, b))
p1 = mp.process(target=job, args=(1, 2))
t1.start()
p1.start()
t1.join()
p1.join()
'''
if __name__=='__main__':
    q = mp.Queue() 
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)