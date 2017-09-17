# -*- coding:utf-8 -*-
"""
这是一个关于次幂计算的函数
"""
import time
def Power():
    for i in range(1, 10):
        n = 10**i # 计算10的i次幂
        start_time = time.time()
        count = 0
        for x in range(0, n):
            count += x
        end_time = time.time()
        print("10^%d:%fs"%(i, (end_time-start_time)))
Power()