class Solution:
    def bitwiseComplement(self, N: int) -> int:
        """
        给你一个十进制数 N，请你返回其二进制表示的反码所对应的十进制整数。
        题目要求和476题相同
        :param N:
        :return:
        """
        a = bin(N)[2:]
        b = '1' * len(a)
        return int(a, 2) ^ int(b, 2)