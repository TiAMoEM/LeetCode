class Solution:
    # def repeatedSubstringPattern(self, s: str) -> bool:
    #     """
    #     暴力查找的方法
    #     :param s:
    #     :return:
    #     """
    #     n = len(s)
    #     for i in range(1, n // 2 + 1):
    #         if n % i == 0:
    #             flag = True
    #             for j in range(i, n):
    #                 if s[j] != s[j - i]:
    #                     flag = False
    #                     break
    #             if flag:
    #                 return True
    #     return False

    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        字符串s如果符合条件时不断移动第一个字符到最后，那么一定会在重复一轮前出现字符串s
        所以可以直接用s+s拼接两个s后，去除第一个和最后一个字符，用长为s的窗口去滑动匹配或是否包含s
        :param s:
        :return:
        """
        string = s + s
        if string[1:-1].find(s) == -1:
            return False
        else:
            return True
