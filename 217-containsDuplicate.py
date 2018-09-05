class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        a = len(nums)
        tmp = set(nums)
        b = len(tmp)
        return a != b