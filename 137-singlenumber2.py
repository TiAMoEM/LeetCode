class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
        :param nums:
        :return:
        """
        for i in nums:
            if nums.count(i) == 1:
                return i