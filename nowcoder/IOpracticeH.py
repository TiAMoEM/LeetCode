"""
链接：https://ac.nowcoder.com/acm/contest/320/H
来源：牛客网

对输入的字符串进行排序后输出
输入描述:
输入有两行，第一行n

第二行是n个空格隔开的字符串
输出描述:
输出一行排序后的字符串，空格隔开，无结尾空格
"""

import sys
lines = sys.stdin.readlines()
length = int(lines[0])
s = []
for i in range(length):
    s.append(lines[1].split()[i])

s.sort()
for i in s:
    print(i, end=" ")