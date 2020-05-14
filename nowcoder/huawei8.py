"""
华为机试练习8
题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开
输出描述:
输出合并后的键值对（多行）
"""
import sys
lines = sys.stdin.readlines()
n = int(lines[0].strip())
dic = {}
for i in range(n):
    k, v = map(int, lines[i+1].strip().split())
    if k in dic:
        dic[k] += v
    else:
        dic[k] = v

for k in dic:
    print(k, dic[k])