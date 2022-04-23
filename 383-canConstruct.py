class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rlist = list(ransomNote)
        mlist = list(magazine)
        for i in range(len(rlist)):
            if rlist[i] not in mlist:
                return False
            else:
                mlist.remove(rlist[i])
        return True
