class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for i in range(n)] for j in range(m)]
        res[-1][-1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                val = 0
                if j + 1 < n:
                    val += res[i][j + 1]
                if i + 1 < m:
                    val += res[i + 1][j]
                res[i][j] = max(res[i][j], val)
        
        
        return res[0][0]