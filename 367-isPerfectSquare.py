class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 4:
            return False
        l = 2
        r = num // 2

        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
