"""
华为机试练习14
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
"""
import sys
lines = sys.stdin.readlines()
n = int(lines[0])
words = []
for i in range(n):
    words.append(lines[i+1].strip())
words = sorted(words)
for word in words:
    print(word)

