import math
class Solution:
    def reverse(self, x: int) -> int:
        arr = []
        if x >= 0:
            arr.append(str(x)[::-1])
            ans = int(arr[0])
            if ans > math.pow(2, 31) - 1:
                return 0
            return ans
        else:
            x = x * -1
            arr.append(str(x)[::-1])
            ans = -1 * int(arr[0])
            if ans < math.pow(2, 31) * -1:
                return 0
            return ans