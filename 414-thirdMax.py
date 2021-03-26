from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        tmp = list(set(nums))
        tmp.sort()
        if len(tmp) < 3:
            return tmp[-1]
        return tmp[-3]
