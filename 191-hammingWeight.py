class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        tmp = bin(n)
        s = str(tmp[2:])
        arr = []
        for i in s:
            arr.append(i)
        return arr.count('1')
