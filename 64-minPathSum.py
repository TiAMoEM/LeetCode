class Solution:
    def minPathSum(self, grid) -> int:
        """
        动态规划
        :param grid:
        :return:
        """
        if grid is None:
            return 0
        if grid[0] is None:
            return 0

        rows = len(grid)
        columns = len(grid[0])

        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[rows - 1][columns - 1]
