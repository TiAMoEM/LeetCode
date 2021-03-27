from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp = set(nums)
        arr = []
        for i in range(1, len(nums) + 1):
            if i not in tmp:
                arr.append(i)
        return arr
