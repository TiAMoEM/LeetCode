class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            row = [1]
            if i == 0:
                ans.append(row)
                continue
            for j in range(1, i):
                num = ans[i - 1][j - 1] + ans[i - 1][j]
                row.append(num)
            row.append(1)
            ans.append(row)
        return ans
