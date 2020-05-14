"""
华为机试练习6
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格

详细描述：
函数接口说明：
public String getResult(long ulDataInput)
输入参数：
long ulDataInput：输入的正整数

返回值：
String

输入描述:
输入一个long型整数
输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
"""
n = int(input())
arr = []
temp = 2
if n == temp:
    print(n, end=' ')
else:
    while n >= temp:
        k = n % temp
        if k == 0:
            arr.append(temp)
            n = n // temp
        else:
            temp += 1
for i in arr:
    print(i, end=' ')