class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        tmp = x ^ y
        return bin(tmp).count('1')
