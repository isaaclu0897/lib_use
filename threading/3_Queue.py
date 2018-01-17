# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:38:55 2017

@author: VX
"""

import threading
from queue import Queue
import time
#==============================================================================
# 定義線程任務
#==============================================================================
def job(l, q):
    res = 0
    for i in range(len(l)):
        l[i] = l[i] ** 2 + 3 * 5 / 4 + 3 **2
        res += l[i]
        
    # 這裡切記不可用 return，不然值就被傳出去了
    q.put(res) # 將結果放入queue中
    del res, l
#==============================================================================
# 定義主程式
#==============================================================================
def multithreading():
    q = Queue() # 儲存進程結果，在進程中，因為沒有return，所以用的是queue
    threads = []
    data = [list(range(1000000)), list(range(1000000)), list(range(1000000)), list(range(1000000))]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q)) # 新增線程
        t.start()
        threads.append(t) # 將處理完的數據丟到threads中
        
    for thread in threads:# 每個thread 等待數據處理完畢
        thread.join() # [t.join() for t in threads]
    results = []
    for _ in range(4): # 把處理好的數據，從q.put 放入q.get，最後藉由list 打印出結果
        results.append(q.get())
    print(results)
    
def multithreading2():
    q = Queue()
    threads = []
    data = [list(range(10000000)), list(range(1000000)), list(range(1000000)), list(range(1000000))]
    t1 = threading.Thread(target=job, args=(data[0], q))
    t2 = threading.Thread(target=job, args=(data[1], q))
    t3 = threading.Thread(target=job, args=(data[2], q))
    t4 = threading.Thread(target=job, args=(data[3], q))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)
    [t.join() for t in threads]
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)
#==============================================================================
# 執行
#==============================================================================
if __name__=='__main__':
    start = time.time()
    multithreading()
    print('1 時間: {}'.format(time.time()-start))
    start = time.time()
    multithreading2()
    print('2 時間: {}'.format(time.time()-start))