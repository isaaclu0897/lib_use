# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:24:08 2017

@author: VX
"""

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes=2)
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    print(res.get())
    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()
