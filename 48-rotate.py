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

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        不创建新的二维数组，先进行一次对角交换，再进行一次上线交换，即可
        """
        n = len(matrix)
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
