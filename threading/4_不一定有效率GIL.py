# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:27:43 2017

@author: VX
"""

import threading
from queue import Queue
import copy
import time
#==============================================================================
# normal函數
#==============================================================================
def normal(l):
    total = sum(l)
    print(total)
#==============================================================================
# 線程
#==============================================================================
# 定義任務
def job(l, q):
    res = sum(l)
    q.put(res)
# 定義線程主程式
def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)
#==============================================================================
# 執行
#==============================================================================
if __name__ == '__main__':
    l = list(range(5000000))
    s_t = time.time()
    normal(l*4) # 因為我們的線程有四個，所以我們給一般函式四倍的資料量，類比線程
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)