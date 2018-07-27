class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 0
        b = x
        c = x // 2
        while a <= b:
            if c ** 2 > x:
                b = c - 1
                c = (b + a) // 2
            elif c ** 2 < x:
                a = c + 1
                c = (b + a) // 2
            else:
                return c
        return c