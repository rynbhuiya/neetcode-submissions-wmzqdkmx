class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        n = target + 1
        res = [0] * n 
        res[0] = 1

        for num in nums:
            for i in range(n - 1, -1, -1):
                if res[i] and i + num < n:
                    res[i + num] = 1
        
        return res[target] == 1