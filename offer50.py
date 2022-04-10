class Solution:
    def firstUniqChar(self, s: str) -> str:
        if len(s) == 0:
            return " "
        if len(s) == 1:
            return s
        dic = {}
        for i in s:
            dic[i] = not i in dic
        for i in s:
            if dic[i]:
                return i
        return " "
