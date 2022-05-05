from typing import List
import collections


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        length = 10
        dic = collections.defaultdict(int)
        for i in range(len(s) - length + 1):
            tmp = s[i: i + length]
            dic[tmp] += 1
            if dic[tmp] == 2:
                ans.append(tmp)
        return ans
