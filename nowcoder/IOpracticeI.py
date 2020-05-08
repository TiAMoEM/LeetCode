"""
链接：https://ac.nowcoder.com/acm/contest/320/I
来源：牛客网

对输入的字符串进行排序后输出
输入描述:
多个测试用例，每个测试用例一行。

每行通过空格隔开，有n个字符，n＜100
输出描述:
对于每组测试用例，输出一行排序过的字符串，每个字符串通过空格隔开
"""
import sys
lines = sys.stdin.readlines()

for i in range(len(lines)):
    a = []
    for j in range(len(lines[i].strip().split())):
        a.append(lines[i].strip().split()[j])
    a.sort()
    for j in a:
        print(j, end=" ")


