from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b = [1] * len(a)
        tmp = 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for j in range(len(a) - 2, -1, -1):
            tmp = a[j + 1] * tmp
            b[j] *= tmp
        return b
