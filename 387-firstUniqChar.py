class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        i = 0
        while i < len(s):
            if s[i] not in s[:i] and s[i] not in s[i + 1:]:
                return i
            i += 1
        return -1
