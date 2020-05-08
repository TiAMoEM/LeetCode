"""
链接：https://ac.nowcoder.com/acm/contest/320/B
来源：牛客网

计算a+b

输入描述:
输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 10^9)
输出描述:
输出a+b的结果
"""
import sys
lines = sys.stdin.readlines()
t = int(lines[0])
a = []
b = []
c = []
for i in range(t):
    a.append(lines[i+1].split()[0])
    b.append(lines[i+1].split()[1])
    c.append(int(a[i]) + int(b[i]))
for i in range(t):
    print(c[i])