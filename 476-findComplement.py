class Solution:
    def findComplement(self, num: int) -> int:
        """
        给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
        :param num:
        :return:
        """
        i = 1
        while num >= i:
            i = i << 1
        return i - 1 - num
