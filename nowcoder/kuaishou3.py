"""
快手19校招测试A
一个非空整数数组，选择其中的两个位置，使得两个位置之间的数和最大。
如果最大的和为正数，则输出这个数；如果最大的和为负数或0，则输出0
输入描述:
3,-5,7,-2,8
输出描述:
13
"""
a = input().split(',')
maxm = num = 0
for j in a:
    if num + int(j) > 0:
        num += int(j)
    else:
        num = 0
    maxm = max(maxm, num)
print(maxm)
