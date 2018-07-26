class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        a = 0
        b = c ** 0.5 // 1
        while a <= b:
            cur = a ** 2 + b ** 2
            if cur < c:
                a += 1
            elif cur > c:
                b -= 1
            else:
                return True
        return False