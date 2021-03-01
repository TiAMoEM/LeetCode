class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        dp = [0 for _ in range(len(text2) + 1)]
        for i in range(1, len(text1) + 1):
            pre = 0
            for j in range(1, len(text2) + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = temp
        return dp[-1]
