# -*- coding:utf-8 -*-

class Solution:
    def cube(self, n, m, arr):
        """

        :type n: int
        :type m: int
        :type arr: List[int]
        :return:
        """
        height = []
        for i in range(1, n+1):
            height.append(arr.count(i))
        return min(height)

if __name__ == "__main__":
    print(Solution().cube(4, 4, [1, 2, 3, 3]))


# import sys
#
# lines = sys.stdin.readlines()
# n, m = map(int, lines[0].strip().split())
# b = list(map(int, lines[1].strip().split()))
#
# task = []
#
# for i in range(1, n + 1):
#     count = b.count(i)
#     task.append(count)
# print(sorted(task)[0])