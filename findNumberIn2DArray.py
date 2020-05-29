class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            tmp = matrix[i][j]
            if target < tmp:
                j -= 1
            elif target > tmp:
                i += 1
            else:
                return True
        return False