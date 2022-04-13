from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] < numbers[j]:
                return numbers[i]
            else:
                m = (i + j) // 2
                if numbers[m] > numbers[j]:
                    i = m + 1
                elif numbers[m] < numbers[j]:
                    j = m
                else:
                    j = j - 1
        return numbers[i]
