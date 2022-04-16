from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        length = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(length)]
        dp[0][0] = grid[0][0]
        for i in range(1, length):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, length):
            for j in range(1, col):
                dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
