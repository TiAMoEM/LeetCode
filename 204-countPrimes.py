import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 常规解法，LeetCode超时，时间复杂度为O(n^2)
        # tmp = [2, 3]
        # for i in range(4, n):
        #     for j in range(2, int(math.sqrt(i)) + 1):
        #         if i % j == 0:
        #             break
        #     else:
        #         tmp.append(i)
        # return len(tmp)

        # 厄拉多塞筛法，时间复杂度为O(nlog(n))
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
