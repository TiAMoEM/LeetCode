import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = collections.Counter(s)
        for i in counter.values():
            ans += i // 2 * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1
        return ans
