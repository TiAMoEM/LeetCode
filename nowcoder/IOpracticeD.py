"""
链接：https://ac.nowcoder.com/acm/contest/320/D
来源：牛客网

计算一系列数的和

输入描述:
输入数据包括多组。
每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
接下来n个正整数,即需要求和的每个正整数。
输出描述:
每组数据输出求和的结果
"""
import sys

lines = sys.stdin.readlines()
c = []
for i in range(len(lines)):
    if int(lines[i].split()[0]) == 0:
        break
    temp = 0
    for j in range(int(lines[i].split()[0])):
        temp += int(lines[i].split()[j + 1])
    c.append(temp)

for i in range(len(c)):
    print(c[i])