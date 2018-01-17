# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:33:49 2017

@author: VX
"""
import multiprocessing as mp
from multiprocessing import Process
import time

def job(v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()

def multicore():
    l = mp.Lock()
    v = mp.Value('i', 0)
    p1 = Process(target=job, args=(v, 1, l))
    p2 = Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()
