"""
华为机试练习9
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
输入描述:
输入一个int型整数
输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
"""
n = input()
arr = []
for i in range(len(n)-1, -1, -1):
    if n[i] not in arr:
        arr.append(n[i])
s = ""
for i in arr:
    s += i
print(int(s))


