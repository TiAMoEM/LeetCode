class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        return self.dfs(visited, m, n, k, 0, 0)

    def dfs(self, visited, m, n, k, i, j):
        if i >= m or j >= n or (i, j) in visited or self.digitSum(i) + self.digitSum(j) > k:
            return 0
        visited.add((i, j))
        return 1 + self.dfs(visited, m, n, k, i + 1, j) + self.dfs(visited, m, n, k, i, j + 1)

    def digitSum(self, num: int) -> int:
        ans = 0
        while num:
            ans += num % 10
            num = num // 10
        return ans
