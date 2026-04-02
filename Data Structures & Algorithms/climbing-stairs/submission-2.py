import math
class Solution:
    def climbStairs(self, n: int) -> int:
        windows = n // 2
        paths = 1
        while windows:
            paths += math.comb(n - windows, windows)
            windows -= 1
        return paths
        
