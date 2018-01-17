# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:19:45 2017

@author: VX
"""

import threading
import time
#==============================================================================
# 定義線程任務
#==============================================================================
def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
        print('123')
    print('T1 finish\n') 

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')
#==============================================================================
# 定義主程式
#==============================================================================
def main():
    added_thread = threading.Thread(target=thread_job, name='T1') # 線程1加到主程式中
    thread2 = threading.Thread(target=T2_job, name='T2') # 線程2加到主程式中
    added_thread.start() # 線程1開始
    thread2.start() # 線程2開始
    added_thread.join() # 等待線程1結束主程式才會繼續往下執行
    print('all done\n')
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    
#==============================================================================
# 執行
#==============================================================================
if __name__=='__main__':
    main()