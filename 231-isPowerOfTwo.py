class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n <=0:
            return False
        else:
            return n & (n - 1) == 0