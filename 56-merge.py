class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        ans = []
        intervals.sort()
        for i, interval in enumerate(intervals):
            left, right = interval
            if len(ans) == 0 or ans[-1][1] < left:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], right)
        return ans
