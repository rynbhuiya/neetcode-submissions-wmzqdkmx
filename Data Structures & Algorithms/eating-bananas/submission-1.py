import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        res = high

        while low <= high:
            mid = (low + high) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time > h:
                low = mid + 1
            elif time <= h:
                high = mid - 1
                res = min(res, mid)
            
            
        return res