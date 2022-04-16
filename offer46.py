class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        dp = [0 * (len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if int(s[i - 2: i]) >= 10 and int(s[i - 2: i]) <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
