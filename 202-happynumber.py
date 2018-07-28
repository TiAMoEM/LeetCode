class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = []
        if n == 1:
            return True
        else:
            while n not in arr and n != 1:
                arr.append(n)
                n = sum(int(d) ** 2 for d in str(n))
            if n == 1:
                return True
            else:
                return False