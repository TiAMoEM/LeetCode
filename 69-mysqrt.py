class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left = 0
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                return mid
        return right
