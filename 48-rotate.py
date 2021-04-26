from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        新建了一个二维数组，最后通过值拷贝的方式赋值给最初的matrix
        """
        n = len(matrix)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][n - i - 1] = matrix[i][j]
        matrix[:] = ans
