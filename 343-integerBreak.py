class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        m = n % 3
        if m == 0:
            return 3 ** (n // 3)
        elif m == 1:
            return 3 ** (n // 3 - 1) * 4
        else:
            return 3 ** (n // 3) * 2
