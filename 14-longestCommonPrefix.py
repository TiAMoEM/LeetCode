class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        横向扫描
        比较第一个和第二个的最长公共前缀得到结果后和第三个比较，以此类推
        :param strs:
        :return:
        """
        if len(strs) == 0:
            return ""

        ans = strs[0]
        length = len(strs)
        for i in range(1, length):
            ans = self.lcp(ans, strs[i])
            if ans == "":
                break
        return ans

    def lcp(self, str1, str2):
        length = min((len(str1)), len(str2))
        index = 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

    def longestCommonPrefix2(self, strs) -> str:
        """
        纵向扫描
        最长公共前缀长度小于每一个字符串，默认取第一个长度来计算
        """
        if len(strs) == 0:
            return ""

        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]

    """
        python已有zip函数解法
        ans = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans
    """
