class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m, cnt = len(strs), len(strs[0]), 0
        f = list(strs[0])
        for i in range(1, n):
            for j in range(m):
                if strs[i][j] < strs[i - 1][j] and f[j] != ".":
                    f[j] = "."
                    cnt += 1
        return cnt