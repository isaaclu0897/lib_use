# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:38:48 2017

@author: VX
"""
''' Lock
如果想將一筆資料使用不同的函數接續處理，則需要用到Lock，
線程1 處裡完Lock的資料後，線程2 接著處裡。
一般來說，我們只有在處裡共享內存才用的到。
'''


import threading

def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
