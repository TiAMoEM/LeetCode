class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sHash = tHash = 1
        sCount = [0] * 26
        tCount = [0] * 26
        p1 = 2903
        p2 = 29947
        for i in range(0, len(s)):
            sCount[ord(s[i]) - ord('a')] += 1
            tCount[ord(t[i]) - ord('a')] += 1

        for i in range(0, 26):
            sHash = sHash * p1 + sCount[i]
            tHash = tHash * p1 + tCount[i]
            p1 *= p2
        return sHash == tHash

    def isAnagram2(self, s: str, t: str) -> bool:
        lists = list(s)
        lists.sort()
        s1 = "".join(lists)
        listt = list(t)
        listt.sort()
        t1 = "".join(listt)
        return s1 == t1
