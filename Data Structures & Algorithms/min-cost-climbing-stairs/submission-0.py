class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0
        
        i = len(cost)

        while i > 1:
                if cost[i - 2] <= cost[i - 1]:
                    i -= 2
                    total += cost[i]
                else:
                    i -= 1
                    total += cost[i]

        return total