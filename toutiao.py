# -*- coding:utf-8 -*-
"""
题目：
有n个人围成一圈，顺序排号1-n。
从第一个人开始报数（从1到k报数），
凡报到k的人退出圈子，
问最后留下的是原来第几号的那位。
"""

def stay(n, k):
    nlist = []
    step = -1
    flag = True
    for i in range(1, n+1):
        nlist.append(i)
    while flag:
        for j in range(k):
            if len(nlist) == 1:
                flag = False
                return nlist[0]
            if step == len(nlist) - 1:
                step = -1
            step += 1
            if j == k-1:
                nlist.remove(nlist[step])
                step -= 1


print(stay(100, 3))


