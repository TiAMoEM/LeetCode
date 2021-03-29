from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += 4
                if i > 0:
                    if grid[i - 1][j] == grid[i][j] == 1:
                        ans -= 2
                if j > 0:
                    if grid[i][j - 1] == grid[i][j] == 1:
                        ans -= 2
        return ans
