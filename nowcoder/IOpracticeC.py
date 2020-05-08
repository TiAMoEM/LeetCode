"""
链接：https://ac.nowcoder.com/acm/contest/320/C
来源：牛客网

计算a+b

输入描述:
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入
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
    if int(a[i]) == 0 and int(b[i]) == 0:
        break
    c.append(int(a[i]) + int(b[i]))
for i in range(len(c)):
    print(c[i])