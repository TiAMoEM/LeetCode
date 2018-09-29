class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1, 2, 3, 4, 5, 6, 8, 9]
        if n < 9:
            return ans[n]
        x1, x2 = 10, 10
        while x1 > 9 and n < len(ans):
            while x1 % 2 == 0:
                x1 = x1 / 2
            while x1 % 3 == 0:
                x1 = x1 / 3
            while x1 % 5 ==0:
                x1 = x1 / 5
            if x1 == 1:
                ans.append(x2)
            x1 += 1
            x2 += 1
        return ans[n]