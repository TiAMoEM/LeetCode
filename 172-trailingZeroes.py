class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        k = 5
        while n > 0:
            k = n // 5
            count += k
            n = k
        return count
