#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 00:09:21 2018

@author: wei
"""

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    
#%%
from multiprocessing import Process
import os
import time
import numpy.random as rand

# 子进程要执行的代码
def run_proc1(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(3)
#    for i in range(20):
#        print(name, i)
    print('end child process %s (%s)...' % (name, os.getpid()))

def run_proc2(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(3)
#    for i in range(20):
#        print(name, i)
    print('end child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p1 = Process(target=run_proc1, args=('test',))
    p2 = Process(target=run_proc2, args=('kkkkkk',))
    print('Child process will start.')
    p1.start()
    p2.start()
#    print('good1')
#    p1.join()
#    print('good2')
#    p2.join()
#    print('good3')
    print('all Child process end.')