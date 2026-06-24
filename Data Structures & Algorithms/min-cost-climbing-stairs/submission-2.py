class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        for i in range(n-1, -1, -1):
            s1, s2 = 0, 0
            if i + 1 < n:
                s1 = cost[i + 1]
            if i + 2 < n:
                s2 = cost[i + 2]
            
            cost[i] = min(cost[i] + s1, cost[i] + s2)
        
        return min(cost[0], cost[1])