class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        pre = [1, 1]
        current = []
        for i in range(2, rowIndex + 1):
            current.append(1)
            for j in range(i - 1):
                current.append(pre[j] + pre[j + 1])
            current.append(1)
            pre = current.copy()
            current.clear()
        return pre