class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans
