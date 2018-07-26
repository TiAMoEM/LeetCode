class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]
        arr = []
        left = 0
        for i, b in enumerate(binary):
            if b == '1':
                arr.append(i - left)
                left = i
        return max(arr)

