# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 00:16:22 2017

@author: VX
"""

import threading

def thread_job(): # 定義線程的任務
    print('this is added Thread, number is {}'.format(threading.current_thread))

def main(): # 定義主程式
    added_thread = threading.Thread(target=thread_job) # 將定義的線程加到主程式中
    added_thread.start() # 線程開始
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())

if __name__=='__main__':
    main()