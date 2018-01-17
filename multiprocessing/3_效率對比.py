# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:15:31 2017

@author: VX
"""

import multiprocessing as mp
import threading as td
import time
#==============================================================================
# 任務內容
#==============================================================================
def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res) # queue
#==============================================================================
# 進程
#==============================================================================
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p3 = mp.Process(target=job, args=(q,))
    p4 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    res1 = q.get()
    res2 = q.get()
    res3 = q.get()
    res4 = q.get()
    print('multicore:' , res1 + res2 + res3 + res4)
#==============================================================================
# 一般函式
#==============================================================================
def normal():
    res = 0
    for _ in range(4):
        for i in range(1000000):
            res += i+i**2+i**3
    print('normal:', res)
#==============================================================================
# 線程
#==============================================================================
def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t3 = td.Thread(target=job, args=(q,))
    t4 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    res1 = q.get()
    res2 = q.get()
    res3 = q.get()
    res4 = q.get()
    print('multithread:', res1 + res2 + res3 + res4)
#==============================================================================
# 執行
#==============================================================================
if __name__ == '__main__':
    st = time.time()
    normal()
    st1= time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time()-st2)