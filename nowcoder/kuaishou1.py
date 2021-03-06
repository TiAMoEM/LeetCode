"""
快手编程题动态规划的问题
题目描述
你需要爬上一个N层的楼梯，在爬楼梯过程中， 每阶楼梯需花费非负代价，第i阶楼梯花费代价表示为cost[i]， 一旦你付出了代价，你可以在该阶基础上往上爬一阶或两阶。
你可以从第 0 阶或者 第 1 阶开始，请找到到达顶层的最小的代价是多少。
N和cost[i]皆为整数，且N∈[2,1000]，cost[i]∈ [0, 999]。

输入描述:
输入为一串半角逗号分割的整数，对应cost数组，例如
10,15,20
输出描述:
输出一个整数，表示花费的最小代价
example:
输入
1,100,1,1,1,100,1,1,100,1
输出
6
"""
import sys
line = sys.stdin.readline()

a = []
for i in range(len(line.strip().split(","))):
    a.append(int(line.strip().split(",")[i]))


def mincost(nums):
    if len(nums) == 0:
        return 0
    if len(nums) <= 2:
        return min(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, len(nums)):
        dp[i] = min(dp[i-1] + nums[i], dp[i-2] + nums[i])
    return min(dp[len(nums)-1], dp[len(nums)-2])


print(mincost(a))




