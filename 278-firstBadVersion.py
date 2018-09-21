# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = n
        while b - a != 1:
            if isBadVersion((a + b) // 2) == True:
                b = (a + b) // 2
            else:
                a = (a + b) // 2
        return b