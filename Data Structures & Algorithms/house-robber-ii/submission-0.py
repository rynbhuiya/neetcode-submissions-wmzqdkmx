class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return max(rob1, rob2)
        n = len(nums)
        if n == 1:
            return nums[0]
        r1 = robber(nums[0:n-1])
        r2 = robber(nums[1:n][::-1])

        return max(r1, r2)
