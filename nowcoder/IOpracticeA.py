"""
链接：https://ac.nowcoder.com/acm/contest/320/A
来源：牛客网

输入描述:
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据包括多组。
输出描述:
输出a+b的结果
"""
import sys
lines = sys.stdin.readlines()
a = []
b = []
c = []
for i in range(len(lines)):
    a.append(lines[i].split()[0])
    b.append(lines[i].split()[1])
    c.append(int(a[i]) + int(b[i]))
for i in range(len(c)):
    print(c[i])

