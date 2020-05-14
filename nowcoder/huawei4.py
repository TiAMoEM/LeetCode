"""
华为机试练习4
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)
输出描述:
输出到长度为8的新字符串数组
"""
s1 = input()
s2 = input()
ans = []
s = ""
for i in range(len(s1)):
    length = len(s)
    if length == 8:
        ans.append(s)
        s = ""
    s += s1[i]
if s != "":
    s += '0' * (8-len(s))
    ans.append(s)
s = ""
for i in range(len(s2)):
    length = len(s)
    if length == 8:
        ans.append(s)
        s = ""
    s += s2[i]
if s != "":
    s += '0' * (8-len(s))
    ans.append(s)

for i in ans:
    print(i)