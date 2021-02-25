class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        if s == "":
            return 0
        dic = {}
        start = 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]] + 1
            temp = i - start + 1
            dic[s[i]] = i
            longest = max(longest, temp)
        return longest
