"""
暴力解法
测试用例："aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"会出现超时情况
class Solution:
    def longestPalindrome(self, s: str) -> str:
        \"""
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
        :param s:
        :return:
        \"""
        n = len(s)
        if n == 1:
            return s
        ans = ""
        longest = 0
        strlist = []
        for i in range(n - 1):
            for j in range(i, n):
                if s[i] == s[j]:
                    strlist.append(s[i:j+1])
        for i in range(len(strlist)):
            if self.palindrome(strlist[i]) == True:
                if longest < len(strlist[i]):
                    longest = len(strlist[i])
                    ans = strlist[i]
        return ans

    def palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        动态规划法
        :param s:
        :return:
        """
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
