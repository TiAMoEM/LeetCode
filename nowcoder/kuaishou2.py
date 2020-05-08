# -*- coding:utf-8 -*-
"""
牛客网快手19校招测试A
对字符串进行RLE压缩，将相邻的相同字符，用计数值和字符值来代替。例如：aaabccccccddeee，则可用3a1b6c2d3e来代替。
输入描述:
输入为a-z,A-Z的字符串，且字符串不为空，如aaabccccccddeee
输出描述:
压缩后的字符串，如3a1b6c2d3e
"""
import sys

s = input().strip()
# s = sys.stdin.readline().strip()
count = 1
ans = ""
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        ans += str(count) + s[i - 1]
        count = 1
ans += str(count) + s[-1]
print(ans)
