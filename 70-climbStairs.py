class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            ans = 0
            for i in range(3, n + 1):
                ans = a + b
                a, b = b, ans
            return ans
